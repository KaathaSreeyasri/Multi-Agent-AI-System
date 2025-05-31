from agents.classifier_agent import classify_and_route
from memory.shared_memory import SharedMemory

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def process_file(file_path, file_type):
    content = read_file(file_path)
    memory = SharedMemory()
    result = classify_and_route(content, memory)
    print("[RESULT]", result)

if __name__ == "__main__":
    # Test cases with example files
    process_file("data/sample_inputs/input_email.txt", "email")
    process_file("data/sample_inputs/input_invoice.json", "json")
    process_file("data/sample_inputs/input_doc.pdf", "pdf")
