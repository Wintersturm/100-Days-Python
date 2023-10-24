#Write a program that interprets the Body Mass Index (BMI) 
#based on a user's weight and height.

# Enter your height in meters e.g., 1.55
height = float(input("Please enter your height! "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Please enter your weight! "))

weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / (height_as_float ** 2)
bmi_as_int = float(bmi)

if bmi_as_int < 18.5:
  print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int < 25:
  print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int == 25:
  print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int <30:
  print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int == 30:
  print(f"Your BMI is {bmi_as_int}, you are obese.")
elif bmi_as_int <35:
  print(f"Your BMI is {bmi_as_int}, you are obese.")
elif bmi_as_int == 35:
  print(f"Your BMI is {bmi_as_int}, you are clinically obese.")
else:
  print(f"Your BMI is {bmi_as_int}, you are clinically obese.")
  