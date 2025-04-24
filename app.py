from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify({"mensagem": "API rodando com Docker!"})

@app.route("/soma", methods=["GET"])
def somar():
	a = int(request.args.get("a", 0))
	b = int(request.args.get("b", 0))
	return jsonify({"resultado": a + b})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
