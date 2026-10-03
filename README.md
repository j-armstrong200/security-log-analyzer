# Security Log Analyzer

Python-based security log analysis project for identifying suspicious authentication activity and generating security findings.

## Overview

This project simulates a basic security log analysis workflow using Python. The script analyzes sample authentication logs to identify potentially suspicious activity, including repeated failed login attempts and successful logins from unusual geographic locations.

The goal of the project is to demonstrate basic security monitoring, log analysis, threat detection, severity classification, and automated security reporting.

## Security Checks

The Python script checks for:

- Multiple failed login attempts associated with a user account
- Five or more failed login attempts indicating possible brute-force activity
- Successful logins originating outside the United States
- Source IP addresses associated with suspicious authentication activity
- Geographic location associated with authentication events
- Severity levels for identified security findings
- Remediation recommendations for detected security issues
- Automated generation of a CSV security findings report

## Technologies and Concepts

- Python
- Security Log Analysis
- Authentication Monitoring
- Brute-Force Detection
- Geographic Login Analysis
- Source IP Analysis
- Threat Detection
- Security Monitoring
- Risk Severity Classification
- Incident Investigation
- Security Remediation
- CSV Data Analysis
- Automated Security Reporting

## Sample Findings

The analyzer identifies findings such as:

```text
MEDIUM: tlee logged in successfully from Russia
HIGH: bwilliams had 5 failed login attempts - possible brute-force activity!
```

The generated report includes supporting information such as the username, source IP address, country, severity level, finding, and remediation recommendation.

## Files

- `log_analyzer.py` - Python script that analyzes authentication logs and generates security findings
- `security_logs.csv` - Sample authentication log data
- `security_findings.csv` - Automatically generated security findings report
- `README.md` - Project documentation

## What I Learned

This project helped me practice using Python to analyze security log data and automate basic threat detection. I learned how to parse CSV authentication logs, use dictionaries to track failed login attempts, identify possible brute-force activity, and detect successful logins from unusual geographic locations.

I also gained experience associating security findings with source IP addresses and geographic information, assigning severity levels, creating remediation recommendations, and generating structured security reports for investigation.

## Disclaimer

This project uses fictional sample authentication data and is intended for educational and portfolio purposes only.