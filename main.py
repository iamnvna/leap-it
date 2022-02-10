year = int(input("Enter a year: "))

try:
    val = int(year)
except ValueError:
    print("Enter a valid year!")

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")

# Commentary
'''
Line 1:
    Line one accepts user input (the year) from the user and
    casts it as an integer.

Line 3-6:
    Line 3 to 6 is a builtin error handling technique that runs
    or evaluates a piece of code and prints the appropriate code.

Line 8-13:
    This block of code iterates through if/elif/else statements
    and prints out the appropriate output based of the evaluations.
'''