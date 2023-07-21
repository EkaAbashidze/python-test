def main():
    period = input("What time is it? ")
    time = convert(period)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else: 
        pass


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60 
    time = hours + minutes
    return time


if __name__ == "__main__":
    main()