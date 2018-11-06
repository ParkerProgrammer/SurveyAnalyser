surveyList = []
surveyInt = []

# Displays menu to user to select option
def menu():
    print("0 - Quit")
    print("1 - Display the menu")
    print("2 - Display all the survey information")
    print("3 - Given a department display the number of customers that answered the survey and the average result")
    print("4 - Display the department(s) with the highest customer satisfaction")
    print("5 - Display the department(s) with the lowest customer satisfaction")
    print("6 - Display the departments where 50% or more of the customers voted fair or poor.")
    print("7 - Display the departments where 60% or more of the customers voted good.")
    print("8 - Work out and display the number of people that have used the customer satisfaction devices and the average value.")
    thirdNum = int(input("Please select an option: "))
    if thirdNum == 0: # Ends survey by exiting loop
        print("Goodbye.")
    elif thirdNum == 1:
        menu()
    elif thirdNum == 2:
        displayData()
        menu()
    elif thirdNum == 3:
        calculateTotalByDepartment() 
        calculateAverageByDepartment()
        menu()
    elif thirdNum == 4:
        displayHighest()
        menu()
    elif thirdNum == 5:
        displayLowest()
        menu()
    elif thirdNum == 6:
        displayPoorPerformance()
        menu()
    elif thirdNum == 7:
        displayExcellentPerformance()
        menu()
    elif thirdNum == 8:
        calculateTotal()
        calculateAverage()
        menu()
    else:
        print("Option does not exist, please try again.") # Message notifying user of incorrect option entered
        menu()

# Reads data from the text file and stores into list
def readData():
    del surveyList[:]
    surveyFile = open("survey.txt","r")
    for line in surveyFile:
        line = line.rstrip("\n")
        line = line.split()
        surveyList.append(line)
    for num in surveyList:
        surveyInt.append(int(num[1]))
        surveyInt.append(int(num[2]))
        surveyInt.append(int(num[3]))
    surveyFile.close()
    print("Data has been read from text file.")
    return surveyList
    return surveyInt

# Displays the data stored in the list
def displayData():
    if surveyList == []:
        print("Empty list, please read data.")
    else:
        print(surveyList)

# Sums up the number of people who took the survey
def calculateTotal():
    print("Total number of people who took the survey:", (sum(surveyInt)))

# This function returns the average value of the survey
def calculateAverage():
    i = 0
    g = 1
    f = 2
    b = 3
    whole = 0
    for i in range (len(surveyList)):
        good = round(int(surveyList[i][g])) * 3
        fair = round(int(surveyList[i][f])) * 2
        poor = round(int(surveyList[i][b])) * 1
        whole += good + fair + poor
    toTal = (sum(surveyInt))
    averAge = whole / toTal
    print("Average value of the survey rounded is:", round(averAge))
        

# Sums up the number of people who took the survey per department
def calculateTotalByDepartment():
    print("Please select department for total number of votes")
    print("0 - Ladies")
    print("1 - Gentlemen")
    print("2 - Toys")
    print("3 - Beauty")
    print("4 - Technology")
    print("5 - Home")
    print("6 - Appliances")
    print("7 - Food")
    print("8 - Shoes")
    print("9 - Children")
    thirdNum = int(input("Please select an option: "))
    if thirdNum == 0:
        print("Number of people who took the survey:", (int(surveyList[0][1]) + int(surveyList[0][2]) + int(surveyList[0][3])))
    elif thirdNum == 1:
        print("Number of people who took the survey:", (int(surveyList[1][1]) + int(surveyList[1][2]) + int(surveyList[1][3])))
    elif thirdNum == 2:
        print("Number of people who took the survey:", (int(surveyList[2][1]) + int(surveyList[2][2]) + int(surveyList[2][3])))
    elif thirdNum == 3:
        print("Number of people who took the survey:", (int(surveyList[3][1]) + int(surveyList[3][2]) + int(surveyList[3][3])))
    elif thirdNum == 4:
        print("Number of people who took the survey:", (int(surveyList[4][1]) + int(surveyList[4][2]) + int(surveyList[4][3])))
    elif thirdNum == 5:
        print("Number of people who took the survey:", (int(surveyList[5][1]) + int(surveyList[5][2]) + int(surveyList[5][3])))
    elif thirdNum == 6:
        print("Number of people who took the survey:", (int(surveyList[6][1]) + int(surveyList[6][2]) + int(surveyList[6][3])))
    elif thirdNum == 7:
        print("Number of people who took the survey:", (int(surveyList[7][1]) + int(surveyList[7][2]) + int(surveyList[7][3])))
    elif thirdNum == 8:
        print("Number of people who took the survey:", (int(surveyList[8][1]) + int(surveyList[8][2]) + int(surveyList[8][3])))
    elif thirdNum == 9:
        print("Number of people who took the survey:", (int(surveyList[9][1]) + int(surveyList[9][2]) + int(surveyList[9][3])))
    else:
        print("Department does not exist, please try again.")
        calculateTotalByDepartment()

