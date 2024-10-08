'''
You are an event organiser. You have a file with 
the names of people you work with and the service
they offer. Our goal is to read the file and 
display the services offered by the people in your
contact list.
'''

with open('event_items.txt', 'r') as file:
    lines = file.readlines()
    # print(lines) # Just checking

# Initialise list
services = []

for line in lines:
    # First iteration: line = 'Sarah Baker: Catering\n'
    name, service = line.strip().split(':')

    services.append(service.strip())
  
# print(services)

for item in services:
    print(item)