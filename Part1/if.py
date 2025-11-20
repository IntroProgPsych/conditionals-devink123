
# if = does some code ONLY IF a condition is true
# else is going to do nothing

age = int(input("Type your age"))
if age>=18 and age<100:
    print("you are an adult")
elif age>=100:
    print("you are too old")
elif age<=0:
    print("you haven't been born yet")
else: 
    print("you are a child")