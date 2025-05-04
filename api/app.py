from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/mensagem', methods=['GET'])
def get_mensagem():
    return jsonify({"mensagem": "Olá, mundo!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
