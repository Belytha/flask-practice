from flask import Flask, request
app = Flask(__name__)

"""Basic math operations."""
@app.route("/add")
def add():
    """Add a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a + b)

@app.route("/sub")
def sub():
    """Subtract a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a - b)

@app.route("/mult")
def mult():
    """Multiply a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a * b)

@app.route("/div")
def div():
    """Divide a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a / b)
