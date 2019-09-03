from flask import Flask, render_template, request
from validate_email import validate_email
from sqlalchemy.orm import sessionmaker
from .models import *
from .views import *
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('postgres+psycopg2://root:admin@postgres:5432/flask')
Session = sessionmaker(bind=engine)
s = Session()
Base.metadata.create_all(engine)



@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        if (validate_email(email)):
            if (s.query(User).filter(User.email == email).first() == None):
                newUser= User(email=email)
                s.add(newUser)
                s.commit()
                return render_template("newsletterThanks.html")
            return "ya tienes una cuenta"
        return render_template("newsletterHome.html")
    return render_template("newsletterHome.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
