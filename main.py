from flask import Flask, render_template
from threading import Thread

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  return render_template("index.html")

def run():
  app.run(host='0.0.0.0',port=3000)

t = Thread(target=run)
t.start()