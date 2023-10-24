#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. 

# 1st input: enter height in meters e.g: 1.65
height = input("What is your height?")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight?")

new_height = float(height)
new_weight = int(weight)
bmi = new_weight / (new_height * new_height)
bmi_new = int(bmi)
print(bmi_new)