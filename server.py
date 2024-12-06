from flask import Flask, request, jsonify
from flask_cors import CORS
import sys, io

app = Flask(__name__)
CORS(app)

@app.route('/execute_python', methods=['POST'])
def execute_python():
    python_code = request.data.decode('utf-8')

    try:
        # Execute Python code here, capturing output
        output = io.StringIO()
        sys.stdout = output
        exec(python_code)
        sys.stdout = sys.__stdout__

        return jsonify({'output': output.getvalue()})
    except Exception as e:
        print(f"Error executing Python code: {str(e)}")
        return jsonify({'error': f"An error occured: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
