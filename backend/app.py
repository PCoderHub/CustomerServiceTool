from flask import Flask, render_template, request, jsonify
#from flask_pymongo import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from userSave import UserSave
from queryprio import QueryPrio
from complaintprio import ComplaintPrio
from priority import Priority
from concernMaker import ConcernMaker
from query import Query
from complaint import Complaint

app = Flask(__name__)

client = MongoClient("mongodb+srv://pooja16:UmuQgKkkuxIaA17Y@cluster0.l2y4xgm.mongodb.net")
db = client["customer-service-mgmt-sys"]

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #register endpoint
    body = request.json
    user = UserSave()                          #Factory pattern applied here

    if db['users'].find_one({'userName': body['userName']}):
        return jsonify({'error': 'Username already exists'}), 400
    
    if body['userType'] == 'agent':                               #to register 'agent' user
        agent = user.user_save(body)

        result = db['users'].insert_one({
        "userName": agent.get_username(),
        "password": agent.get_password(),
        "userType": agent.get_usertype(),
        "department": agent.get_department()
        })
        return jsonify({
            'id': str(result.inserted_id),
            'userName': agent.get_username(),
            'password': agent.get_password()
        })

    elif body['userType'] == 'customer':                         # to register 'customer'user
        customer = user.user_save(body)
        
        result = db['users'].insert_one({
        "userName": customer.get_username(),
        "password": customer.get_password(),
        "userType": customer.get_usertype(),
        "serviceType": customer.get_servicetype()
        })
        return jsonify({
            'id': str(result.inserted_id),
            'userName': customer.get_username(),
            'password': customer.get_password()
        })

@app.route('/login', methods = ['POST'])
def login():
    #login endpoint
    body = request.json

    user = db['users'].find_one({'userName': body['userName'], 'password': body['password']})

    if user:
        return jsonify({
            'id': str(user['_id']),
            'userName': user['userName'],
            'password': user['password'],
            'userType': user['userType']
        })
    else:
        return jsonify({'error': 'Invalid credentials'}), 400
    
@app.route('/register/<string:usertype>', methods = ['GET'])
def agentnames(usertype):
    #register/<userType> endpoint to fetch a particular usertype
    agents = db['users'].find({'userType': usertype})
    agentJson = []

    for data in agents:
        id = data['_id']
        userName = data['userName']

        agentDict = {
            "id": str(id),
            "userName": userName
        }
        agentJson.append(agentDict)
    return jsonify(agentJson)

    
@app.route('/concerns', methods = ['POST', 'GET'])
def tickets():
    # to save raised tickets
    if request.method == 'POST':
        body = request.json
        concern = ConcernMaker()           #facade pattern applied here

        if body['concernType'] == "query":
            query = Query()
            query.set_username(body['userName'])
            query.set_email(body['email'])
            query.set_agent(body['agent'])
            query.set_subject(body['subject'])
            query.set_description(body['description'])

            concerntype = concern.make_query()

            prio = QueryPrio()
            priority = Priority(prio)              #strategy pattern applied here
            pri = priority.set_priority()

            result = db['concerns'].insert_one({
            "userName": query.get_username(),
            "email": query.get_email(),
            "agent": query.get_agent(),
            "concern": body['concernType'],
            "concernType": concerntype,
            "priority": pri,
            "subject": query.get_subject(),
            "description": query.get_description()
        })

            return jsonify({
            'id': str(result.inserted_id),
            'userName': query.get_username(),
            'email': query.get_email(),
            'agent': query.get_agent(),
            'concern': body['concernType'],
            'concernType': concerntype,
            'priority': pri,
            'subject': query.get_subject(),
            'description': query.get_description()
        })    

        else: 
            complaint = Complaint()
            complaint.set_username(body['userName'])
            complaint.set_email(body['email'])
            complaint.set_agent(body['agent'])
            complaint.set_subject(body['subject'])

            concerntype = concern.make_complaint()

            prio = ComplaintPrio()
            priority = Priority(prio)                   #strategy pattern applied here
            pri = priority.set_priority()

            result = db['concerns'].insert_one({
            "userName": complaint.get_username(),
            "email": complaint.get_email(),
            "agent": complaint.get_agent(),
            "concern": body['concernType'],
            "concernType": concerntype,
            "priority": pri,
            "subject": complaint.get_subject()
        })
            
            return jsonify({
            'id': str(result.inserted_id),
            'userName': complaint.get_username(),
            'email': complaint.get_email(),
            'agent': complaint.get_agent(),
            'concern': body['concernType'],
            'concerntype': concerntype,
            'priority': pri,
            'subject': complaint.get_subject()
        })

    # to get tickets raised by a particular user
    if request.method == 'GET':
        username = request.args.get('userName')

        if username:
            myConcerns = db['concerns'].find({'userName': username})
            myconcernJson = []

            for data in myConcerns:
                id = data['_id']
                userName = data['userName']
                email = data['email']
                agent = data['agent']
                concern = data['concern']
                concerntype = data['concernType']
                pri = data['priority']
                subject = data['subject']

                if concern == 'query':
                    description = data['description']
                    concernDict = {
                    "id": str(id),
                    "userName": userName,
                    "email": email,
                    "agent": agent,
                    "concern": concern,
                    "concernType": concerntype,
                    "priority": pri,
                    "subject": subject,
                    "description": description,
                    }
                else:
                    concernDict = {
                    "id": str(id),
                    "userName": userName,
                    "email": email,
                    "agent": agent,
                    "concern": concern,
                    "concernType": concerntype,
                    "priority": pri,
                    "subject": subject
                }
                myconcernJson.append(concernDict)
            return jsonify(myconcernJson)

        else:
            allConcerns = db['concerns'].find()
            concernJson = []

            for data in allConcerns:
                id = data['_id']
                userName = data['userName']
                email = data['email']
                agent = data['agent']
                concern = data['concern']
                concerntype = data['concernType']
                pri = data['priority']
                subject = data['subject']

                if concern == 'query':
                    description = data['description']
                    concernDict = {
                    "id": str(id),
                    "userName": userName,
                    "email": email,
                    "agent": agent,
                    "concern": concern,
                    "concernType": concerntype,
                    "priority": pri,
                    "subject": subject,
                    "description": description,
                    }
                
                else:
                    concernDict = {
                    "id": str(id),
                    "userName": userName,
                    "email": email,
                    "agent": agent,
                    "concern": concern,
                    "concernType": concerntype,
                    "priority": pri,
                    "subject": subject
                }

                concernJson.append(concernDict)
            return jsonify(concernJson)
        
@app.route('/concerns/<string:id>', methods = ['PUT', 'DELETE'])
def oneticket(id):
    # to update ticket
    if request.method == 'PUT':
        body = request.json
        email = body['email']
        agent = body['agent']
        subject = body['subject']

        if body['concern'] == "query":
            description = body['description']
            db['concerns'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "email": email,
                    "agent": agent,
                    "subject": subject,
                    "description": description
                }
            }
        )
            
        else:
            db['concerns'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "email": email,
                    "agent": agent,
                    "subject": subject
                }
            }
        )
        return jsonify({
            'message': 'ticket number ' + id + ' is updated!'
        })
    
    # to delete a ticket
    if request.method == 'DELETE':
        db['concerns'].delete_many({'_id': ObjectId(id)})
        return jsonify({
            'message': 'ticket number ' + id + ' is deleted'
        })


if __name__ == '__main__':
    app.debug = True
    app.run()