
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! you look sharp want some juice we can as well have some good time together",200

# if __name__ == "__main__":
#     app.run(debug=True)
#     @app.route("toysss")
#     def toy():
#         return "toy"
if __name__ == "__main__":
        app.run(debug=True,port=6700)