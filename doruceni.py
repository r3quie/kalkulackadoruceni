from workalendar.registry import registry
from workalendar.europe import CzechRepublic
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import calendar
#import locale

#locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")
dateformat = '%d.%m.%Y'

def is_holiday_or_weekend(zacatek: datetime, delka: timedelta):
    holidays = CzechRepublic().holidays(zacatek.year)
    konec = datetime.date(zacatek + delka)
    if zacatek.year != konec.year:
        holidays += CzechRepublic().holidays(konec.year)
    while True:
        if konec.weekday() == 5 or konec.weekday() == 6 or konec in list(zip(*holidays))[0]:
            konec += timedelta(days=1)
        else:
            break
    return konec.strftime(dateformat + ' (%A)')

def get_time(gotten: str, delka: int):
    if gotten == 'd':
        return timedelta(days=delka)
    elif gotten == 'm':
        return relativedelta(months=delka)
    elif gotten == 'r':
        return relativedelta(years=delka)
    else:
        print("Neplatná jednotka času.")
        return get_time()

def main():
    zacatek = datetime.strptime(input("Zadejte datum zahájení běhu lhůty: "), dateformat)
    delka = get_time(input("Zadejte jednotku času (d/m/r): "), int(input("Zadejte délku lhůty: ")))
    print(is_holiday_or_weekend(zacatek, delka))
        

if __name__ == '__main__':
    main()
