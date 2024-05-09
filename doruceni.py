from workalendar.registry import registry
from workalendar.europe import CzechRepublic
from datetime import date, timedelta, datetime
import calendar
import locale

locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")
dateformat = '%d.%m.%Y'

def is_holiday_or_weekend(zacatek, delka):
    holidays = CzechRepublic().holidays(zacatek.year)
    konec = zacatek + delka
    if zacatek.year != konec.year:
        holidays += CzechRepublic().holidays(konec.year)
    while True:
        if konec.weekday() == 5 or konec.weekday() == 6 or konec in holidays:
            konec += timedelta(days=1)
        else:
            break
    return konec.strftime(dateformat + ' (%A)')

def main():
    zacatek = datetime.strptime(input("Zadejte datum zahájení běhu lhůty: "), dateformat)
    delka = timedelta(days=int(input("Zadejte délku lhůty v dnech: ")))
    print(is_holiday_or_weekend(zacatek, delka))

if __name__ == '__main__':
    main()
