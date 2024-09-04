from flask import Flask
from scripts.init_state import init_state
from scripts.logs import split_records
from flask import render_template, request

db = init_state()

app = Flask(__name__)

@app.route("/sftp-1")
def get_sftp1():
    collection = db['sftp-1']
    documents = collection.find()
    table1, table2 = split_records(documents, 'sftp-2', 'sftp-3')
    return render_template('Report.html', name='sftp-1', sender1='sftp-2', sender2='sftp-3', table1=table1, size1=len(table1), table2=table2, size2=len(table2))

@app.route("/sftp-2")
def get_sftp2():
    collection = db['sftp-2']
    documents = collection.find()
    table1, table2 = split_records(documents, 'sftp-1', 'sftp-3')
    return render_template('Report.html', name='sftp-2', sender1='sftp-1', sender2='sftp-3', table1=table1, size1=len(table1), table2=table2, size2=len(table2))

@app.route("/sftp-3")
def get_sftp3():
    collection = db['sftp-3']
    documents = collection.find()
    table1, table2 = split_records(documents, 'sftp-1', 'sftp-2')
    return render_template('Report.html', name='sftp-3', sender1='sftp-1', sender2='sftp-2', table1=table1, size1=len(table1), table2=table2, size2=len(table2))