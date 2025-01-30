from flask import Flask, request
import socket
from datetime import datetime
from pymongo import MongoClient
import os

app = Flask(__name__)


MONGO_HOST = os.environ.get("MONGO_HOST", "mongodb")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
MONGO_DB   = os.environ.get("MONGO_DB", "mydatabase")
MONGO_USER = os.environ.get("MONGO_USER", "root")
MONGO_PASS = os.environ.get("MONGO_PASS", "example")

@app.route("/")
def index():

    my_name       = "Marwen"
    project_name  = "My Awesome Project"
    version       = "V2"
    hostname      = request.host_url
    current_date  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Connect to MongoDB on each request
    client = MongoClient(
        host=MONGO_HOST,
        port=MONGO_PORT,
        username=MONGO_USER,
        password=MONGO_PASS
    )
    db = client[MONGO_DB]
    collection = db["requests"]

    # Insert the client's IP address and current date
    client_ip = request.remote_addr  # IP of the user making the request
    record = {
        "ip": client_ip,
        "date": datetime.now()
    }
    collection.insert_one(record)

    # Retrieve the last 10 records (sorted by date descending)
    last_10 = collection.find().sort("date", -1).limit(10)

    # Build an HTML table of last 10 records
    history_html = "<table border=1><tr><th>IP</th><th>Date</th></tr>"
    for doc in last_10:
        history_html += f"<tr><td>{doc['ip']}</td><td>{doc['date']}</td></tr>"
    history_html += "</table>"

    # Create the main HTML content
    html_content = f"""
    <html>
      <head><title>{project_name} - {version}</title></head>
      <body>
        <h1>Welcome to {project_name}!</h1>
        <p><strong>Name:</strong> {my_name}</p>
        <p><strong>Project Name:</strong> {project_name}</p>
        <p><strong>Version:</strong> {version}</p>
        <p><strong>Hostname:</strong> {hostname}</p>
        <p><strong>Current Date:</strong> {current_date}</p>
        <hr/>
        <h2>Last 10 Access Records</h2>
        {history_html}
      </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
