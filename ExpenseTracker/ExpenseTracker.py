import datetime

import collections 
# my dictionary format is  {'date': { 'Income'  : [(category, amount)]   , 'Expense' :  [(category, amount)] }}
mydict = {  }

def add():
    global date
    mydict[date]["Income"] = []
    mydict[date]["Expense"] = []
    while True:
        # select which choice you want add
        choice = input("To add income(i),To add expense(e) and exit to return to menu : ")
        if choice == 'i':
            type_of_transaction = "Income"
            category = input("Enter a category name for Income :")
            amount = float(input("Enter the Amount: "))
            #mydict[date][type_of_transaction] = []
            
            mydict[date][type_of_transaction].append( (category, amount) )
            saveToFile(type,category,amount)
        elif choice == 'e':
            type_of_transaction = "Expense"
            category = input("Enter a category name for Expense :")
            amount = float(input("Enter the Amount: "))
            #mydict[date][type_of_transaction] = []
            mydict[date][type_of_transaction].append( (category, amount) )

        elif  choice.lower() == 'exit':
            break         
        else:
            print("Invalid Input")
            break

    saveToFile()


def saveToFile():
    pass

def Alllist():
    select = input("List all Expenses (all) or  List by Date (d)? ")
    if select.lower() == "all":
        print(mydict)
    elif select.lower() == "d":
        #list all transactions of a particular day
        key = input("Enter the date you want to see the transactions: ")
        try:
            print(mydict[key])
        except KeyError:
            print("No Transactions on that Day!")
    else:
        pass   # do nothing

def  update():
    pass

def  delit():
    pass
    

    
while True:
    select = input("add (a) , list expenses (l) , Update (u) or delete an expense (d) or 0  to exit? : ")
    if select.lower() == "a":
        # add new transaction to the selected day
        date = input("Enter a date in format dd/mm/yyyy: ")
        mydict[date] = {}
        add()
    elif  select.lower() == "l":
        Alllist()
        
    elif  select.lower() == "u":
        #update existing transaction
        print(mydict)
        update()
    elif  select.lower() == "d":
        #delete existing transaction
        delit()
    elif  select == '0':
        break
    else:
        break






'''print("\n\nYour Transaction History is as follows:\n")
for i in sorted(mydict.keys()):
    print(f'{i}:')
    for j in mydict[i].items():
        print(f"\t{j[0]} : ", end="")
        if len(j)==2:
            print(f"{j[1]['Income']}, {j[1]['Expense']}")
        else:
            print(j[1])'''