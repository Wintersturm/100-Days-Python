#Write a program that works out whether if a given number is an odd or even number.

# Which number do you want to check?
number = int(input("Choose a number! "))

new_number = int(number) % 2

if new_number != 1:
  print("This is an even number.")
else:
  print("This is an odd number.")