# Returns the average value per department
def calculateAverageByDepartment():
    print("Please select department for average value")
    print("0 - Ladies")
    print("1 - Gentlemen")
    print("2 - Toys")
    print("3 - Beauty")
    print("4 - Technology")
    print("5 - Home")
    print("6 - Appliances")
    print("7 - Food")
    print("8 - Shoes")
    print("9 - Children")
    thirdNum = int(input("Please select an option: "))
    if thirdNum == 0:
        whole = 0
        good = round(int(surveyList[0][1])) * 3
        fair = round(int(surveyList[0][2])) * 2
        poor = round(int(surveyList[0][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[0][1]) + int(surveyList[0][2]) + int(surveyList[0][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 1:
        whole = 0
        good = round(int(surveyList[1][1])) * 3
        fair = round(int(surveyList[1][2])) * 2
        poor = round(int(surveyList[1][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[1][1]) + int(surveyList[1][2]) + int(surveyList[1][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 2:
        whole = 0
        good = round(int(surveyList[2][1])) * 3
        fair = round(int(surveyList[2][2])) * 2
        poor = round(int(surveyList[2][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[2][1]) + int(surveyList[2][2]) + int(surveyList[2][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 3:
        whole = 0
        good = round(int(surveyList[3][1])) * 3
        fair = round(int(surveyList[3][2])) * 2
        poor = round(int(surveyList[3][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[3][1]) + int(surveyList[3][2]) + int(surveyList[3][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 4:
        whole = 0
        good = round(int(surveyList[4][1])) * 3
        fair = round(int(surveyList[4][2])) * 2
        poor = round(int(surveyList[4][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[4][1]) + int(surveyList[4][2]) + int(surveyList[4][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 5:
        whole = 0
        good = round(int(surveyList[5][1])) * 3
        fair = round(int(surveyList[5][2])) * 2
        poor = round(int(surveyList[5][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[5][1]) + int(surveyList[5][2]) + int(surveyList[5][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 6:
        whole = 0
        good = round(int(surveyList[6][1])) * 3
        fair = round(int(surveyList[6][2])) * 2
        poor = round(int(surveyList[6][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[6][1]) + int(surveyList[6][2]) + int(surveyList[6][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 7:
        whole = 0
        good = round(int(surveyList[7][1])) * 3
        fair = round(int(surveyList[7][2])) * 2
        poor = round(int(surveyList[7][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[7][1]) + int(surveyList[7][2]) + int(surveyList[7][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    elif thirdNum == 8:
        whole = 0
        good = round(int(surveyList[8][1])) * 3
        fair = round(int(surveyList[8][2])) * 2
        poor = round(int(surveyList[8][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[8][1]) + int(surveyList[8][2]) + int(surveyList[8][3]))
        print("Average value to the nearest whole number:", (round(avy)))
    elif thirdNum == 9:
        whole = 0
        good = round(int(surveyList[9][1])) * 3
        fair = round(int(surveyList[9][2])) * 2
        poor = round(int(surveyList[9][3])) * 1
        whole += good + fair + poor
        add = (int(surveyList[9][1]) + int(surveyList[9][2]) + int(surveyList[9][3]))
        averAge = whole / add
        print("Average value to the nearest whole number:", (round(averAge)))
    else:
        print("Department does not exist, please try again.")
        calculateAverageByDepartment()


# Displays department(s) with highest customer satisfaction
def displayHighest():
    i = 0
    b = 1
    n = 2
    g = 3
    for i in range (len(surveyList)):
        whole = int(surveyList[i][b]) + int(surveyList[i][2]) + int(surveyList[i][3])
        good = round(int(surveyList[i][b]) / whole * 100)
        fair = round(int(surveyList[i][n]) / whole * 100)
        poor = round(int(surveyList[i][g]) / whole * 100)
        poorAndFair = poor + fair
        if good > poorAndFair:
            print(surveyList[i][0], "has a high customer satisfaction rating:", str(good) + "%", "voted good,", str(fair) + "%", "voted fair and", str(poor) + "%", "voted poor.")

# Displays department(s) with lowest customer satisfaction
def displayLowest():
    i = 0
    b = 1
    n = 2
    g = 3
    for i in range (len(surveyList)):
        whole = int(surveyList[i][b]) + int(surveyList[i][2]) + int(surveyList[i][3])
        good = round(int(surveyList[i][b]) / whole * 100)
        fair = round(int(surveyList[i][n]) / whole * 100)
        poor = round(int(surveyList[i][g]) / whole * 100)
        if good < fair or good < poor:
            print(surveyList[i][0], "has a low customer satisfaction rating:", str(good) + "%", "voted good,", str(fair) + "%", "voted fair and", str(poor) + "%", "voted poor.")


# Displays departments with low survey rates of 50% or more of the customers that voted fair or poor
def displayPoorPerformance():
    i = 0
    b = 1
    n = 2
    g = 3
    for i in range (len(surveyList)):
        whole = int(surveyList[i][b]) + int(surveyList[i][2]) + int(surveyList[i][3])
        good = round(int(surveyList[i][b]) / whole * 100)
        fair = round(int(surveyList[i][n]) / whole * 100)
        poorAndfair = round(int(surveyList[i][g]) / whole * 100 + fair)
        if poorAndfair >= 50:
            print(surveyList[i][0], "department voted low,", str(poorAndfair) + "%", "having voted poor or fair.")


# Displays departments with excellent survey rates of 60% or more of the customers voted good.
def displayExcellentPerformance():
    i = 0
    b = 1
    n = 2
    g = 3
    for i in range (len(surveyList)):
        whole = int(surveyList[i][b]) + int(surveyList[i][2]) + int(surveyList[i][3])
        good = round(int(surveyList[i][b]) / whole * 100)
        if good >= 60:
            print(surveyList[i][0], "has a high survey rate", str(good) + "%", "good")
        else:
            print("No department displayed an excellent survey rate of 60% or more of the customers voting good.")
        break


readData()   
menu()

