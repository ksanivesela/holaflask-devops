from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
    <head>
        <title>Mi Aplicación Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                text-align: center;
                padding-top: 80px;
            }
            .card {
                background: white;
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2563eb;
            }
            p {
                color: #555;
            }
            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask + Docker + GitHub Actions</h1>
            <p>Proyecto desplegado correctamente en Docker Swarm.</p>
            <p>Estudiante: Kevin Smith Nivesela Armijos</p>
            <p class="status">✅ Aplicación en funcionamiento</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)