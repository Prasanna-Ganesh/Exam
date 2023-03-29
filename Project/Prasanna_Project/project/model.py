from Prasanna_Project.project import  db
from marshmallow import Schema, fields


class InventorySchema(Schema):
    no = fields.Int()
    item = fields.Str()
    ordered = fields.Int()
    remaining = fields.Int()
    vendor = fields.Str()
    c_price = fields.Int()
    s_price = fields.Int()


class Inventory(db.Model):
    __tablename__ = 'inventory'
    no = db.Column(db.Integer, primary_key = True )
    item = db.Column(db.String)
    ordered = db.Column(db.Integer)
    remaining = db.Column(db.Integer)
    vendor = db.Column(db.String)
    c_price = db.Column(db.Integer)
    s_price = db.Column(db.Integer)


    def __init__(self, no, item, ordered, remaining, vendor, c_price, s_price):
        self.no = no
        self.item = item
        self.ordered = ordered
        self.remaining = remaining
        self.vendor = vendor
        self.c_price = c_price
        self.s_price = s_price


db.create_all()
