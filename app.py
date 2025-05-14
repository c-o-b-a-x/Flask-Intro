"""what we have done so far

        Created Virtual Enviroment "python -m venv venv"
                - contains a copy of py and pip for just this project                 
        Activated the Virtual Enviroment with "./venv/Scripts/activate
                -
        Installed flask" pip install flask"
                -
        Created templates in a templates folder to return HTML pages
                
        Rendered Templates with render_template()
        
        Created Requirements.txt files that will let users easily install packages used 
                -create with : pip freeze > requirements.txt
                -can be ran with : pip install -r requirements.txt
        added a .gitignore to make sure we dont comit our venv 

        Created static folder to be used t o server other local resources
                -used url_for() to load static assets in HTML pages
"""

#import flask class from flask 
from flask import Flask,render_template,request
import datetime
import requests
app=Flask(__name__)

#define route for home page
@app.route("/")
def home():
        #return a simple string that is  valid HTML
        return render_template("home.html")
@app.route("/time")
def time():
        now= datetime.datetime.now()
        return render_template("time.html", current_time=now)
@app.route ("/form",methods=['GET','POST'])
def form():
        if request.method== 'POST':
                name=request.form.get('name')
                ssn=request.form.get('ssn')
                return render_template ("greeting.html",name=name,ssn=ssn)
        return render_template("form.html")



@app.route ("/math")
def math():
        return render_template ("math.html")

@app.route ("/math-results",methods=['GET','POST'])
def  solve():
        num1=request.form.get('num1')
        num2=request.form.get('num2')
        operation=request.form.get('operation')
        answer = eval(f"{int(num1)}{operation}{int(num2)}")
        return render_template ("math_results.html",answer=answer,num1=num1,num2=num2,operation=operation)

@app.route ("/cat-fact")
def catfact():
        response=requests.get("https://catfact.ninja/fact")
        if response.status_code== 200:
                data = response.json()
                fact=data["fact"]
        else:
                fact = "Sorry I couldnt get a cat fact right now please try again later "

        picsrep= requests.get("https://cataas.com/cat?json=true")
        if response.status_code== 200:
                picdata = picsrep.json()
                img=picdata["url"]
        else:
                img = "/image/404.png"
        return render_template("cat.html",cat_fact=fact,cat_img= img)



if __name__ == "__main__":
        app.run(debug=True)