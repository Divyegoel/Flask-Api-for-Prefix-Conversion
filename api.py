from flask import Flask, request, jsonify

app = Flask(__name__)
# Logic for prefix expression evaluation
def evaluate_prefix(expression):
    stack = []
    
    operators = {'+', '-', '*', '/'}
    
    # Split the expression and traverse it from right to left
    tokens = expression.split()[::-1]

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(int(operand1 / operand2)) 

    return stack.pop()

# Define API endpoint
@app.route('/api/evaluate-prefix', methods=['POST'])
def evaluate_prefix_api():
    try:
        data = request.json
        expression = data.get('expression', '')
        
        if not expression:
            return jsonify({'error': 'No expression provided'}), 400
        
        result = evaluate_prefix(expression)
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
