import csv

transID = {}
itemsID = {}

with open('data-70000.csv', 'rb') as csvfile:
    all_trans = csv.reader(csvfile, delimiter=',')
    index = 0
    for trans in all_trans:
        arr_items = trans[2].split('/')
        if trans[1] not in transID:
            transID[trans[1]] = []
        for item in arr_items:
            if item and item not in transID[trans[1]]:
                transID[trans[1]].append(item)
            if item and item not in itemsID:
                index += 1
                itemsID[item] = index

file_name = 'tranform_ecom_data.txt'
file = open(file_name, 'w')
for trans in transID:
    for item in transID[trans]:
        file.write(str(itemsID[item]) + ' ')
    file.write('\n')
file.close()

file_name = 'items_id.txt'
file = open(file_name, 'w')
new_list = sorted(itemsID.keys())
for item in new_list:
    file.write(item + ' = ' + str(itemsID[item]) + '\n')
file.close()

print 'finish'
