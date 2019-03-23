from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import smtplib
from flask_mail import Mail,Message
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
app.config["SECRET_KEY"]="difhosuh09wre8rfeifr"

db=SQLAlchemy(app)
admin=Admin(app)

app.config.update(
DEBUG=True,
MAIL_SERVER="mail.ajairahouse.com",
MAIL_PORT=465,
MAIL_USE_SSL=True,
MAIL_USERNAME="rahi@ajairahouse.com",
MAIL_PASSWORD="ajairarahiriya"
)

mail=Mail(app)
class Team(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    institute=db.Column(db.String(50),nullable=False)
    study=db.Column(db.String(50),nullable=False)
    birth=db.Column(db.String(20),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    phone=db.Column(db.Integer(),nullable=False)
    email=db.Column(db.String(120),nullable=False)
    skills=db.Column(db.String(120),nullable=False)
    technology=db.Column(db.String(200),nullable=False)
    experience=db.Column(db.String(200),nullable=False)
    why_work=db.Column(db.Text(),nullable=False)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form.get('fullname')
        email=request.form.get('email')
        message=request.form.get('message')
        try:
            msg=Message("Team|IceCream Contact Us Email",
            sender='rahi@ajairahouse.com',
            recipients=["zanjarwhite@gmail.com"])
            msg.body=("Name: "+name+"\nEmail: "+email+"\nMessage: "+message)
            mail.send(msg)
            flash("Thanks for Contact with Team | IceCream")
        except:
            pass

    return render_template('home.html')

@app.route('/join_team_icecream',methods=["GET","POST"])
def join_us():
    if request.method=="POST":
        name=request.form.get('name')
        institute=request.form.get('institute')
        study=request.form.get('study')
        birth=request.form.get('birth')
        gender=request.form.get('gender')
        email=request.form.get('email')
        phone=request.form.get('phone_number')
        skills=request.form.get('skills')
        technology=request.form.get('interest')
        experience=request.form.get('experience')
        why_work=request.form.get('why_work')
        join_request=Team(name=name,institute=institute,study=study,birth=birth,
        gender=gender,email=email,phone=phone,skills=skills,technology=technology,experience=experience,why_work=why_work)

        db.session.add(join_request)
        db.session.commit()
        flash("Your Join Request has been success,Team | IceCream will contact with you in Your Email.")
        return redirect(url_for('home'))


    return render_template('join_us.html')



admin.add_view(ModelView(Team,db.session, url='/@@@@@@@@@@@'))


if __name__=="__main__":
    app.run(debug=True)
