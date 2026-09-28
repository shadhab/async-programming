import json

INPUT_FILE = "email.json"

def read_email():
    with open (INPUT_FILE,"r",encoding="utf-8") as file:
        emails = json.load(file)

        print(f"Loaded {len(emails)} emails.")
        return emails

    