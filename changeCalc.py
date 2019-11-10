import time
def cc(cost, paid):
    change = round(paid - cost,2)
    # adding one line of code to assign 'change' variable the attributes paid - cost
    numberQuarters = change // 0.25
    print(" ")
    time.sleep(.1)
    print("Your total purchase is ${}.".format(round((cost),2)))
    time.sleep(.4)
    print("You have made a payment of ${}.".format(round((paid),2)))
    time.sleep(.65)
    print(" ")
    print("Your change is ${}, or:".format(round(change,2)))
    print(" ")
    time.sleep(1.2)
    if numberQuarters >= 1:
        print("{} quarters".format(int(numberQuarters)))
        costQuarters = numberQuarters * 0.25
        changeQuarters = round(change - costQuarters, 2)
        numberDimes = changeQuarters // 0.10
        if numberDimes >= 1:
            print("{} dimes".format(int(numberDimes)))
            costDimes = numberDimes * 0.10
            changeDimes = round(changeQuarters - costDimes, 2)
            numberNickels = changeDimes // 0.05
            if numberNickels >= 1:
                print("{} nickels".format(int(numberNickels)))
                costNickels = numberNickels * 0.05
                changeNickels = round(changeDimes - costNickels, 2)
                numberPennies = changeNickels / 0.01
                if numberPennies >= 1:
                    print("{} pennies".format(int(numberPennies)))
            else:
                numberPennies = round(changeDimes / 0.01, 2)
                if numberPennies >= 1:
                    print("{} pennies".format(int(numberPennies)))
        elif changeQuarters // 0.05 >= 1:
            print("{} nickels".format(int(changeQuarters // 0.05)))
            costNickels = round((changeQuarters // 0.05) * 0.05, 2)
            changeNickels = round(changeQuarters - costNickels, 2)
            numberPennies = changeNickels / 0.01
            if numberPennies >= 1:
                print("{} pennies".format(int(numberPennies)))
        else:
            numberPennies = changeQuarters / 0.01
            if numberPennies >= 1:
                print("{} pennies".format(int(numberPennies)))
    # 10c
    elif change // 0.10 >= 1:
        print("{} dimes".format(int(change // 0.10)))
        costDimes = (change // 0.10) * 0.10
        changeDimes = round(change - costDimes, 2)
        numberNickels = changeDimes // 0.05
        if numberNickels >= 1:
            print("{} nickels".format(int(numberNickels)))
            costNickels = numberNickels * 0.05
            changeNickels = round(changeDimes - costNickels, 2)
            numberPennies = changeNickels / 0.01
            if numberPennies >= 1:
                print("{} pennies".format(int(numberPennies)))
        else:
            numberPennies = round(changeDimes / 0.01, 2)
            if numberPennies >= 1:
                print("{} pennies".format(int(numberPennies)))
    elif change // 0.05 >= 1:
        print("{} nickels".format(int(change // 0.05)))
        costNickels = (change // 0.05) * 0.05
        changeNickels = change - costNickels
        numberPennies = changeNickels / 0.01
        if numberPennies >= 1:
            print("{} pennies".format(int(numberPennies)))
    else:
        numberPennies = change / 0.01
        if numberPennies >= 1:
            print("{} pennies".format(int(numberPennies)))