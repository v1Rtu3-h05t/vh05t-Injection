# vh05t-Injection
This tool is designed to test a web application for SQL injection vulnerabilities by sending crafted payloads to various URL parameters and analyzing the server's response. It's a basic scanner that helps identify weak spots where malicious SQL code could be injected.
⚙️ How It Works
1. User Input
You start by entering a target URL (e.g., http://example.com/login).

The script assumes this URL accepts query parameters (like ?user=admin).

2. Payloads
It uses a list of SQL injection payloads—these are snippets of SQL code designed to trick the server into revealing data or bypassing authentication.

Examples include:

' OR '1'='1 → classic login bypass

UNION SELECT → attempts to merge malicious queries with legitimate ones

EXISTS and COUNT(*) → used to probe for the existence of specific data

3. Parameters
The script tests each payload against a list of common parameter names like file_path, command, payload, etc.

It constructs URLs like: http://example.com?command=' OR '1'='1

4. Curl Execution
For each combination of parameter and payload, it runs a curl command to send the request to the server.

It captures and prints the server's response, which may reveal whether the injection was successful.

5. Output
Results are printed with color-coded formatting:

Blue for scan details

Yellow for errors

Red for the banner
