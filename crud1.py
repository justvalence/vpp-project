import os, subprocess, csv, json

#Running vpp command (with pipe). 
command = "sudo vppctl show ip arp | column -t"
process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
output = process.communicate()[0]

#output the result to text file for easy translation
s = open('showiparp.txt', 'w')
print >>s, output
s.close()

#Ready the txt file for json format translation(replace space with commas).
realoutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/todo-api/showiparp.txt").read()

#saving the readied output for json translation
s = open('showiparp.csv', 'w')
print >>s, realoutput
s.close()

#performing the .csv to .json translation, saving json output to a file
with open('showiparp.csv') as s:
	read = csv.DictReader(s)
	rows = list(read) 

json.dump(rows, open("showiparp.json", "w"), indent=4)
