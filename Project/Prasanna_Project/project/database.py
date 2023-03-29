from Prasanna_Project.project.model import Inventory,InventorySchema
from Prasanna_Project.project import db
from flask import request,jsonify


def add():
    no = request.form['no']
    item = request.form['item']
    ordered = request.form['ordered']
    remaining = request.form['remaining']
    vendor = request.form['vendor']
    c_price = request.form['c_price']
    s_price = request.form['s_price']
    inv = Inventory(no, item, ordered, remaining, vendor, c_price, s_price)
    db.session.add(inv)
    db.session.commit()
    return {"message": "Acc added"}


def view():
    try:
        no = request.form['no']
        found = Inventory.query.filter_by(no=no).first()
        inv_schema = InventorySchema().dump(found)
        return inv_schema
    except:
        return jsonify({"Message":"No such ID Present"})


def viewall():
    all=Inventory.query.all()
    return all


def update():
    try:
        Inventory.query.filter(Inventory.no==request.form['no']),
        no=request.form['no']
        inv=Inventory.query.filter_by(no=no).first()
        inv.name=request.form['name']
        inv.ordered = request.form['ordered']
        inv.remaining = request.form['remaining']
        inv.vendor = request.form['vendor']
        inv.c_price = request.form['c_price']
        inv.s_price = request.form['s_price']
        db.session.commit()
    except:
        return jsonify({"Message":"No such ID to update"})


def delete():
    try:
        no = request.form['no']
        d = Inventory.query.filter_by(no=no).first()
        db.session.delete(d)
        db.session.commit()
    except:
        return jsonify({"Message":"No such ID to found"})

