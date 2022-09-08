from flask import Flask, request, render_template
from enviandoParaBanco import EnviandoParaBanco

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/enviando-dados', methods=['POST']) 
def enviando_dados():
    request_data = request.get_json()
    return EnviandoParaBanco.dados(request_data)

if __name__ == '__main__':
    app.run(debug = True)
