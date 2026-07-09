# Patient Privacy Management System
This system manages patient data using a JSON file as a small database and includes a privacy‑audit mechanism.
It demonstrates how sensitive information can be stored, displayed, and securely removed according to privacy rules.

Features
Stores patient information (name, citizenServiceNumber, blood_group) in patient.json

Loads and prints the current database contents to the terminal

Removes sensitive data (citizenServiceNumber) from the JSON file

Logs the deletion event in privacy_audit.txt

Shows how to handle personal data safely and transparently

How it works
The system creates a JSON file containing patient details.

It reads the file and prints the current database information.

It loads the JSON file again and deletes the sensitive field (citizenServiceNumber).

It writes the updated data back to the JSON file.

It appends a privacy‑audit message to privacy_audit.txt confirming the secure deletion.

Learning Purpose
This project helps practice:

JSON creation, reading, updating, and deletion

Handling sensitive information

File logging for compliance and auditing

Building small backend components with privacy awareness

Understanding how real systems manage personal data securely
