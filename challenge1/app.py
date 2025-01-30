from flask import Flask
import socket
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():

    my_name = "Marwen"
    project_name = "My Awesome Project"
    version = "V3"
    hostname = request.host_url
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <html>
      <head><title>{project_name}</title></head>
      <body>
        <h1>Hello, welcome to {project_name}!</h1>
        <p><strong>Name:</strong> {my_name}</p>
        <p><strong>Project Name:</strong> {project_name}</p>
        <p><strong>Version:</strong> {version}</p>
        <p><strong>Hostname:</strong> {hostname}</p>
        <p><strong>Current Date:</strong> {current_date}</p>
      </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

