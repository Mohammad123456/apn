import numpy as np
import glob

for file_path in glob.glob('MMLTask_PS-CS-MAE*'): #glob for regex in path
    text = open(file_path, 'r')
    lines = np.array(text.readlines())
########################################## find node names
search_res = np.char.find(lines, "ugw@")
nodes_index = np.where(search_res > -1)[0]
nodes_names = []
for i in range(len(nodes_index)):
    nodes_names.append(lines[nodes_index[i]][5:11])
nodes_names=[item.strip() for item in nodes_names] #delete /n end of names
########################################### insert time column
time_index = []
node_time = []
for i in nodes_index:
    time_index.append(i+2)
for q in time_index:
    node_time.append(lines[q][18:38])

########################################## inset last segment for last node
nodes_index = np.append(nodes_index,(len(lines)-1))

######################################### separate started
sep1=[]
for i in range(len(nodes_index)-1):
    sep1.append(lines[nodes_index[i]:nodes_index[i+1]])

apn_name = []
apn_used = []
for i in range(len(sep1)):

    apn_name.append([])
    apn_used.append([])
    start = np.char.find(sep1[i], "Ip Address Allocation Method")
    index_start = np.where(start > -1)[0]
    end = np.char.find(sep1[i], "---    END")
    index_end = np.where(end > -1)[0]
    for j in range(len(index_start)):
        table = (sep1[i][index_start[j]+4:index_end[j]-1])
        # table2.append(table)
        for l in range(len(table)):
            apn = table[l][0:21]
            apn_name[i].append(apn)
            apn_used[i].append(table[l][28:40])

###################################### nodes appendded in 1 column
node_append = []
for i in range(len(nodes_names)):
    node_append.append([])
    for j in range (len(apn_name[i])):
        node_append[i].append(nodes_names[i])
#################################### time append in 1 column
time_append = []
for i in range(len(node_time)):
    time_append.append([])
    for j in range (len(apn_name[i])):
        time_append[i].append(node_time[i])
################################## result - merge result arrays
for i in range(len(nodes_names)):
    ar3 = []
    ar3.append(time_append[i])
    ar3.append(node_append[i])
    ar3.append(apn_name[i])
    ar3.append(apn_used[i])
    ar3 = np.array(ar3)
    np.savetxt(str(nodes_names[i]+".csv"), ar3.T, delimiter=",", fmt='%s')



print (nodes_index)
print (time_index)
print(node_time)