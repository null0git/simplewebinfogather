Advanced Website Information Gathering Tool
This tool is a Python and Flask-based web application for gathering detailed information about websites. It detects various attributes such as IP address, HTTP headers, DNS records, SSL certificate details, and technologies/frameworks used on the website. The tool organizes and animates the output, providing an engaging and intuitive interface for users.

Features
IP Address Retrieval: Fetches the IP address associated with a domain.
HTTP Header Analysis: Retrieves HTTP headers and displays them in a readable format.
DNS Records: Collects and displays DNS records (A, NS, MX, TXT).
SSL Certificate Details: Provides SSL information including issuer, subject, and validity dates.
Technology Detection: Detects technologies, libraries, and frameworks used by the target site.
Categorized and Animated Output: Organizes information into distinct categories with a clean, animated interface.
Built With
Flask: For handling web requests and serving the frontend.
Requests: For sending HTTP requests to gather headers.
Wappalyzer: For detecting technologies and frameworks used on the website.
dnspython: For DNS record retrieval.
socket and ssl: For retrieving IP address and SSL certificate information.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/website-info-gathering-tool.git
cd website-info-gathering-tool
Install dependencies:

bash
Copy code
pip install flask requests dnspython socket Wappalyzer python-Wappalyzer
Run the Flask application:

bash
Copy code
python app.py
Open in Browser: Visit http://127.0.0.1:5000 to access the tool.

Usage
Enter Domain: In the input field, enter the domain of the target website (e.g., example.com).
Scan: Click the Scan button to retrieve and categorize information.
View Results: The tool will display:
IP Address
HTTP Headers
DNS Records
SSL Information
Detected Technologies
File Structure
php
Copy code
.
├── app.py                 # Main application code
├── templates/
│   └── index.html         # HTML for the main page
├── static/
│   ├── style.css          # CSS styles
│   └── script.js          # JavaScript functions
└── README.md              # Documentation
Screenshots
Input Screen

Sample Results Screen

Libraries and Tools Used
Flask: A lightweight web application framework for Python.
Wappalyzer: A tool that detects various technologies and frameworks on websites.
dnspython: DNS toolkit for Python.
requests: For handling HTTP requests.
socket: For network communication.
ssl: For SSL certificate information.
