from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

#when user logs in. If specific admin login, will take to feedback page.
#otherwise, will take to basket or similar.
#will probably implement basic hash function to hide username and password
#obviously not secure, still better than 0.
@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        if (request.form.getlist('username')[0]=="pjohn") and ((request.form.getlist('password')[0]) == "pizzapie"):
            return render_template('feedback.txt')
        #any username will work, so long as password == username123
        #have welcome message saying, welcome "username".
        elif request.form.getlist('password')[0]==request.form.getlist('username')[0]+"123":
            return("Welcome back",request.form.getlist('username')[0])
        else:
            return("Error. Username or password is incorrect")

#Simply sends feedback, without too much extra.
#will simply write text to file.
@app.route('/submitfeedback')
def send_feedback():
    pass



app.run(host='0.0.0.0',port=81)
