from flask import render_template
from Prasanna_Project.project import app
from Prasanna_Project.project.database import add,update,view,viewall

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewall/',methods=['GET'])
def Viewall():
    all= viewall()
    return render_template('viewall.html',all=all)


@app.route('/add/', methods=['POST'])
def Add():
    result = add()
    return result


@app.route('/view/', methods=['GET'])
def View():
    result = view()
    return result


@app.route('/update/',methods=['PUT'])
def Update():
    result = update()
    return result

@app.route('/delete/',methods=['DELETE'])
def Delete():
    result = Delete()
    return result

if __name__=='__main__':
    app.run(debug=True)