# pip install requests
# pip install bs4
# pip install html5lib

import requests
from flask import Flask,request,jsonify,session,redirect,url_for,render_template

app=Flask(__name__)
app.config["DEBUG"] = True

url = "https://api.covid19india.org/data.json"



@app.route("/")
@app.route("/home")
def home():
	r = requests.get(url).json()	
	return render_template("home.html", val = r)

if __name__ == "__main__":
	app.run()
#step 1: Get the HTML

