# declaring the function convert to days
def convert_to_days():
    hours = int(input("Please enter the number of hours: "))
    minutes = int(input("Please enter the number of minutes: "))
    seconds = int(input("Please enter the number of seconds: "))

    def get_days():  # helper function get days to convert the values into days
        hrs = hours/24  # convert the inputted hours into days in float
        mins = minutes/1440  # convert the inputted minutes into days in float
        secs = seconds/86400  # convert the inputted seconds into days in float
        return hrs + mins + secs  # sum of converted hours, minutes, seconds into days
    return get_days()


days = round(convert_to_days(), 4)  # round days with 4 digits after decimal point
print(days)
