# =======================================
# Igor DAzevedo - Data Scientist
# python 3 - mongodb - flask - html/mdl
# IDE: VSCODE
# =======================================

from flask import Flask, session, render_template, request, redirect, url_for, jsonify
import pymongo
from pymongo import MongoClient
import json
import urllib3
import jinja2


app = Flask(__name__)

@app.route("/")
def index():
    mongo = MongoClient()
    mongo = MongoClient('mongodb://127.0.0.1:27017')
    db_data01 = mongo['teste_db']
    registros = mongo.db.db_data01.find()
    # exibe no output os registros existentes no banco de dados
    print(registros)
    regs = []
    
    for xn in registros:
        print(xn)
        if len(xn) == 4:
            regs.append({'nome':xn['nome'], 'email':xn['email'], 'telefone':xn['telefone']})
        print("---")
    
    insert_record()
    return render_template("index.html", regs=regs)   





# cadastro inicial --------------------------------------------------------
# cadastra collections: 
# {'nome': 'Lucas', 'email': 'lucas@gmail.com', 'telefone': '11 99389-3244'}
# {'nome': 'Lara' , 'email': 'lara@gmail.com' , 'telefone': '11 99333-3556'} 
# -----------
@app.route("/inicio")
def cadastroInicial():
        mongo = MongoClient()
        mongo = MongoClient('mongodb://127.0.0.1:27017')
        db_data01 = mongo['teste_db']
        newUser = mongo.db.db_data01
        newUser.insert({'nome': 'Lucas', 'email': 'lucas@gmail.com', 'telefone': '11 99389-3244'}, {'nome': 'Lara', 'email': 'lara@gmail.com', 'telefone': '11 99333-3556'})
        return 'Collections cadastradas.'



# recebe dados do form e envia para os end points: insert_records e get_records
# apenas exibe os registros que tenham os 3 campos. registros com menos campos sao descartados.
# para exibir apenas os dados que estamos inserindo para este teste.
@app.route("/registros")
def get_records():
    mongo = MongoClient()
    mongo = MongoClient('mongodb://127.0.0.1:27017')
    db_data01 = mongo['teste_db']
    registros = mongo.db.db_data01.find()
    # exibe no output os registros existentes no banco de dados
    print(registros)
    regs = []
    
    for xn in registros:
        print(xn)
        if len(xn) == 4:
            regs.append({'nome':xn['nome'], 'email':xn['email'], 'telefone':xn['telefone']})
        print("---")
    
    insert_record()
    return render_template("index.html", regs=regs)   


# insert_record - recebe os dados do formulario e cadastra em teste_db

def insert_record():
    if request.method == 'POST':
        resultado = json.loads(request.data.decode('utf-8'))
        print(resultado)
        print('dados do POST')
        print('Nome:')
        print(resultado['nome'])
        print('Email:')
        print(resultado['email'])
        print('Telefone:')
        print(resultado['telefone'])
        # cadastra no db_teste com pymongo lib
        mongo = MongoClient()
        mongo = MongoClient('mongodb://127.0.0.1:27017')
        db_data01 = mongo['teste_db']
        newUser = mongo.db.db_data01
        newUser.insert({'nome': resultado['nome'], 'email': resultado['email'], 'telefone': resultado['telefone']})




if __name__ == '__main__':
    app.run(debug = True)

