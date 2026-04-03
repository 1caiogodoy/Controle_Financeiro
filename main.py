from flask import Flask, request, render_template
import matplotlib.pyplot as plt


app = Flask(__name__)

def grafico(renda, gastos, investimento, lazer, dividas, sobra):
    """Função para gerar o gráfico de controle financeiro atual"""
    labels = ['Gastos', 'Investimento', 'Lazer', 'Divídas', 'Sobras']

    valores = [gastos, investimento, lazer, dividas, sobra]

    plt.figure(figsize=(8,8))
    plt.pie(valores, labels=labels, autopct='%1.1f%%')

    plt.savefig("static/grafico.png", bbox_inches='tight')
    plt.close()


def grafico2(gastos, investimento, lazer, dividas, sobra):

    gastos2 = gastos + dividas
    investimento2 = investimento + sobra/2
    lazer2 = lazer + sobra/2

    labels = ['Gastos + Divídas', 'Investimento', 'Lazer']
    valores = [gastos2, investimento2, lazer2]

    plt.figure(figsize=(8,8))
    plt.pie(valores, labels=labels, autopct='%1.1f%%')

    plt.savefig("static/grafico2.png", bbox_inches='tight')
    plt.close()

def calcular_sobra(renda, gastos, investimento, lazer, dividas):
    return renda - (gastos + investimento + lazer + dividas)

@app.route('/')
def formulario():
    return render_template("formulario.html")

@app.route('/resultado.html', methods=['POST'])
def resultado():
    """Função para colocar os valores dos inputs dentro das variaveis da função grafico"""
    try:
        renda = float(request.form['renda'])
        gastos = float(request.form['gastos'])
        investimento = float(request.form['investimento'])
        lazer = float(request.form['lazer'])
        dividas = float(request.form['dividas'])

        grafico(renda, gastos, investimento, lazer, dividas, sobra=calcular_sobra())
        grafico2(gastos, investimento, lazer, dividas, sobra=calcular_sobra())
        
        sobra = renda - (gastos + investimento + lazer + dividas)
        if sobra < 0:
            return render_template("/resultado.html", erro="Seus gastos ultrapassam sua renda")
        
        return render_template("/resultado.html", grafico=True, grafico2=True)
    except Exception:
        return render_template("/resultado.html", grafico=False, grafico2=False, erro="Seus gastos ultrapassam sua renda. Revise seus valores")

if __name__ == "__main__":
    app.run(debug=True)