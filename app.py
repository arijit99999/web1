from flask import Flask,request,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def home_page():
    return render_template("web.html")




if __name__=="__main__":
 app.run(host='0.0.0.0',port=8080)