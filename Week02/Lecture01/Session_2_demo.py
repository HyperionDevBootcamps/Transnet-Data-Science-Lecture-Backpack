# for loops
for i in range(4):
    print(i)

print("------------------------------------------")
# while loops
count = 0

while count < 11:
    print(f"Count is {count}")
    count = count + 1
    print(f"Count is {count} after adding 1 to it.")

print("------------------------------------------")

# Boolean data type and logical operators

has_access_permission = True
is_system_online = False

# case 1: user is able to do their job if they have access and sys online
# case 2: user has access but system is offline
# case 3: user does not have permission to access

if has_access_permission and is_system_online:
    print("You can proceed and do your job.")
elif has_access_permission and not is_system_online:
    print("You have access, but the system is offline")
else:
    print("You do not have access.")

print("------------------------------------------")

# Error Handling
'''
try:
    num = int(input("Enter a number:"))
    result = 100 / num
    print(f"100 divided by {num} is {result}.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Error: input invalid. Please enter a number.")
'''

while True:
    try:    
        num = int(input("Enter any positive number or -1 to quit:"))

        if num == -1:
           print("Goodbye!")
           break

        else:
           result = 100 / num
           print(f"100 divided by {num} is {result}.")

    except ValueError:
        print("Error: input invalid. Please enter a number.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")