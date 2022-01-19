from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Secret"


@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/addtwo')
def add_two():
    session['counter'] += 1
    return redirect("/")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)