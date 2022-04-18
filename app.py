from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    return "<H1>Hello from Flask App running inside a Docker</H1>"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)