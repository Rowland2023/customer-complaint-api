from flask import Flask,request,jsonify
from app.complaint import CustomerComplaint

app = Flask(__name__)

scheduled = CustomerComplaint(category= 'general')
def serialize_complaint(c):
    return {
        'customer_type': c['customer_type'],
        'category': c['category'],
        'timestamp': c['timestamp'],
        'submitted': c['submitted'].isoformat()
    }
@app.route('/add_complaint',methods=['POST'])
def add_order():
    data = request.get_json()
    try:
        scheduled.submit_complaint(data)
        return jsonify({'message':'complain submitted successfully'}),200
    except Exception as e:
        return jsonify({'error': f'Missing field: {str(e)}'}),500
    
@app.route('/next_complaint',methods=['GET'])
def get_next_complaint():
    complaints = scheduled.get_next_complaint()
    if not complaints:
        return jsonify({'error':'No complaint in queue'}),400
    return jsonify({'next_complaint':serialize_complaint(complaints)}),200
