from flask import Flask, jsonify, render_template_string, request, redirect
import sqlite3
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

# Função para consultar o banco de dados
def get_ocorrencias():
    conn = sqlite3.connect('ocorrencias.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, latitude, longitude, origem FROM ocorrencias")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "latitude": r[2], "longitude": r[3], "origem": r[4]} for r in rows]

# Página inicial
@app.route('/')
def home():
    return "🦂 API de Ocorrências de Escorpiões"

# Rota para retornar dados em JSON
@app.route('/ocorrencias')
def ocorrencias():
    return jsonify(get_ocorrencias())

# Mapa de calor com todos os pontos
@app.route('/mapa')
def mapa():
    dados = get_ocorrencias()

    if not dados:
        return "Sem dados para exibir."

    lat_media = sum(d['latitude'] for d in dados) / len(dados)
    lon_media = sum(d['longitude'] for d in dados) / len(dados)

    mapa = folium.Map(location=[lat_media, lon_media], zoom_start=13)
    pontos = [[d['latitude'], d['longitude']] for d in dados]
    HeatMap(pontos).add_to(mapa)

    html = mapa._repr_html_()

    return render_template_string("""
    <html>
    <head><title>Mapa de Ocorrências 🦂</title></head>
    <body style="font-family:Arial; text-align:center;">
        <h2>Mapa de Calor das Ocorrências de Escorpiões</h2>
        <p><a href="/adicionar">➕ Adicionar nova ocorrência</a></p>
        {{ html|safe }}
    </body>
    </html>
    """, html=html)

# Formulário para nova ocorrência
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_ocorrencia():
    if request.method == 'POST':
        nome = request.form.get('nome')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        origem = request.form.get('origem')

        if nome and latitude and longitude and origem:
            conn = sqlite3.connect('ocorrencias.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ocorrencias (nome, latitude, longitude, origem)
                VALUES (?, ?, ?, ?)
            ''', (nome, float(latitude), float(longitude), origem))
            conn.commit()
            conn.close()
            return redirect('/mapa')
        else:
            return "⚠️ Todos os campos são obrigatórios."

    return render_template_string("""
    <html>
    <head><title>Adicionar Ocorrência</title></head>
    <body style="font-family:Arial; padding:20px;">
        <h2>📌 Inserir Nova Ocorrência</h2>
        <form method="POST">
            <label>Nome:</label><br>
            <input type="text" name="nome" required><br><br>

            <label>Latitude:</label><br>
            <input type="number" step="any" name="latitude" required><br><br>

            <label>Longitude:</label><br>
            <input type="number" step="any" name="longitude" required><br><br>

            <label>Origem:</label><br>
            <select name="origem" required>
                <option value="">-- selecione --</option>
                <option value="SINAN">SINAN</option>
                <option value="Armadilha">Armadilha</option>
                <option value="Cidadão">Cidadão</option>
                <option value="Outra">Outra</option>
            </select><br><br>

            <input type="submit" value="Adicionar">
        </form>
        <br>
        <a href="/mapa">← Voltar ao mapa</a>
    </body>
    </html>
    """)

# 👇 ESSENCIAL para funcionar no Render

from flask import send_file

@app.route('/home')
def homepage():
    return send_file('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
    
