print("===== Expens Tracker =====")

expenses=[]

amount=float(input("Enter Expense Amount : "))

expenses.append(amount)


while True:


 user_input=input("enter expenses amount or done to finish ")

 if user_input == "done" :

     break 

 new_amount=float(user_input)
 expenses.append(new_amount)

print(f"your expenses list is : {expenses}")

total=sum(expenses)

print(f" Total expenses is : {total}")



  