from flask import Flask
from flask import request
from markupsafe import escape
from markupsafe import escape
from flask import abort, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
        return login_post()
   else:
       return login_get()


@app.get('/login')
def login_get():
   return render_template('login.html')

def login_post():
    grade = request.form['grade']
    error = "Недостаточно данных!"
    return render_template('profile.html', grade=grade, error=error)

def search(a, b):
    return



if __name__ == '__main__':
    app.run(port=5000)
    db = Database("localhost", "root", "admin", "school")