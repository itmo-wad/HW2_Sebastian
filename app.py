from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'Sebastian1235678'  # secretkey

# Configuration  MongoDB
app.config["MONGO_URI"] = "mongodb+srv://sebastianguevara11:sebastian123@cluster0.ap2mmu3.mongodb.net/miBaseDeDatos?retryWrites=true&w=majority&appName=Cluster0"
app.config["MONGO_OPTIONS"] = {"ssl": True}

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    error = None
    if 'username' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        users = mongo.db.users
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.find_one({'username': username})

        if user and user['password'] == password:  
            session['username'] = user['username']
            return redirect(url_for('profile'))
        else:
            
             error = 'Incorrect user or password'  # error message

    return render_template('login.html', error=error)

@app.route('/profile')
def profile():
    if 'username' in session:
        # dynamic parameters
        return render_template('index.html', 
                               name=session['username'], 
                               email="sebastianguevara11@gmail.com",  
                               date_current=datetime.utcnow())
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect(url_for('main'))

@app.route('/logout')
def logout():
    session.clear()  # This deletes all session information.
    return redirect(url_for('main'))  # Redirects the user to the home page (login).

if __name__ == '__main__':
    app.run(debug=True, port=5000)
