function startScan() {
    const domain = $("#domainInput").val();
    if (!domain) {
        alert("Please enter a domain.");
        return;
    }
    $.ajax({
        url: "/scan",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ domain }),
        success: function (response) {
            $("#results").fadeIn();
            $("#ipAddress .data").text(response["IP Address"]);
            $("#httpHeaders .data").html("<pre>" + JSON.stringify(response["HTTP Headers"], null, 2) + "</pre>");
            $("#dnsRecords .data").html("<pre>" + JSON.stringify(response["DNS Records"], null, 2) + "</pre>");
            $("#sslInfo .data").html("<pre>" + JSON.stringify(response["SSL Information"], null, 2) + "</pre>");
            $("#technologies .data").html("<pre>" + JSON.stringify(response["Technologies"], null, 2) + "</pre>");
        },
        error: function () {
            alert("Error gathering information.");
        }
    });
}
