# List of IDs: adding, removing
user_ids = [1689, 7438, 9480, 4029]

# How to access first item in list
user_ids[0]

for item in user_ids:
    print(f"Person has id {item}.")

user_ids.append(8743)
print(user_ids)

user_ids.remove(1689)
print(user_ids)

# Sorting
user_ids.sort()
print(user_ids)

# 2D list: iteration, accessing items
transactions = [[45.6, 72.0, 99.9], 
                [4563, 52726, 0.2], 
                [78347, 0.7, 44]]

for row in transactions:
    print(row)

    for item in row:
        print(item)

# Accessing item in 2D list
print(transactions[2][1])

# Dictionaries: creation, adding key-value pair, updating value, iterating

user_profile = {
    'user_id' : 10101,
    'name' : 'Sally',
    'balance' : 150.75
}

print("ID number", user_profile['user_id'])

user_profile['last_login'] = '03-10-2024 14:39'
print(user_profile)

print("The result:", user_profile.items())

for key, value in user_profile.items():
    print(f"The key is {key} and its associated value is {value}.")

# String handling: leading/trailing whitespace, case conversion, splitting

email = "    Transaction confirmed: Sally bought an item worth R13500.  "

print("Original email:", email)
print("Edited email:", email.strip())
print("Emphasising email:", email.strip().upper())

words_list = email.split()
print(words_list)

words = email.split(':')
print(words)
