col1=['blue','green','red','white','black']
col2=['yellow','red','blue','indigo','white']
for i in range(len(col1)):
    if col1[i] not in col2:
        print("the colors are:"+col1[i])

