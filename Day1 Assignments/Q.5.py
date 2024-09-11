#Create a program that checks if a given year is a leap year.

n = int(input("Enter a year to check for leap year:"))

if((n%4==0 and n%100 !=0) or n%400 ==0):
        print("It is a leap year")
else:
    print("It is not a leap year")