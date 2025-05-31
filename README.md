# Multi-Agent-AI-System
To automatically identify and understand different types of documents like emails, invoices, and PDFs, extract important information from them, and store this data in a shared memory system for easy access and further use.

## Objective
The goal of this project is to automatically detect the type of input document (like Email, JSON, or PDF), extract useful information from it, and save the result in a shared memory space for further use.

This can help automate document handling tasks, like sorting emails, reading invoice data, or classifying files based on their purpose.

## Folder Structure

```text
multi_agent_ai/
│
├── agents/
│   ├── json_agent.py        
│   ├── email_agent.py         
│   └── pdf_agent.py
       
├── input_samples/
│   ├── sample.json           
│   ├── sample_email.txt       
│   └── sample.pdf             
│
├── classifier.py              
├── memory.py                 
├── main.py                    
├── requirements.txt           
```
## Components

### 1. Classifier Agent
It reads the content of a file and decides:
What type of file it is (like Email, JSON, or PDF)
What the content is about (like an Invoice, Complaint, or RFQ)

#### Purpose: 
This helps send the file to the correct agent to handle it properly.

### 2. Email Agent
Processes basic email structure and handles email content.

#### It extracts:
Sender – Who sent the email

Subject – What the email is about

Urgency – Checks if the email is marked or feels urgent

#### Purpose:
Helps sort and process emails automatically, like in customer support or sales systems.

### 3. JSON Agent
It works with structured data in JSON format, usually from documents like invoices.

#### It extracts:
Invoice number

Date

Total amount

Bonus: It also checks if any of these fields are missing.

#### Purpose:
It simplifies reading invoice data and saves time by avoiding manual checks.

#### 4. Shared Memory
Stores results temporarily while the program runs.

#### It stores:
Extracted data (like sender, invoice total, etc.),
File type and intent

Timestamp of when it was stored.

#### Purpose: 
Makes data accessible to other agents if needed later. This can be expanded later to use tools like Redis or SQLite to save data even after the program ends.

## Working
1. You run the program using `main.py`.
2. It reads sample files from the `data/sample_inputs/` folder.
3. The content is classified based on format (like Email or JSON).
4. It’s passed to the right agent (Email Agent or JSON Agent).
5. Useful details are extracted and saved to shared memory.
6. Results are printed to the console.

## How to Execute
   #### Install the requirements:
   pip install -r requirements.txt



   #### Run the main.py :
   python main.py
