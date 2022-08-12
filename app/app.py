from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean,DateTime
import datetime
import os
from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_cors import CORS, cross_origin
from mysql.connector import connect, Error
import yaml
from yaml.loader import SafeLoader


app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

meta_data ={}

if os.path.exists('/env/.env'):
    print("loaded data")
    with open('/env/.env') as f:
        meta_data = yaml.load(f, Loader=SafeLoader)
    meta_data["db_username"] = os.environ.get("DB_ROOT_USERNAME")
    meta_data["db_password"] = os.environ.get("DB_ROOT_PASSWORD")
    print(meta_data)
else:
    print("not loaded")
    meta_data = {
        "host": "0.0.0.0",
        "port": "8080",
        "expiration_duration": 0.5,
        "db_hostname": 'db',
        "db_username": "root",
        "db_password": "root",
    }



SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}:3306/{databasename}".format(
    username=meta_data["db_username"],
    password=meta_data["db_password"],
    hostname=meta_data["db_hostname"],
    databasename="secretnotes",
)
print(SQLALCHEMY_DATABASE_URI)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(app)
ma = Marshmallow(app)



@app.route("/")
def home_page():
    return render_template('index.html',server_address="{}:{}".format(meta_data['host'], meta_data["port"]))


@app.route("/addnote/", methods=['POST', 'GET'],)
def add_note():
    note_content = request.form['text']
    # print(note_content)
    new_comment = Note(content=note_content, creation_time=datetime.datetime.now(), expiration_time=datetime.datetime.now() + datetime.timedelta(minutes=meta_data['expiration_duration']) )
    db.session.add(new_comment)
    db.session.commit()
    note_url = "http://" + meta_data['host'] + ":" + meta_data["port"]+"/getnote/"+str(new_comment.id)
    # print(new_comment.content,"  ", new_comment.id)
    return render_template('link.html', note_url=note_url, server_address="{}:{}".format(meta_data['host'], meta_data["port"]))


@app.route("/getnote/<int:note_id>", methods=['POST', 'GET'],)
def get_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.expiration_time < datetime.datetime.now():
        db.session.delete(note)
        db.session.commit()
        return render_template('expired.html', note_id=note_id, server_address="{}:{}".format(meta_data['host'], meta_data["port"]))

    return render_template('read_destroy.html', note_id=note_id, server_address="{}:{}".format(meta_data['host'], meta_data["port"]))



@app.route("/deletenote/<int:note_id>", methods=['POST', 'GET'], )
def delete_note(note_id):
    content =""
    try:
        note = Note.query.filter_by(id=note_id).first()
        content = note.content
        db.session.delete(note)
        db.session.commit()
    except:
        pass
    try:
        note = Note.query.filter_by(id=note_id).first()
        print(note.id)
    except:
        print("note is deleted")
    return render_template('show_notes.html', note_content=content, server_address="{}:{}".format(meta_data['host'], meta_data["port"]))



# data base cli commands >>>>>>>>>>>>>>>>>>>>>>
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
    m1 = Note(
        content="seed note!"
     )

    db.session.add(m1)
    db.session.commit()
    print('DB seeded')


# data base models >>>>>>>>>>>>>>>>>>>>>>
class Note(db.Model):
    __tablename__ = 'notes'
    id = Column(db.Integer, primary_key=True)
    content = Column(db.String(1000))
    creation_time = Column(DateTime) 
    expiration_time = Column(DateTime) 

# marshmallow >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content',)


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

if __name__ == '__main__':
    app.run(host = meta_data["host"], port = meta_data["port"])
