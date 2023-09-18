import lister_for_del_1



#d 
def noe(liste,tall):
    sum = 0
    for i in liste:
        if i >= tall:
            sum +=1
    return sum

#i
print("Antall dager over eller lik 20:",noe(lister_for_del_1.temperaturer,20))
print("Antall dager over eller lik 25:",noe(lister_for_del_1.temperaturer,25))
print("Antall dager over eller lik 30:",noe(lister_for_del_1.temperaturer,30))