from flask import Flask
app = Flask(__name__)
@app.route("/LW")
def LW(): 
    return "This is returns LW"
    print("this is LW")
@app.route("/college")
def git(): 
    return "This returns git"
    print("GLobal Institute of technology")

@app.route('/Home')
def Agra(): 
    print("TAJ MAHAL")
    return "Agra is part of Uttar Pradesh"

app.run()
