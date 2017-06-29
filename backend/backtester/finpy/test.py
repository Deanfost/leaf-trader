lister = [1,2,3,4]
lister2 = [3,5]
lister3 = [3,6]
lister4 = []

full_list = [lister, lister2, lister3, lister4]
new_full_list = []
for listerr in full_list :
    if len(listerr) > 0 :
        new_full_list.append(listerr)

finalresult = set(new_full_list[0])

for lister in new_full_list[1:]:
    finalresult.intersection_update(lister)


print finalresult
