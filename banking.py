user_list = []
employee_list = []

class account :
    
    user_list = []
    username_list = []

    def __init__(self, accNumber, Name, password, balance):
        self.Name=Name
        self.accNumber=accNumber
        self.password=password

    def edit_account(self):
        
        pw = input("enter password: ")
        if (pw==self.password):
            choice=int(input("1-- to change username\n2-- to change password\n"))
            if(choice==1):
                self.Name=input("enter new username: ")
            elif ( choice==2 ):
                self.password=input("enter new password: ")
            else:
                print("invalid")
        else:
            print("Wrong credentials")

    def money(self):
        pw = input("enter password: ")
        if (pw==self.password):
            choice=int(input("1 to withdraw\n2 to add"))
            if(choice==1):
                amount=int(input("Amount: "))
                self.amount=self.amount-amount
            elif ( choice==2 ):
                amount=int(input("Amount: "))
                self.amount=self.amount+amount
            else:
                print("invalid")
        else:
            print("Wrong credentials")

    def delete(self, i):
        pw = input("enter password: ")
        if (pw==self.password):
            del account.username_list[i]
            del account.user_list[i]
            print("delete succesful")
        else:
            print("Wrong credentials")

    def __del__ (self):
        print("\n")

class employess:

    emp_list = []
    empname_list = []

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def edit(self):
        self.name=input("enter name: ")
        self.age=input("age: ")
        self.salary=input("enter salary: ")

edit=True
input1=int(input("1 for customer\n2 for employes\n"))
print("\n")
if(input1==1):
    while(edit):
        input2=int(input("\n1 for new account\n2 for edit details\n3 for transactions\n4 to delete account\n"))
        if(input2==1):
            name = input("\nenter your username: ")
            accNumber = input("enter alloted account number: ")
            password = input("enter a password: ")
            balance = int(input("Enter deposite amount: "))
            o = account(accNumber,name,password,balance)
            account.user_list.append(o)
            account.username_list.append(o.Name)
        elif(input2==2):
            username = input ("\nenter username: ")
            i = account.username_list.index(username)
            o= account.user_list[i]
            o.edit_account()
        elif(input2==3):
            username = input ("\nenter username: ")
            i = account.username_list.index(username)
            o= account.user_list[i]
            o.money(i)

        elif(input2==4):
            username = input ("\nenter username: ")
            i = account.username_list.index(username)
            o= account.user_list[i]
            o.delete(i)

        else:
            print("invalid\n")
        
        status = int(input("\n1 for done\nanything for not done\n"))
        if(status==1):
            edit=False
        del o

elif(input1==2):
    while(edit):
        input2=int(input("\n1 for new employee\n2 for edit details\n"))
        if(input2==1):
            name = input("\nenter your username: ")
            age = input("enter age: ")
            salary = int(input("enter salary: "))
            o = employess(name,age,salary)
            employess.emp_list.append(o)
            employess.empname_list.append(o.name)
        elif(input2==2):
            username = input ("\nenter username: ")
            i = employess.empname_list.index(username)
            o= employess.emp_list[i]
            o.edit()

        else:
            print("invalid\n")
        
        status = int(input("\n1 for done\nanything for not done\n"))
        if(status==1):
            edit=False
        del o

else:
    print("invalid")
