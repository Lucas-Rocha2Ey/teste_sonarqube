import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/v1/show_password')
def show_password():
    password = "secret_password"
    return password

@app.route('/api/v1/run_command')
def run_command():
    command = request.args.get('command')
    result = os.system(command)
    return str(result)

@app.route('/api/v1/files')
def read_file():
    filepath = request.args.get('filepath')
    file = open(filepath, 'r')
    content = file.read();
    file.close()
    return content

def unused_function():
    print("Estou perdido aqui!")

def accumulate_large_list():
    large_list = []
    for i in range(10000000):
        large_list.append(i)
    return sum(large_list)

if __name__ == "__main__":
    app.run(debug=True)