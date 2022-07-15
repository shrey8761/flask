import flask 
import os 

app = flask.Flask(__name__) #flask object named as app
@app.route('/')
def function():
    # return ("Hello World")
    dirlist = os.listdir()
    return (f"<h1> shrey1 </h1> <br> {dirlist.__str__()} </br> ")

app.run() # usitng its property/method
