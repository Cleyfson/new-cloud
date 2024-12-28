from flask import Flask, request, jsonify
import pickle
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

MODEL_PATH = "/data/recommendation_rules.pkl"
MODEL_DATE = None

def load_model(model_path):
    if not os.path.exists(model_path):
        logging.error(f"Arquivo de modelo {model_path} não encontrado.")
        raise FileNotFoundError(f"Arquivo de modelo {model_path} não encontrado.")
    
    global MODEL_DATE
    MODEL_DATE = datetime.fromtimestamp(os.path.getmtime(model_path)).strftime("%Y-%m-%d %H:%M:%S")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        print(model)
    
    logging.info(f"Modelo carregado do arquivo {model_path}. Última atualização: {MODEL_DATE}")
    return model

def recommend_playlists(user_songs, rules, top_n=3, max_rules=1000):
    recommendations = []

    for i, rule in enumerate(rules):
        if i >= max_rules:
            break
        antecedent = set(rule['antecedent'])
        consequent = set(rule['consequent'])

        if antecedent.issubset(user_songs):
            recommendations.append((consequent, rule['confidence']))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve ser JSON"}), 400

        data = request.get_json()
        user_songs = set(data.get("songs", []))

        if not user_songs:
            return jsonify({"error": "A lista de músicas não pode estar vazia"}), 400

        recommendations = recommend_playlists(user_songs, app.model, top_n=5)

        recommended_songs = [list(rec[0]) for rec in recommendations]
        response = {
            "songs": recommended_songs,
            "version": app.version,
            "model_date": MODEL_DATE
        }
        return jsonify(response), 200
    except Exception as e:
        logging.error(f"Erro no endpoint /api/recommend: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.model = load_model(MODEL_PATH)
    app.version = "1.0.0"
    
    PORT = 30502
    app.run(host="0.0.0.0", port=PORT)
