#from flask import Flask, jsonify, request
import time
import threading
from scan_runner import scan_control_thread
import scan_db

"""
app = Flask(__name__)

@app.route('/', methods=['POST'])
def new_scan():
"""
"""
<scan>
"""
"""
    #new_scan = json.loads(request.data)
    scan_db.add_scan(new_scan)
    
@app.route('/scheduled/', methods=['GET'])
def get_scheduled():
    return scan_db.get_scheduled_scans()
    
@app.route('/running/', methods=['GET'])
def get_running():
    return scan_db.get_running_scans()

@app.route('/previous/', methods=['GET'])
def get_previous():
    return scan_db.get_previous_scans()

@app.route('/edit/', methods=['PUT'])
def edit_scan():
"""
"""
{
scan_id : <scan_id>,
scan : <scan_dict>
}
"""
"""
    editted_scan = json.loads(request.data)
    scan_db.edit_scan(editted_scan["scan_id"], editted_scan["scan"])

@app.route('/delete/', methods=['DELETE'])
def delete_scan():
"""
"""
<scan_id>
"""
"""
    delete_scan_id = json.loads(request.data)
    scan_db.delete_scan(delete_scan_id)
"""

if __name__ == '__main__':
    scan_db.load_db("database.json")
    scan_thread = scan_control_thread()
    scan_thread.start()
    