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

def main():
    date = input("Date: ")
    
    if '/' in date:
        date = date.split("/")
        ordered_date = [date[2], f"{int(date[0]):02}", f"{int(date[1]):02}"]
        date = "-".join(ordered_date)
        print(date)
        
    for month in months:
        if month in date:
            date = date.split(", ")
            month_converted = date[0].split(" ")
            day = month_converted[1]s
            month_converted = month_converted[0]
            if month_converted.lower() == month.lower():
                month_formatted = f"{months.index(month_converted) + 1:02}"
            try:
                ordered_date = [date[1], month_formatted, day]
                date = "-".join(ordered_date)
                print(date)
            except UnboundLocalError:
                pass

main()