import os, subprocess, csv, json

commnd = "sudo vppctl show interface | column -t"
output = subprocess.Popen(commnd, shell=True, stdout=subprocess.PIPE)
result = output.communicate()[0]

file = open ('showresult.txt', 'w')
print >> file, result
file.close()

newOutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/vpp-api/showresult.txt").read()

file = open('showresult.csv', 'w')
print >> file, newOutput
file.close()

with open('showresult.csv') as file:
	read = csv.DictReader(file)
	rows = list(read)

json.dump(rows, open("showresult.json", "w"), indent = 4)

