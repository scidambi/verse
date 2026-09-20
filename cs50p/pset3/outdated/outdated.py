date = input("Date: ")
calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

day = int(date.split("/")[1])
month = int(date.split("/")[0])-1
year = int(date.split("/")[2])
print(day)
print(month)
print(year)

print(calendar[month])

print(f"{day}/{month}/{year}")