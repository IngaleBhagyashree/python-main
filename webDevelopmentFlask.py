from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    print("hello from flask")