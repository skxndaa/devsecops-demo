from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """A simple endpoint that returns a greeting."""
    return "Hello, DevSecOps!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
    ### hello 