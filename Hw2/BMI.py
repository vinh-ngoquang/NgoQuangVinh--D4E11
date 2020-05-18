height = int(input('Your Height(cm): '))
weight = int(input('Your Weight(kg): '))
bmi = weight / ((height*height)/10000)

if bmi <= 16:
    print(' You are servely underweight')
elif bmi > 16 and bmi <= 18.5:
    print('You are underweight')
elif bmi > 18.5 and bmi <= 25:
    print('You are normal')
elif bmi > 25 and bmi <= 30:
    print('You are overweight')
else:
    print('You are obese')