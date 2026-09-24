import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Aplicacion funcionando"


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


def main():
    secret = os.getenv("DEMO_SECRET")

    if not secret:
        raise RuntimeError("DEMO_SECRET no existe")

    print("Secret cargado correctamente")

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False,
        use_reloader=False
    )


if __name__ == "__main__":
    main()
