#Create a program that prints the multiplication table of a given number using a while loop.

table = int(input("Enter a number Multiplication table:"))
lines = int(input("Enter the number of lines:"))
i=1
while(i<=lines):
    print(f"{table}*{i}={table*i}")
    i+=1
    