# def readfile(path):
#     try:
#         with open(path,"r") as file:
#             return file.read()
#     except FileNotFoundError as e:
#         print("Not found the file")
#     finally:
#         print("reading attempted completed")
# print(readfile("Eprac.py"))  

#ATM VALIDATION________________________________________________
# class InstanceError(Exception):
#     pass
# def AtmFile(value):
#     if not value.isdigit():
#         raise InstanceError("value must be digits")
#     if len(value)!=4:
#         raise InstanceError("Pin must me four digits")

# try:
#     value=input()
#     AtmFile(value)
# except Exception as e:
#     print(e)
# else:
#     print("successfull login")


class Insufficient(Exception):
    def __init__(self,balance,value):
        super.__init__(f"withdrawal {value} is greaterthen valueof {balance} balnace vavailable")
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdrawal(self,value):
        if value>self.balance:
            raise Insufficient(self.balance,value)
acc=BankAccount(1000)
try:
    value=int(input())
    acc.withdrawal(value)
except ValueError as e:
    print("input is invalid")
except Exception as e:
    print(e)
else:
    print("succesfful withdrawal")

