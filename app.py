from flask import Flask, redirect, url_for, request,render_template,send_file
from testscript import test_view
import shutil
import sys
from os import path,makedirs
from datetime import datetime
from shutil import rmtree
import socket

app = Flask(__name__)
basis = sys.executable
required_folder = path.split(basis)[0]
now = datetime.now()
date_string = now.strftime("%d-%m-%Y_%Hh%M")

@app.route('/success/<name>', methods=['GET','POST'])
def success(name):
    return render_template(['index.html','style.css'],name=name)

@app.route('/failed')
def failed():
    return render_template(['failed.html','style.css'])

@app.route('/continu/<name>', methods=['GET','POST'])
def continu(name):
    liste = name.replace("'","").replace("[","").replace("]","").split(",")
    distrib = liste[0]
    project = liste[1]
    number_tickets = liste[2]
    range_high = liste[3]
    range_low = liste[4]
    font_path = 'static/font/Arial Black.ttf'
    resp = test_view(distrib,project,number_tickets,range_high,range_low,font_path)
    if not path.exists(required_folder+"/test"):
        makedirs(required_folder+"/test/")
    for element in resp:
        element[0].save(required_folder+"/test/"+element[1]+".png")

    shutil.make_archive(required_folder+"/test_"+date_string, 'zip', required_folder+"/test/")
    rmtree(required_folder+"/test")
    return render_template(['empty.html','style.css'])

@app.route("/download")
def download():
    return send_file(
        required_folder+"/test_"+date_string+".zip",
        mimetype='application/zip',
        download_name="test_"+date_string+".zip",
        as_attachment=True
    )

@app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        return redirect(url_for('success', name=[request.form['env'],request.form['pk'],request.form['nt'],request.form['ht'],request.form['lt']]))
    else:
        return redirect(url_for('failed', name=""))

@app.route('/')
def home():
    return render_template(['config.html','style.css'])


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)