# variables and data types
num = 10 # integer (int)
height = 1.72 # float
name = "Steve" # String (str)
is_student = True # Boolean (bool)

print(num)

# Arithmetic operations: sum, difference, product, division, power, modulo
print("The sum of num and 3 is ", num + 3)
print("The difference between num and 2 is", num - 2)
print("Num divided by 2 is", num/2)
print("The product of 4 and 6 is", 4*6)
print("Two cubed is", 2**3)
print(9%3)
print(5%2)

# Ask the user to enter their favourite number
# Output: tell the user if it's even or odd

user_input = int(input("Enter your favourite number: "))
if user_input % 2 == 0:
    # What the program will do if the user's fav number is even
    print(f"{user_input} is even!")
    # "4 is even!"
else:
    # What the program will do if fav number is odd
    print(f"{user_input} is odd!")

# for loop
# We want to iterate over the sequence of nums 0, 1, 2, 3, 4
for i in range(5):
    print(f"For this iteration of the for loop, i is {i}")

# while loop
count = 0

while count < 5:
    print(f"Count is {count}")
    count = count + 1