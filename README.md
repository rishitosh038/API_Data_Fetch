# Public API Integration Using Python

## Project Overview

This project demonstrates how to consume a public REST API using Python.

The script:
- Sends a GET request to a public API
- Checks HTTP status codes
- Parses JSON response
- Extracts required fields
- Handles errors gracefully
- Saves API response to a local JSON file

This project helps understand real-world API communication and JSON parsing.

---

## Tools Used

- Python 3.x
- requests library
- json module (built-in)
- VS Code

Install requests (if not installed):

pip install requests

---

## API Used

Official Joke API  
Endpoint:

https://official-joke-api.appspot.com/random_joke

### Sample JSON Response:

{
  "type": "general",
  "setup": "Why does a chicken coop only have two doors?",
  "punchline": "Because if it had four doors it would be a chicken sedan.",
  "id": 356
}

---

## Project Structure

api_data_fetch.py  
quote_data.json  
README.md  

---

## How to Run the Project

1. Open terminal in project directory
2. Run:

python api_data_fetch.py

3. The program will:
   - Fetch a random joke
   - Display it in formatted output
   - Save the JSON response to quote_data.json

---

## Features Implemented

✔ GET request using requests  
✔ HTTP status code checking  
✔ JSON parsing  
✔ Nested data extraction  
✔ Exception handling (Timeout & Request errors)  
✔ Saving response to local file  
✔ Clean formatted output  

---

## Error Handling Included

The script handles:

- Network errors
- Timeout errors
- Invalid status codes
- File writing errors

Example:

except requests.exceptions.Timeout:
    print("Request Timed Out ❌")

---

## Concepts Covered

- What is an API?
- What is REST API?
- HTTP methods (GET)
- Status Codes (200, 404, 500)
- JSON parsing in Python
- Handling nested dictionaries
- Exception handling
- File operations

---

## Learning Outcome

After completing this task, you can:

- Communicate with external APIs
- Parse JSON into Python dictionaries
- Extract nested JSON data
- Handle API failures professionally
- Store API responses locally
- Build data-driven backend applications

---
