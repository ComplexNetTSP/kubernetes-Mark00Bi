from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h2>Flask No DB - app1 </h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

