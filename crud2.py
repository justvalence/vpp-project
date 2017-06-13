#!flask/bin/python
from flask import Flask,jsonify,abort,request
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'sti':
		return 'sti'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 401)
import subprocess

app = Flask(__name__)

subpro = subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
res = subpro.communicate()[0]

tasks=res

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	return tasks

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_tasks():
	task = {
		'flags': request.json['flags'],
		'IP4': request.json['IP4'],
		'Interface': request.json['Interface'],
  		'Ethernet': request.json['Ethernet']
	}

	flag= str(request.json['flags'])
	ipaddr= str(request.json['IP4'])
	interface= str(request.json['Interface'])
	eth= str(request.json['Ethernet'])

	insert= "sudo vppctl set ip arp %s %s %s %s" % (flag, interface, ipaddr, eth)
	sub6= subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
	soutput= sub6.communicate()[0]

	supdate = "python crud1.py"
	subprocess.call(supdate,shell=True)

	ssub = subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
	newres = ssub.communicate()[0]
	newtasks = newres
	
	return ''

@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
@auth.login_required
def Update_tasks():
	
	task = {
                'flags': request.json['flags'],
                'IP4': request.json['IP4'],
                'Interface': request.json['Interface'],
                'Ethernet': request.json['Ethernet']
        }

        flag= str(request.json['flags'])
        ipaddr= str(request.json['IP4'])
        interface= str(request.json['Interface'])
        eth= str(request.json['Ethernet'])

	insert= "sudo vppctl set ip arp %s %s %s %s" % (flag, interface, ipaddr, eth)
        sub6= subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
        soutput= sub6.communicate()[0]

        supdate= "python crud1.py"
        subprocess.call(supdate,shell=True)

        ssub= subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
        newres = ssub.communicate()[0]
        newtasks = newres
        
        return ''


	return ''

@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def delete_tasks():
        task = {
                'flags': request.json['flags'],
                'IP4': request.json['IP4'],
                'Interface': request.json['Interface'],
                'Ethernet': request.json['Ethernet']
        }

        flag= str(request.json['flags'])
        ipaddr= str(request.json['IP4'])
        interface= str(request.json['Interface'])
        eth= str(request.json['Ethernet'])

        insert= "sudo vppctl set ip arp %s delete %s %s %s" % (flag, interface, ipaddr, eth)
        sub6= subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
        soutput= sub6.communicate()[0]

        supdate= "python crud1.py"
        subprocess.call(supdate,shell=True)

        ssub= subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
        newres = ssub.communicate()[0]
        newtasks = newres

        return ''



if __name__ == '__main__':
	app.run(debug=True)
