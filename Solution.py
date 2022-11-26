class Solution:
    def sumNumberInString(self, string):
        sum = 0
        for digit in string:
            if digit.isdigit():
                sum += int(digit)
        print(sum)

    def getLadderString(self, amountOfSteps):
        for i in range(amountOfSteps):
            print(" " * (amountOfSteps - 1 - i) + "#" * (i + 1))

    def to_json(func):
        changeableString = str(func())
        newString = changeableString.replace("\'","\"")
        print(newString)

    @to_json
    def get_data():
        return {
            "data": 42
        }


