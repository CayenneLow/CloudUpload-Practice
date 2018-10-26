import os
from app import app
from app import app, db
from flask import Flask, render_template, redirect, request, url_for
from models import Files

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    files = Files.query.order_by(Files.id.desc()).all()
    for file in files:
        print(file.filename)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST','GET'])
def upload():
    file = request.files['inputFile']
    # saving it in uploads folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    # saving it in database
    newFile = Files(filename=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    files = Files.query.order_by(Files.id.desc()).all()
    for file in files:
        db.session.delete(file)
    db.session.commit()

    return redirect(url_for('index'))

