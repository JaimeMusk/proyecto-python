##Saludo##
print(f"\tWelcome to the Basketball Roster Program")
##Roadster##
roster = []    #.title para el nombre##
roster.append(input("\tWho is your point guard:\t").title())
roster.append(input("\tWho is your shooting guard:\t").title())
roster.append(input("\tWho is your small forward:\t").title())
roster.append(input("\tWho is your power forward:\t").title())
roster.append(input("\tWho is your center:\t\t").title())
##cambios del roadster##
print(f"\n\t\tYour starting 5 for the upcoming basketball season\n\t\t\tPoint Guard:\t\t{roster[0]}\n\t\t\tShooting Guard:\t\t{roster[1]}\n\t\t\tSmall Forward:\t\t{roster[2]}\n\t\t\tPower Forward:\t\t{roster[3]}\n\t\t\tCenter:\t\t\t{roster[4]}\n")
print(f"\n\tOh no, {roster[2]} is injured.")
removed_player = roster[2]
del roster[2]
print(f"\tYour roster only has {len(roster)} players.")
roster.insert(2,input(f"\tWho will take {removed_player}`s spot:\t").title())
print(f"\n\t\tYour starting 5 for the upcoming basketball season\n\t\t\tPoint Guard:\t\t{roster[0]}\n\t\t\tShooting Guard:\t\t{roster[1]}\n\t\t\tSmall Forward:\t\t{roster[2]}\n\t\t\tPower Forward:\t\t{roster[3]}\n\t\t\tCenter:\t\t\t{roster[4]}\n")