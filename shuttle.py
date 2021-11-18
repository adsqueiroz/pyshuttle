#!/usr/bin/env python3

import json
import os

with open("shuttle_0.json", "r") as file:
	lines = file.read()

x = json.loads(lines)

print("+-----------------------------------------------------------------------------------------------") 
print("| number | name                                        | command")                                             
print("+-----------------------------------------------------------------------------------------------") 

count = 0

for i in x["hosts"][0]["home"]:
    count = count + 1
    print("| {0}      | {1}   ".format(count, i["name"], i["cmd"]))
    print("|------------------------------------------------------ {0}".format(i["cmd"]))


op = int(input("\nEnter a bookmark to connect: "))

if op == 1:
    print(" ")
    os.system(i["cmd"])        

elif op == 2:
    print(" ")    
    os.system(i["cmd"])        

elif op == 3:
    print(" ")    
    os.system(i["cmd"])        

else:
    print("\nChoose again!")
