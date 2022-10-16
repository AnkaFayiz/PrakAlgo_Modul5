import sys

if __name__ == '__main__':
    print("This program will determine the number of days of a given month")
    
    while True:
        print("Enter -1 to stop the program")
        month = int(input("Enter the month (1 - 12) : "))
        if month > 12:
            print("* Invalid value entered: {}".format(month))
        elif month == -1:
            print("Thank You!")
            sys.exit()
        
        if month % 2 == 0 and month != 2:
            print("There are 30 days in the month")
        elif month % 2 != 0:
            print("There are 31 days in the month")
        
        if month == 2:
            februaryKabisat = int(input("Please enter the year (e.g., 2021) : "))

            if (februaryKabisat % 4) == 0:
                if (februaryKabisat % 100) == 0:
                    if (februaryKabisat % 400) == 0:
                        print("There are 29 days in the month")
                    else:
                        print("There are 28 days in the month")
                else:
                    print("There are 29 days in the month")
            else:
                print("There are 28 days in the month")
