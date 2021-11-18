#!/usr/bin/env python3

import json
import os

with open("shuttle.json", "r") as file:
	lines = file.read()

x = json.loads(lines)

print("+-----------------------------------------------------------------------------------------------") 
print("| number | name                                        | command")                                             
print("+-----------------------------------------------------------------------------------------------") 

hosts = []
count = 0

for i in x["hosts"][0]["home"]:
    count = count + 1
    print("| {0}      | {1}   ".format(count, i["name"], i["cmd"]))
    print("|------------------------------------------------------ {0}".format(i["cmd"]))
    hosts.append(i["cmd"])

user_choice = int(input("\nEnter a bookmark to connect: "))

if user_choice == 1:
    os.system(hosts[0])

elif user_choice == 2:
    os.system(hosts[1])

elif user_choice == 3:
    os.system(hosts[2])

elif user_choice == 4:
    os.system(hosts[3])

else: 
    print("Try again!")
