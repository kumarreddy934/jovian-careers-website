from flask import  Flask

app=Flask(__name__)

@app.route("/")
def home_msg():
  return "<h1>hello</h1>"

print(__name__,"hello")
if __name__=="__main__":
   app.run(host='0.0.0.0',debug=True)