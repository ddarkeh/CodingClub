# Import required modules.
import time, re

# User inputs time.
userInput = input("Enter the time (HH:MM:SS):  ")

# Loop is repeated if the user input does not match the regex pattern.
while not re.match("(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)", userInput):
    print("Error! Please enter the time in the correct format (HH:MM:SS)")
    userInput = input("Enter the time (HH:MM:SS): ")

#Splits the user input using ":" as the divider and gives them separate variables so they can be modified.
userHH, userMM, userSS = userInput.split(":")

while True:
    if int(userSS) > 59:
        userSS = 00 # Changes seconds to 00 when they go above 59
        userMM = int(userMM) + 1 # Increases minutes be 1 when seconds rise above 59.
    if int(userMM) > 59:
        userMM = 00 # Changes minute to 00 when it goes above 59.
        userHH = int(userHH) + 1 # Increases hour by 1 when minutes rise above 59.
    if int(userHH) > 23:
        userHH = 00 # Changes hour to 00 when it rises above 23.

    formatTime = str(userHH).zfill(2) + ":" + str(userMM).zfill(2) + ":" + str(userSS).zfill(2)  # zfill used to pad leading zero to single digits.
    print(formatTime, end='\r') # end='\r' used to replace previous line
    userSS = int(userSS) + 1
    time.sleep(1)
