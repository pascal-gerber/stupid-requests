#isnumeric "requested by: Talentschool"

#requested code:

def askIfNumeric(text):
    isItNumeric = True
    allNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for everyLetter in text:
        if everyLetter not in allNumbers:
            isItNumeric = False
    return(isItNumeric)


print(askIfNumeric("69"), "requested")

#Horrible way
print("420".isnumeric(), "bad way")
