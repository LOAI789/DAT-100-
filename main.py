import lister_for_del_1



#d 
def noe(liste,tall):
    sum = 0
    for i in liste:
        if i >= tall:
            sum +=1
    return sum

#e 
def diff(liste):
    differanse = []
    for i in range(len(liste)-1):
        differanse.append(liste[i]-liste[i+1])
    return differanse



#i
"""
print("Antall dager over eller lik 20:",noe(lister_for_del_1.temperaturer,20))
print("Antall dager over eller lik 25:",noe(lister_for_del_1.temperaturer,25))
print("Antall dager over eller lik 30:",noe(lister_for_del_1.temperaturer,30))
"""

#j 
"""
for i in diff(lister_for_del_1.temperaturer):
    if i > 0:
        print("Stigende",i)
    else:
        print("Synkende",i)
"""