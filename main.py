from flask import Flask, render_template, request, jsonify
import socket
import requests
import dns.resolver
import ssl
from Wappalyzer import Wappalyzer, WebPage

app = Flask(__name__)
wappalyzer = Wappalyzer.latest()

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return "Not Available"

def get_http_headers(url):
    try:
        response = requests.get(url)
        return dict(response.headers)
    except Exception:
        return "Not Available"

def get_dns_records(domain):
    records = {}
    try:
        for record_type in ["A", "NS", "MX", "TXT"]:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(rdata) for rdata in answers]
    except Exception:
        records = "Not Available"
    return records

def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
            return {
                "Issuer": cert.get('issuer'),
                "Subject": cert.get('subject'),
                "Valid From": cert.get('notBefore'),
                "Valid Until": cert.get('notAfter')
            }
    except Exception:
        return "Not Available"

def get_technologies(url):
    try:
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze_with_versions_and_categories(webpage)
        return technologies
    except Exception:
        return "Not Available"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.json.get('domain')
    url = f"http://{domain}"
    data = {
        "IP Address": get_ip(domain),
        "HTTP Headers": get_http_headers(url),
        "DNS Records": get_dns_records(domain),
        "SSL Information": get_ssl_info(domain),
        "Technologies": get_technologies(url)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
