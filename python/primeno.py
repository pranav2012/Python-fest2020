# BEGINNING OF CODE


nom = int(input("ENTER A NUMBER: "))
if nom > 1:
    for i in range(2, nom):
        if (nom % i) == 0:
            print(nom, "ISN'T A PRIME NUMBER")
            break
    else:
        print(nom, "IS A PRIME NUMBER")
else:
    print(nom, "IS A PRIME NUMBER")
    
    
#END OF CODE
#This code was written by arnavk09 for HacktoberFest 2020
