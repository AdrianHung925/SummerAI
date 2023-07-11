#task 1
hours = int(input("Input the number of hours"))
minutes = hours * 60
print("That is ",minutes,"minutes")

#task 2
timeChosen = False
hour = False
minute = False
while timeChosen == False:
    timeChoice = int(input("Enter the number for your selection:\n1. Minute to Hours\n2. Hours to Minute\n"))
    if timeChoice == 1 or timeChoice == 2:
        timeChosen = True
        if timeChoice == 1:
            minute = True
        else:
            hour = True
    else:
        print("Invalid Input\n")
if minute == True:
    time = float(input("Input the number of minutes you would like to convert to hours "))
    time = round(time/60)
    print("The number of hours are",time)
else:
    time = float(input("Input the number of hours you would like to convert to minutes "))
    time = round(time*60)
print("The number of minutes are",time)

#task 3
word = str(input("Type in the word you want to check the length of "))
num = len(word)
print("The number of letters in that word is",num)

#without verification