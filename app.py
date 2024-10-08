from flask import Flask, request, jsonify, render_template
import subprocess
import os
import time
from pyvirtualdisplay import Display

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    # Start a new virtual display
    with Display(visible=0, size=(800, 600)) as display:
        # Set the DISPLAY environment variable
        os.environ['DISPLAY'] = f":{display.display}"

        # Save the C++ code from the request
        code = request.json.get('code', '')

        # Write the code to test.cpp
        with open('test.cpp', 'w') as f:
            f.write(code)

        # Compile the C++ code
        compile_process = subprocess.run(['g++', 'test.cpp', '-o', 'test', '-lgraph'], 
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if compile_process.returncode != 0:
            return jsonify({'error': compile_process.stderr.decode()}), 400

        # Run the compiled program
        run_process = subprocess.Popen(['./test'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the GUI to initialize
        time.sleep(10)

        # Save the screenshot in the static folder
        scrot_process = subprocess.run(['scrot', 'static/screenshot.png'])

        if scrot_process.returncode != 0:
            return jsonify({'error': 'Failed to take screenshot'}), 400

        return jsonify({'message': 'Program running', 'screenshot': '/static/screenshot.png'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
