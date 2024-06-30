from flask import Flask, render_template, url_for, request, redirect
import os
from smtplib import SMTP_SSL as SMTP

MY_EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with SMTP("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: New Message from portfolio website \n\nName: {name}\nEmail: {email}\nMessage: {message}"
            )
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=False)