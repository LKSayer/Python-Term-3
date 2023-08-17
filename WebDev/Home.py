from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Homepage():
    return render_template("Home.html")  

@app.route("/Contact")
def Contactpage():
    return render_template("Contact.html")  

@app.route("/About")
def Aboutpage():
    return render_template("About.html")  

@app.route("/Shop")
def Shoppage():
    return render_template("Shop.html")  

if __name__ == '__main__':
    app.run()