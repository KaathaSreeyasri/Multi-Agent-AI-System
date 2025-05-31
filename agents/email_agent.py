import re

def handle_email(content: str, memory):
    print("[LOG] Processing Email content...")

    # Simple extraction: sender, subject, urgency based on keywords
    sender = re.search(r"from:\s*(.*)", content, re.IGNORECASE)
    subject = re.search(r"subject:\s*(.*)", content, re.IGNORECASE)
    urgency = "High" if "urgent" in content.lower() else "Normal"

    extracted = {
        "sender": sender.group(1).strip() if sender else "Unknown",
        "subject": subject.group(1).strip() if subject else "Unknown",
        "urgency": urgency
    }

    memory.store('last_email_data', extracted)

    return {
        "status": "Processed Email",
        "extracted": extracted
    }
