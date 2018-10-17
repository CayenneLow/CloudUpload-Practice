from app import app
from app import app, db
from flask import Flask, render_template, redirect, request
from models import Files

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    file = request.files['inputFile']
    newFile = Files(filename=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()

    return "Nice, uploaded " + file.filename + "."
