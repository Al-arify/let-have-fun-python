def convert_minutes(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    print(f"{minutes} min in sec is {seconds} and in hour is {hours}")

convert_minutes(30)