from flask import Flask, request, jsonify


app=Flask(__name__)



database=[
    {
        "Empname":"kiran",
        "number":84989,
        "add":"vgr",
        "sex":"m"
    },
    {
        "Empname":"vsk",
        "number":81500,
        "add":"vgr",
        "sex":"m"
    }
]

@app.route('/Datastore/assignment',methods=['GET','POST'])
def Datastore():
    if request.method=='GET':
        if len(database)!=0:
            return  jsonify(database)
        if len(database)==0:
            return  'NO records',404
    if request.method=='POST':
        new_Empname=request.form['Empname']
        new_num=request.form['number']
        new_name=request.method['add']
        new_type=request.form['sex']
        new_obj={
                 "Empname":'new_Empname',
                 "num":'new_num',
                 "add":'new_name',
                 "sex":'new_type'
                }

        database.append(new_obj)
        return jsonify(database)




if __name__=='__main__':
    app.run()

@app('/Datastore/Assignment/<string:name>/',method=['GET','DELETE'])
def check(name):
    if request.method=='GET':
        for i in database:
            if i['Empname']==name:
                return jsonify(i)
    return 'No ',404
    if request.method=='DELETE':
        for i,x in enumerate(database):
            if x[Empname]=='name':
                database.pop(i)
                return jsonify(database)
