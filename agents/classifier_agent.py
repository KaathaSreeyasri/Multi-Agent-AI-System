from memory.shared_memory import SharedMemory

def classify_content_rule_based(content: str) -> dict:
    content_lower = content.lower()

    if content_lower.strip().startswith('{') and content_lower.strip().endswith('}'):
        format_type = "JSON"
    elif "@" in content_lower and ("subject:" in content_lower or "from:" in content_lower):
        format_type = "Email"
    elif "%pdf" in content_lower or "/page" in content_lower or content_lower.strip().endswith("pdf"):
        format_type = "PDF"
    else:
        format_type = "Unknown"

    # Simple keyword-based intent detection
    if "invoice" in content_lower:
        intent = "Invoice"
    elif "rfq" in content_lower or "request for quotation" in content_lower:
        intent = "RFQ"
    elif "complaint" in content_lower:
        intent = "Complaint"
    elif "regulation" in content_lower:
        intent = "Regulation"
    else:
        intent = "Unknown"

    return {"format": format_type, "intent": intent}

def classify_and_route(content: str, memory: SharedMemory):
    print("[LOG] Classifying content...")

    classification = classify_content_rule_based(content)

    print(f"[LOG] Classification: {classification}")

    # Log classification in shared memory
    memory.store('last_classification', classification)

    format_type = classification.get("format", "").lower()

    if format_type == "json":
        from agents.json_agent import handle_json
        return handle_json(content, memory)
    elif format_type == "email":
        from agents.email_agent import handle_email
        return handle_email(content, memory)
    elif format_type == "pdf":
       
        
        return classification
    else:
        print("[LOG] No suitable agent found for this content.")
        return classification
