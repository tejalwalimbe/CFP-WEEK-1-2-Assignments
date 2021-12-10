# Check Leap Year
#input
year = int(input("Enter Year: "))
#condition
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")

