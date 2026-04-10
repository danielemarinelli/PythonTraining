daynumber = int(input("Enter daynumber (1-7): "))

if daynumber == 1:
    print("Today it's sunday")
elif daynumber == 2:
    print("Today it's monday")
elif daynumber == 3:
    print("Today it's tuesday")
elif daynumber == 4:
    print("Today it's wednesday")
elif daynumber == 5:
    print("Today it's thursday")
elif daynumber == 6:
    print("Today it's friday")
elif daynumber == 7:
    print("Today it's saturday")
else:
    print("Invalid day number!!")

match daynumber:
    case 1: print("SUNDAY")
    case 2: print("MONDAY")
    case 3: print("TUESDAY")
    case 4: print("WEDNESDAY")
    case 5: print("THURSDAY")
    case 6: print("FRIDAY")
    case 7: print("SATURDAY")

match daynumber:
    case 2|3|4|5|6: print("weekday, go to work!!")
    case 1|7: print("enjoy weekend....")
    case _: print("Check again the number you inserted...")