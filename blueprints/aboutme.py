from flask import Blueprint

app = Blueprint('aboutapp','aboutapp')

@app.route('/about')

def aboutme():
    return """Hi , I am Shrey"""