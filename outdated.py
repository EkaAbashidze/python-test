date = input("Date: ")

months = [
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

if '/' in date:
    date = date.split("/")
    orderedDate = [date[2], f"{int(date[0]):02}", f"{int(date[1]):02}"]
    date = "/".join(orderedDate)

for month in months:
    if month in date:
        date = date.split(", ")
        monthConverted = date[0].split(" ")
        day = monthConverted[1]
        monthConverted = monthConverted[0]
        if monthConverted == month:
            monthFormatted = f"{months.index(monthConverted) + 1:02}"
        orderedDate = [date[1], monthFormatted, day]
        date = "/".join(orderedDate)
        print("ordered date:", date)

print(date)