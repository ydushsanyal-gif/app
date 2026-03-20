from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return "welcome to about page"  
@app.route('/dashboard') 
def dashboard():
    return "Represents your dashboard"
@app.route('/services')
def services():
    return " Offers code flexibility"
@app.route("/contact")
def contact ():
    return " contact number - 1234567890"










if __name__ == '__main__':
    app.run(debug=True)