from flask import Flask,render_template,request
import requests
import datetime
import smtplib


# print(data)
day=datetime.datetime.now()  
thathi=day.strftime("%B %d, %Y")
response=requests.get("https://api.npoint.io/49e817800520d48406e9")
store=response.json()

app=Flask(__name__)
@app.route('/')
def get_all_posts():
    
    return render_template("index.html",datess=thathi,datass=store)



@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact',methods=['GET',"POST"])
def contacts():
    if request.method=="POST":
        my="lingadugmail.com"
        password=pass
        to_onwer_email="lingesh.91918@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as c:
            c.starttls()
            c.login(user=my,password=password)
            c.sendmail(from_addr=my,
            to_addrs=to_onwer_email,
            msg=f"Subject:Client's Message from Website\n\n{request.form['name']}\n{request.form['phone']}\n{request.form['email']}\n{request.form['message']}"
            )
            print("sent!!")
        return render_template("contact.html",msg_sent=True)
        #  f"<h1>{request.form['name']}{request.form['phone']}\n{request.form['email']}\n{request.form['message']}\n</h1>"

    return render_template("contact.html",msg_sent=False)


# @app.route('/form-entry',)
# def recive_data():
#     pass




@app.route('/posts/<int:bid>')
def postss(bid):
    return render_template('post.html',datass=store,b=bid,datess=thathi)



if __name__=='__main__':
    app.run(debug=True)