from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def log(x):
    import math
    return math.log10(x)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        num1 = float(data['num1'])
        operation = data['operation'].lower()
        
        if operation == 'log':
            if num1 <= 0:
                result = "Error! Logarithm undefined for non-positive numbers."
            else:
                result = log(num1)
        else:
            num2 = float(data['num2'])
            if operation == 'addition':
                result = add(num1, num2)
            elif operation == 'subtraction':
                result = subtract(num1, num2)
            elif operation == 'multiplication':
                result = multiply(num1, num2)
            elif operation == 'division':
                result = divide(num1, num2)
            elif operation == 'power':
                result = power(num1, num2)
            else:
                result = "Invalid Operation"
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
