from flask import Flask, render_template,request, flash
from model import InputForm
from compute import visualize_series
from flask_mail import Message, Mail
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Formulary', methods=['GET', 'POST'])
def formulary():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = visualize_series(Q1=form.Q1.data,Q2=form.Q2.data,Q3=form.Q3.data,
                                  Q4=form.Q4.data,Q5=form.Q5.data,Q6=form.Q6.data,
                                  Q7=form.Q7.data,Q8=form.Q8.data,Q9=form.Q9.data,
                                  Q10=form.Q10.data)
        return render_template("sumaries.html", form=form, result=result)
    else:
        result = None
        textInfo = None
    print(request.method, [field.errors for field in form])
    return render_template("formulary.html", form=form, result=result,textInfo = textInfo)


@app.route('/Feedback', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        mail_settings = {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 465,
            "MAIL_USE_TLS": False,
            "MAIL_USE_SSL": True,
            "MAIL_USERNAME": 'trainsnatset@gmail.com',
            "MAIL_PASSWORD": 'trains2020'
            #"MAIL_PASSWORD": os.environ['MAIL_PASSWORD']

        }

        app.config.update(mail_settings)
        mail = Mail(app)

        body = "From " + request.form.get('name') + "\n" \
               + request.form.get('email') + "\n\n" \
               + request.form.get('message')

        msg = Message(subject="Feedback from TRAINS form",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=app.config.get("MAIL_USERNAME").split(),  # replace with your email for testing
                      body=body)
        mail.send(msg)

        return render_template('thanks.html')

    return render_template('comments.html')

if __name__ == '__main__':
    app.run(debug=True)