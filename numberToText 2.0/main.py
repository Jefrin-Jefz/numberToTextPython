import conversion

def printAnswer(theNumber , answerList):
    a=""
    for i in range(len(answerList)):
        a=a+answerList[i]
    a=a.capitalize()    
    print("\n{} is {}".format(theNumber,a))    

def wantToContinue():
    yesOrNo = input("\n Do you want to continue?   YES or No \n\t\t")
    yesOrNo = yesOrNo.upper()
    if yesOrNo == "YES":
        main()
    elif yesOrNo == "NO":
        quit()
    else:
        print("\nType in 'YES' or 'NO' to proceed : ")
        wantToContinue()


def main():
    while True:
        input_number=int(input("\nEnter the number : "))
        if input_number > 9999999:
            print("\nEnter a number in million range")
            continue
        break
    answerList = conversion.start_conversion(input_number)
    printAnswer(input_number , answerList)
    answerList.clear()
    wantToContinue()

    

main()