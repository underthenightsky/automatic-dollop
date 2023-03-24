from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/sign_up')
def products():
    return render_template('sign_up.html')
if __name__=="__main__":
    app.run(debug=True)
