from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

# Define a function to run Flask on a specific port
def run(port):
    app.run(host='0.0.0.0', port=port, threaded=True)

# Function to keep the Flask app running on multiple ports
def keep_alive():
    ports = [8080, 1111, 8888]
    threads = []

    for port in ports:
        t = Thread(target=run, args=(port,))
        threads.append(t)
        t.start()

    # Optionally join threads to ensure they all complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    keep_alive()
