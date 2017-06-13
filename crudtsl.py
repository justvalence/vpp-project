import os, subprocess, csv, json

#run vpp command
vpp = "sudo vppctl show bridge-domain | column -t"
pro = subprocess.Popen(vpp,shell=True,stdout=subprocess.PIPE)
output = pro.communicate()[0]

#output into a text file
o = open('bridge.txt', 'w')
print >>o, output
o.close()

#readying txt for json
toutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/bridge.txt").read()

#translate to json
o = open('bridge.csv', 'w')
print >>o, toutput
o.close()

#.csv to .json translation
with open('bridge.csv') as o:
        reader = csv.DictReader(o)
        rows = list(reader)
json.dump(rows, open('bridge.json', 'w'), indent=4)

