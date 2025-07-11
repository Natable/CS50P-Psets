def main():
    mealTime = input("What time is it? ")
    hours = convert(mealTime)

    if hours >= 7.0 and hours <= 8.0:
        print("breakfast time")
    elif hours >= 12.0 and hours <= 13.0:
        print("lunch time")
    elif hours >= 18.0 and hours <= 19.0:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")

    fHours = float(hours)
    fMinutes = float(minutes)

    decimalHours = fHours + fMinutes / 60

    return decimalHours

if __name__ == "__main__":
    main()
