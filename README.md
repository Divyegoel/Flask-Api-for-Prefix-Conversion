# Prefix Expression Evaluator API

## Description

This project provides a **Flask API** for evaluating **prefix expressions**. Prefix notation (also known as Polish notation) is a mathematical notation in which operators precede their operands. This API accepts a prefix expression as input and returns the evaluated result.

## Features
- Supports basic arithmetic operations: **Addition**, **Subtraction**, **Multiplication**, and **Division**.
- Handles expressions with **double-digit** numbers.
- Simple and easy-to-use RESTful API.

## Prerequisites

- **Python 3.x**
- **Flask** library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Divyegoel/Flask-Api-for-Prefix-Conversion
cd Flask-Api-for-Prefix-Conversion
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install flask
```

## Usage
### 1. Run the Flask Server
bash
```
python api.py
```
By default, the server runs on http://127.0.0.1:5000.

### 2. Send a POST Request
You can use curl to send a request or use tools like Postman.

Example with curl
bash
```
curl -X POST http://127.0.0.1:5000/api/evaluate-prefix \
-H "Content-Type: application/json" \
-d "{\"expression\": \"+ 9 * 2 3\"}"
```
Expected Response:
json
```
{
  "result": 15
}
```
### Note: Please have spaces between the input like "+ 9 * 2 3"
## Examples:

- **Input**: `+ 9 * 2 3`
- **Output**: `15`

- **Input**: `* + 4 5 3 / 20 2`
- **Output**: `7`

- **Input**: `* + 3 5 + 6 34`
- **Output**: `320`
