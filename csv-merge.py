import os, datetime

x = datetime.datetime.now()
csv_header = 'standard,standard'
csv_out = 'out/consolidated_'+x.strftime("%c")+'.csv'

csv_dir = os.getcwd()

dir_tree = os.walk(csv_dir+'/in')
for (dirpath, dirnames, filenames) in dir_tree:
    pass

csv_list = []
for file in filenames:
    if file.endswith('.csv'):
        csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header+','+'branch')
csv_merge.write('\n')

for file in csv_list:
    csv_in = open('in/'+file)
    for line in csv_in:
        if line.startswith(csv_header):
            continue      
        newline=line.rstrip()+','+file.replace('.csv', '')+'\n'
        csv_merge.write(newline)
    csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)

			