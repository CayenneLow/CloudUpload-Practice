import os
from app import app
from app import app, db
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
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

# clears database and uploads folder
@app.route('/clear')
def clear():
    files = Files.query.order_by(Files.id.desc()).all()
    for file in files:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        db.session.delete(file)
    db.session.commit()

    return redirect(url_for('index'))

# reroutes downloads to download from uploads
@app.route('/download/<path:name>')
def download(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name, as_attachment=True)
