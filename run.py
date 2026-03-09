from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

TAXAS = {'cdb': 1.2, 'tesouro_direto': 0.9, 'acoes': 2.5}

@app.route('/')
def index():
    return render_template('index.html')

#==============================================
@app.route('/simulacao', methods=['GET', 'POST'])
def simulacao():
    taxa_juros = None
    tipo_investimento = None
    valor_inicial = None
    periodo = None
    resultado = None

    if request.method == 'POST':
        tipo_investimento = request.form.get('tipo_investimento')
        valor_inicial_raw = request.form.get('valor_inicial')
        periodo_raw = request.form.get('periodo')

        if tipo_investimento and valor_inicial_raw and periodo_raw:
            valor_inicial = float(valor_inicial_raw)
            periodo = int(periodo_raw)
            taxa_juros = TAXAS.get(tipo_investimento, 0)
        
        # Calcula o valor futuro
            valor_final = valor_inicial * ((1 + (taxa_juros / 100)) ** periodo)
            resultado = f"R$ {valor_final:,.2f}"

    return render_template('simulacao.html',
                           taxa_juros=taxa_juros,
                           tipo_investimento=tipo_investimento,
                           valor_inicial=valor_inicial,
                           periodo=periodo,
                           resultado=resultado)

#=====================================================
@app.route('/sobrenos')
def sobrenos():

    return render_template('sobrenos.html')

#============================================================
@app.route('/produtos')
def produto():

    return render_template('produtos.html')
#==================================================
@app.route('/conteudos')
def conteudo():

    return render_template('conteudos.html')
#================================================
@app.route('/tesouro')
def tesouro():

    return render_template('tesouro.html')
#==================================================
@app.route('/cdb')
def cdb():

    return render_template('cdb.html')
#======================================================
@app.route('/acoes')
def acoes():

    return render_template('acoes.html')
#======================================================
app.run(host= '0.0.0.0', port=5000, debug=True)