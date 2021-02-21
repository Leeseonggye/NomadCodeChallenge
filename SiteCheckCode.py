import requests
import os
InputSite = input("Wecome to IsItDown.py!\nPlease write a URL or URLs you want to check.(separated by comma)").split(",")

for i in range(len(InputSite)):
    if 'http://' in InputSite[i]:
        InputSite[i] = InputSite[i].strip()
    else:
        InputSite[i] = 'http://' + InputSite[i].strip()

try:
    for Site in InputSite:
        URL = requests.get(Site)
        if URL.status_code == 200:
            print(f"{Site} is up!")
        else:
            print(f"{Site} is down!")        
except:
    print(f"{Site} is not a valid.")

continueQ = input("Do you want to start over? y/n: ")

while continueQ == "y":
    InputSite = input("Wecome to IsItDown.py!\nPlease write a URL or URLs you want to check.(separated by comma)").split(",")
    for i in range(len(InputSite)):
        if 'http://' in InputSite[i]:
            InputSite[i] = InputSite[i].strip()
        else:
            InputSite[i] = 'http://' + InputSite[i].strip()
    try:
        for Site in InputSite:
            URL = requests.get(Site)
            if URL.status_code == 200:
                print(f"{Site} is up!")
            else:
                print(f"{Site} is down!")        
    except:
        print(f"{Site} is not a valid.")
    continueQ = input("Do you want to start over? y/n: ")


if continueQ == "n":
    print("Okay bye.")

        
else:
    print("That's not a valid answer.")