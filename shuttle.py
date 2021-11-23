#!/usr/bin/env python3

import json
import os
import time
 
home_dir = os.environ['HOME']
hosts_file = "/.shuttle.json"

with open(home_dir+hosts_file, "r") as file:
    lines = file.read()

hosts = json.loads(lines)["hosts"]

def selected_command(opt):
    if(len(hosts) > 0 and (opt+1) <= len(hosts)):
        os.system(hosts[opt]["cmd"])
    else:
        print("\nTry again! Choose a number to connect from the list provided.")

def f_connect():
    print("+-----------------------------------------------------------------------------------------------")
    print("| number | name                                        | command")
    print("+-----------------------------------------------------------------------------------------------")

    for index, host in enumerate(hosts):
        print("| {0}      | {1}   ".format(index, host["name"]))
        print(
            "|------------------------------------------------------ {0}\n".format(host["cmd"]))

    user_choice = input("\nChoose a number to connect: ")

    try:
        i_user_choice = int(user_choice)
        selected_command(i_user_choice)

    except ValueError:
        os.system("clear")
        print("Enter with a number!")
        time.sleep(2)
        os.system("clear")
        f_connect()

f_connect()        
