def time_of_day(h):
    if 6 <= h < 12:
        return "Утро"
    if 12 <= h < 18:
        return "День"
    if 18 <= h < 24:
        return "Вечер"
    else:
        return "Ночь"


print(time_of_day(10))
