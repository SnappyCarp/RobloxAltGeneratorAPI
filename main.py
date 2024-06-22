import requests, json, random
from datetime import datetime

# Load Json Data
with open("config.json") as js:
    data = json.load(js)
    baseUsername = str(data['startofusername'])
    password = str(data['password'])
    numbersafterusername = int(data['Digits'])

accountnumber = 1

class generator():
    def __init__(self) -> None:
        currentYear = datetime.now().year
        self.sesh = requests.Session()
        self.birthday = "{}-01-01T07:00:00.000Z".format(currentYear - 99)
        self.sesh.get("https://www.roblox.com/signup")
        while True:
            self.username = baseUsername + self.genNumber()
            if self.checkUsername(self.username):
                print("Username Not In Use. Continuing")
                break
            else:
                print("Username In Use. Regenerating")
                pass
        # Continue
        self.Signup()
    def genNumber(self):
        tempList = list()
        for i in range(numbersafterusername): 
            tempList.append(str(random.randint(0, 9)))
        return str().join(tempList)
    
    def checkUsername(self, usernam: str):
        used = requests.get("https://auth.roblox.com/v1/usernames/validate", {"username":usernam,"context":"Signup","birthday":self.birthday})
        if used.json()["code"] == 0: return True
        else: return False
    
    def Signup(self):
        currentUsername = self.username
        # Signup
        self.sesh.post()
        # Write Log
        with open("log.txt", 'a') as log:
            write = "Successfully Created Account: " + self.username
            print(write)
            log.write(write)
            log.write("\n")
            log.close()

print("Creating {} Accounts".format(accountnumber))
# Enter Account Making Loop
for i in range(int(accountnumber)):
    g=generator()