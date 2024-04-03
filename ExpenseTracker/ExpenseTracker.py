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
        key = input("Enter the date (dd/mm/yyyy) you want to see the transactions: ")
        try:
            print(mydict[key])
        except KeyError:
            print("No Transactions on that Day!")
    else:
        pass   # do nothing

def  update():
    pass

def  delit():
    print(mydict)
    while True:
        select = input("Enter a date(dd/mm/yyyy), TYPE('Income' / 'Expense') and Category you want to remove a transaction for separated by comma : ")
        select = select.split(", ")
        print(select[0] + "\n" + select[1] +"\n" +select[2])
        for t in mydict[select[0]][select[1]]:
            if  t[0] == select[2]:
                mydict[select[0]][select[1]].remove(t)
        print(f'Transaction Removed from {select[0]} on {select[1]}: ')
        
        conti = input("\nDo you wish to continue removing more items? Y/N : ")
        if conti.lower() != 'y':
            break
        select = input("Enter a date, TYPE and Category you want to remove a transaction for separated by comma : ")
    
def balance():
    print(mydict)
    while True:
        checkDate = input("Enter the month and year(mm/yyyy) your summary or exit to return to menu: ")
        if checkDate =='exit':
            break
        else:
            mydates = list(mydict.keys())
            totalIncome = 0
            totalExpense = 0
            for i in mydates:
                if i[3:] == checkDate:
                    for  j in mydict[i]['Income']:
                        totalIncome += float(j[1])
                    for k in mydict[i]['Expense']:
                        totalExpense += float(k[1])
            
            net_balance = totalIncome - totalExpense
            print(f'\nSummary for {checkDate}:\n Incomes:{totalIncome}\n Expenses:{totalExpense}\n Net Balance:{net_balance}\n')
    
while True:
    select = input("add (a) , list expenses (l) , Update (u) or delete an expense (d) or check monthly budget(b) or 0  to exit? : ")
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
    elif  select.lower() == 'b':
        #show balance of specific month 
        balance()
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
