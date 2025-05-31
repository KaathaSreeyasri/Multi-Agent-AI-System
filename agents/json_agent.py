import json

def handle_json(content: str, memory):
    print("[LOG] Processing JSON content...")
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}

    # Simple extraction & validation example
    required_fields = ["invoice_number", "date", "total_amount"]
    missing_fields = [field for field in required_fields if field not in data]

    result = {
        "extracted_data": {field: data.get(field) for field in required_fields if field in data},
        "missing_fields": missing_fields,
        "status": "Processed JSON"
    }

    memory.store('last_json_data', result)

    if missing_fields:
        result["status"] = "Missing fields detected"

    return result
