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
if __name__ == "__main__":
        app.run(debug=True)