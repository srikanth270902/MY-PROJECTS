name=input('enter your Name: ')
age= int(input("enter your age: "))
totalyears=str(50-age)

if age<50:
    print(""+name.title()+" got "+totalyears+" to reach 50")
else:
    print(""+name.title()+" crossed 50 before "+totalyears+"")