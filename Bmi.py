x = float(input("enter your weight"))
y = float(input("enter your height"))
z = y/100
bmi = x/(z**2)
if bmi<18.5:
    print("you are underweight")
elif bmi>=18.5 and bmi<25:
    print("normal")
elif bmi>=25 and bmi<30:
    print("overweight")
else :
    print("obesity")





