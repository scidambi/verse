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

while True:
    try:
        date = input("Date: ")
        day = int(date.split("/")[1])
        month = int(date.split("/")[0])-1
        year = int(date.split("/")[2])

        print(f"{year}-{month+1:02}-{day:02}")
        break
    except: 
        try:
            year = int(date.split()[2])
            day = int(date.split()[1].replace(",",""))
            month = date.split()[0]
            month_english = calendar.index(month)+1

            print(f"{year}-{month_english:02}-{day:02}")
            break
        except:
            continue