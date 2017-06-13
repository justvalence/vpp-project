#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'Zhenghan':
	return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


vpp = Flask(__name__)
cld = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
output = cld.communicate()[0]
tasks = output

@vpp.route('/vpp/tasks', methods=['POST'])
@auth.login_required
def create_loop():
	createl = 'sudo vppctl loopback create-interface'
	subprocess.call(createl,shell=True)
	return ''

@vpp.route('/vpp/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
        return tasks

@vpp.route('/vpp/tasks', methods=['PUT'])
@auth.login_required
def update_tasks():

        task= {
                'ID': request.json['ID'],
                'Fwd': request.json['Fwd'],
                'Disable': request.json['Disable']
        }

        ID = str(request.json['ID'])
        Fwd = str(request.json['Fwd'])
        Disable = str(request.json['Disable'])
        Update = "sudo vppctl set bridge-domain %s %s %s" % (Fwd, ID, Disable)
        subp = subprocess.Popen(Update,stdout=subprocess.PIPE,shell=True)
        result = subp.communicate()[0]

        return ''

@vpp.route('/vpp/tasks', methods=['DELETE'])
@auth.login_required
def delete_loop():
	if not request.json or not 'Name' in request.json:
		abort(400)
	task = {'Name': request.json['Name']}
	loopintf = str(request.json['Name'])
	deletel = 'sudo vppctl loopback delete-interface intfc %s' % (loopintf)
	subprocess.call(deletel,shell=True)
	return ''


if __name__ == '__main__':
	vpp.run(debug=True)
