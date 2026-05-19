from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# =====================================
# DADOS MOCKADOS
# =====================================

clientes = [
    {
        'id': 1,
        'nome': 'Construtora Alpha',
        'telefone': '(47) 99999-9999'
    },
    {
        'id': 2,
        'nome': 'Terraplanagem Beta',
        'telefone': '(47) 98888-8888'
    }
]

maquinas = [
    {
        'id': 1,
        'nome': 'Escavadeira Hidráulica',
        'status': 'Alugada'
    },
    {
        'id': 2,
        'nome': 'Retroescavadeira',
        'status': 'Disponível'
    },
    {
        'id': 3,
        'nome': 'Mini Carregadeira',
        'status': 'Disponível'
    }
]

alugueis = [
    {
        'cliente': 'Construtora Alpha',
        'maquina': 'Escavadeira Hidráulica',
        'data_inicio': '01/02/2026',
        'data_fim': '10/02/2026',
        'status_pagamento': 'Pago'
    },
    {
        'cliente': 'Terraplanagem Beta',
        'maquina': 'Mini Carregadeira',
        'data_inicio': '05/02/2026',
        'data_fim': '15/02/2026',
        'status_pagamento': 'Pendente'
    }
]

# =====================================
# ROTAS
# =====================================

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():

    return render_template(
        'cadastro.html',
        active_page='cadastro'
    )

@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        alugueis=alugueis
    )


@app.route('/maquinas-alugadas')
def maquinas_alugadas():
    return render_template(
        'maquinas_alugadas.html',
        alugueis=alugueis
    )


@app.route('/maquinas-estoque')
def maquinas_estoque():
    return render_template(
        'maquinas_estoque.html',
        maquinas=maquinas
    )


@app.route('/cadastro-maquinas', methods=['GET', 'POST'])
def cadastro_maquinas():

    if request.method == 'POST':

        nova_maquina = {
            'id': len(maquinas) + 1,
            'nome': request.form['nome'],
            'status': 'Disponível'
        }

        maquinas.append(nova_maquina)

        return redirect(url_for('cadastro_maquinas'))

    return render_template(
        'cadastro_maquinas.html',
        maquinas=maquinas
    )


@app.route('/cadastro-clientes', methods=['GET', 'POST'])
def cadastro_clientes():

    if request.method == 'POST':

        novo_cliente = {
            'id': len(clientes) + 1,
            'nome': request.form['nome'],
            'telefone': request.form['telefone']
        }

        clientes.append(novo_cliente)

        return redirect(url_for('cadastro_clientes'))

    return render_template(
        'cadastro_clientes.html',
        clientes=clientes
    )


@app.route('/novo-aluguel', methods=['GET', 'POST'])
def novo_aluguel():

    if request.method == 'POST':

        aluguel = {
            'cliente': request.form['cliente'],
            'maquina': request.form['maquina'],
            'data_inicio': request.form['data_inicio'],
            'data_fim': request.form['data_fim'],
            'status_pagamento': request.form['status_pagamento']
        }

        alugueis.append(aluguel)

        for maquina in maquinas:
            if maquina['nome'] == request.form['maquina']:
                maquina['status'] = 'Alugada'

        return redirect(url_for('maquinas_alugadas'))

    maquinas_disponiveis = [
        maquina for maquina in maquinas
        if maquina['status'] == 'Disponível'
    ]

    return render_template(
        'aluguel.html',
        clientes=clientes,
        maquinas=maquinas_disponiveis
    )


if __name__ == '__main__':
    app.run(debug=True)