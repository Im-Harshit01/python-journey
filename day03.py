# This a basic code to check the age of a person to see if they can go for a ride on a roller coaster.

age = int(input("What is your age? "))

if age >= 75:
    print("The ride could be dangerous for senior citizens")
elif age >= 16:
    print("you can go for a ride on roller coaster")
else:
    print("you  can't go for a ride")



# This is a more advanced version of the code that checks the age of a person to see if they can go for a ride on a roller coaster, and also checks if they have any heart problems.

age = input("What is your age? ")
if not age.isdigit():
    print("Please enter your age in numbers.")
    exit()
else:
    age = int(age)
is_heart_problem = input("Do you have any heart problems? (YES/NO) ").upper().strip()
if is_heart_problem not in ["YES", "NO"]:
    print("Please answer with YES or NO.")
    exit()

if age >= 75 or age < 16 or is_heart_problem == "YES":
    print("You cannot go for a ride on the roller coaster.")
else:
    print("You can go for a ride on the roller coaster.")



# This is a code to check if a device is compatible with an app based on its RAM, storage, and graphics card.

Device_ram = input("Enter your device RAM in GB: ")
if not Device_ram.isdigit():
    print("Please enter your Device_ram in numbers.")
    exit()
else:
    Device_ram = int(Device_ram)
Availablestorage = input("Enter your available storage in GB: ")
if not Availablestorage.isdigit():
    print("Please enter your Storage in numbers.")
    exit()
else:
    Availablestorage = int(Availablestorage)
is_rtx_2060 = input("Do you have RTX 2060+ graphics card? (YES/NO) ").upper().strip()
if is_rtx_2060 not in ["YES", "NO"]:
    print("Please answer with YES or NO.")
    exit()
else:
    is_rtx_2060 = is_rtx_2060 == "YES"
if Device_ram >= 6 and Availablestorage >= 64 and is_rtx_2060:
    print("Your device is compatible with the app.")
else:
    print("Your device is not compatible with the app.")