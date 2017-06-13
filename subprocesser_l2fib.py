#!/usr/bin/python
import os, subprocess, csv, json


def read_l2fib():
#Run command and get the l2fib table details. Remove the last line.
	command = "sudo vppctl show l2fib verbose | column -t | sed '$d; s/^ *//'"
	process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	stdout_value = process.communicate()[0]
#Paste retrieved l2fib table to a texfile
	textfile = open('showl2fibtable.txt', 'w')
	print >>textfile, stdout_value
	textfile.close()
#Change delimiter from space to comma and write to CSV file
	output = os.popen("awk '{$1=$1}1' OFS=, showl2fibtable.txt").read()
	file = open('showl2fibtable.csv', 'w')
	print >>file, output
	file.close()
#Convert csv format to json format, use of json.dump
	csvfile = open('showl2fibtable.csv', 'r')
	jsonfile = open('showl2fibtable.json', 'w')
	reader = csv.DictReader(csvfile)
	for row in reader:
		json.dump(row, jsonfile, indent=4)
		jsonfile.write('\n')
	jsonfile.close()
	csvfile.close()


def add_l2fib(mac_addr, bd_id, intf, stat):
#Get parameters and pass to bash command to execute
	command = "sudo vppctl l2fib add %s %s %s %s" % (mac_addr, bd_id, intf, stat)
	process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	stdout_value = process.communicate()[0] 


def upd_l2fib(mac_addr, bd_id, intf, stat):
#Get parameters and pass to bash command to execute
        command = "sudo vppctl l2fib add %s %s %s %s" % (mac_addr, bd_id, intf, stat)
        process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
        stdout_value = process.communicate()[0] 


def del_l2fib():
#Run command to clear l2fib table and retrieve the table for later use 
	command1 = "sudo vppctl clear l2fib"
	process1 = subprocess.call(command1,shell=True)
	command2 = "sudo vppctl show l2fib verbose | column -t | sed '$d; s/^ *//'"
        process2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)
        stdout_value = process2.communicate()[0]
#Paste retrieved l2fib table to a texfile
        textfile = open('showl2fibtable.txt', 'w')
        print >>textfile, stdout_value
        textfile.close()
#Change delimiter from space to comma and write to CSV file
        output = os.popen("awk '{$1=$1}1' OFS=, showl2fibtable.txt").read()
        file = open('showl2fibtable.csv', 'w')
        print >>file, output
        file.close()
#Convert csv format to json format, use of json.dump
        csvfile = open('showl2fibtable.csv', 'r')
        jsonfile = open('showl2fibtable.json', 'w')
        reader = csv.DictReader(csvfile)
        for row in reader:
                json.dump(row, jsonfile, indent=4)
                jsonfile.write('\n')
        jsonfile.close()
        csvfile.close()
