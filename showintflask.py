#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

cmd = subprocess.Popen('cat showresult.json', stdout = subprocess.PIPE, shell = True)
output = cmd.communicate()[0]
intoutput = output

@app.route('/vpp/api/tasks', methods=['GET'])
@auth.login_required
def get_interface():
	return intoutput

@app.route('/vpp/api/tasks', methods=['POST'])
def create_interface():
	if not request.json or not 'intname' in request.json:
		abort(400)

	task = {'intname': request.json['intname']}
	newint = str(request.json['intname'])
	createintcmd = 'sudo vppctl create host-interface name %s' % (newint)
	subprocess.call(createintcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
	return jsonify({'Output':'Command Executed'})

@app.route('/vpp/api/tasks', methods=['DELETE'])
def delete_interface():
	if not request.json or not 'name' in request.json:
		abort(400)
	tasks = {'name': request.json['name']}
	delint = str(request.json['name'])
	delintcmd = 'sudo vppctl delete host-interface name %s' % (delint)
	subprocess.call(delintcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
	return jsonify({'Output':'Command Executed'})

@app.route('/vpp/api/tasks/up', methods=['PUT'])
def state_up():
	if not request.json or not 'getnameup' in request.json:
		abort(400)
	tasks = {'getnameup': request.json['getnameup']},
	getintUPname = str(request.json['getnameup'])
	setintstateUPcmd = 'sudo vppctl set interface state %s up' % (getintUPname)
        subprocess.call(setintstateUPcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})

@app.route('/vpp/api/tasks/down', methods=['PUT'])
def state_down():
        if not request.json or not 'getnamedown' in request.json:
                abort(400)
        tasks = {'getnamedown': request.json['getnamedown']},
	getintDOWNname = str(request.json['getnamedown'])
        setintstateDOWNcmd = 'sudo vppctl set interface state %s down' % (getintDOWNname)
        subprocess.call(setintstateDOWNcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})

@auth.get_password
def get_password(username):
	if username == 'user1':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 401)

if __name__ == '__main__':
	app.run(debug=True)
