import csv

findings = []
failed_logins = {}
failed_login_ips = {}

with open("security_logs.csv", newline="") as file:
    reader = csv.DictReader(file)

    for event in reader:
        if event["status"] == "Failed":
            username = event["username"]

            if username not in failed_logins:
                failed_logins[username] = 0

            failed_logins[username] += 1
            failed_login_ips[username] = event["source_ip"]
   
        if event["status"] == "Success" and event["country"] != "US":
            print("MEDIUM:", event["username"], "logged in successfully from", event["country"])

            findings.append({
                "username": event["username"],
                "source_ip": event["source_ip"],
                "country": event["country"],
                "severity": "Medium",
                "finding": "Successful login from unusual geographic location",
                "recommendation": "Verify the login with the user and investigate the source IP"
        })
for username, count in failed_logins.items():
    if count >= 5:
        print("HIGH:", username, "had", count, "failed login attempts - possible brute-force activity!")

        findings.append({
            "username": username,
            "source_ip": failed_login_ips[username],
            "country": "",
            "severity": "High",
            "finding": "Possible brute-force activity",
            "recommendation": "Investigate the account and review authentication activity"
        })

with open("security_findings.csv", "w", newline="") as report_file:
    fieldnames = ["username", "source_ip", "country", "severity", "finding", "recommendation"]
    writer = csv.DictWriter(report_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(findings)