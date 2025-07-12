from flask import Flask
app = Flask(__name__)
@app.route("/LW")
def LW(): 
    print("this is LW")
@app.route("/college")
def git(): 
    return "hello"
    print("GLobal Institute of technology")

@app.route('/Home')
def Agra(): 
    print("TAJ MAHAL")

app.run()
