import random



# 1=red 2=2red 3=blue 4=2blue 5=white 6=black
wantedResult = {
    "red": 0,
    "blue": 0,
    "white": 0,
    "black": 0
}

inputString = input("Enter Values for [Red Blue White Black]\n")
inputString = inputString.split()
wantedResult["red"] = int(inputString[0])
wantedResult["blue"] = int(inputString[1])
wantedResult["white"] = int(inputString[2])
wantedResult["black"] = int(inputString[3])

print("Wanted: " + str(wantedResult))

successCounter = 0
failedCounter = 0
total = 10000

for k in range(total):


    result = {
        "red": 0,
        "blue": 0,
        "white": 0,
        "black": 0
    }

    diceAmount = 5
    nextDiceAmount = 5;
    for j in range(3):
        # set dice amount for this round
        diceAmount = nextDiceAmount
        nextDiceAmount = 0

        # roll the dice and add them to result or add them to next roll
        for i in range(diceAmount):
            
            x = random.randint(1, 6)
            #print(x)

            if x == 1 and wantedResult["red"] > result["red"]:
                result["red"] = result["red"] + 1;
            elif x == 2 and wantedResult["red"] > result["red"]:
                result["red"] = result["red"] + 2;
                if result["red"] > wantedResult["red"]:
                    result["red"] -= 1
            elif x == 3 and wantedResult["blue"] > result["blue"]:
                result["blue"] = result["blue"] + 1;
            elif x == 4 and wantedResult["blue"] > result["blue"]:
                result["blue"] = result["blue"] + 2;
                if result["blue"] > wantedResult["blue"]:
                    result["blue"] -= 1
            elif x == 5 and wantedResult["white"] > result["white"]:
                result["white"] = result["white"] + 1;
            elif x == 6 and wantedResult["black"] > result["black"]:
                result["black"] = result["black"] + 1;
            else:
                nextDiceAmount += 1;

        #print("Wanted: " + str(wantedResult))
        #print("Rolled: " + str(result))

    if wantedResult == result:
        #print("SUCCESS")
        successCounter += 1
    else:
        #print("FAILED")
        failedCounter += 1

print("Tries: " + str(total))
print("SUCCESSES: " + str(successCounter))
print("FAILS: " + str(failedCounter))
print("PERCENT: " + str(successCounter / total * 100) + " %")