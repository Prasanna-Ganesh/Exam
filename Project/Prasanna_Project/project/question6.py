from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rod'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
app.app_context().push()


class InventorySchema(Schema):
    no = fields.Int()
    item = fields.Str()


class Inventory(db.Model):
    __tablename__ = 'inven'
    no = db.Column(db.Integer, primary_key = True )
    item = db.Column(db.String)


def __init__(self, no, item):
    self.no = no
    self.item = item


db.create_all()

@app.route('/add', methods=['POST'])
def add():
    no = request.form['no']
    item = request.form['item']
    # ordered = request.form['ordered']
    # remaining = request.form['remaining']
    # vendor = request.form['vendor']
    # c_price = request.form['c_price']
    # s_price = request.form['s_price']
    inv = Inventory(no, item)
    db.session.add(inv)
    db.session.commit()
    return {"message": "Acc added"}


if __name__ == '__main__':
    app.run(debug=True)