import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Erro 1: Exposição de dados sensíveis
@app.route('/api/v1/show_password')
def show_password():
    password = "secret_password" # Never expose sensitive data in code
    return password

@app.route('/api/v1/run_command')
def run_command():
    # Erro 2: Injeção de comando
    command = request.args.get('command')
    result = os.system(command) # Never use unfiltered user's input to run system command
    return str(result)

@app.route('/api/v1/files')
def read_file():
    filepath = request.args.get('filepath')
    # Erro 3: Leitura de caminho de arquivo tratada inseguramente
    file = open( filepath , 'r') # Dangerous path traversal without checking
    content = file.read();
    file.close()
    return content

# Erro 4: função que nunca é usada
def unused_function():
    print("Estou perdido aqui!")

# Erro 5: Uso desnecessário de recursos em um loop
def accumulate_large_list():
large_list = []
    for i in range(10000000):
        large_list.append(i)
    return sum(large_list)

if __name__ == "__main__":
    app.run(debug = True)