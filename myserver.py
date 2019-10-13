from flask import Flask, request, redirect, url_for,jsonify

app=Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hi"

@app.route('/rpta', methods=['POST'])
def rec():
    data=request.data
    print(data)
    return "hello my baby"



if __name__=='__main__':
    app.run()