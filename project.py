from flask import Flask, jsonify,request
app = Flask(__name__)
tasks = [
    {
        'id':1, 
        'contact':'0987654321',
        'name':'Harry Potter',
        'done':False
        
    },{
        'id':2, 
        'contact':'0987654312',
        'name':'Krish Patel',
        'done':False
    } 
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message":"Please Provide The Data"
        },400)
    task = {
        'id':tasks[-1]['id']+1, 
        'name':request.json['name'],
        'contact':request.json.get("contact",""),
        'done':False
    }    
    tasks.append(task)
    return jsonify({
        "Status":"Success",
        "Message":"Task Added Successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "Data":tasks
    })
if (__name__ == "__main__"):
    app.run(debug = True)