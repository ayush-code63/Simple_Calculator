from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.json
        expression = data['expression']
        
        # Replace common functions for evaluation
        expression = expression.replace('sin(', 'math.sin(')
        expression = expression.replace('cos(', 'math.cos(')
        expression = expression.replace('tan(', 'math.tan(')
        expression = expression.replace('log(', 'math.log10(')
        expression = expression.replace('ln(', 'math.log(')
        expression = expression.replace('sqrt(', 'math.sqrt(')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        expression = expression.replace('^', '**')
        
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
