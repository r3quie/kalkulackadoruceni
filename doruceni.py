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
    return konec

def get_time(gotten: str, delka: int):
    if gotten == 'd':
        return timedelta(days=delka)
    elif gotten == 'm':
        return relativedelta(months=delka)
    elif gotten == 'r':
        return relativedelta(years=delka)
    else:
        print("Neplatná jednotka času.")
        return False
    
def pravni_moc(posledni_den: datetime):
    return posledni_den + timedelta(days=1)

def export_handle(zacatek, delka):
    konec = is_holiday_or_weekend(zacatek, delka)
    return konec.strftime(dateformat + ' (%A)'), pravni_moc(konec).strftime(dateformat + ' (%A)')

def input_delka():
    while True:
        gotten = input("Zadejte jednotku času (d/m/r): ")
        while True:
            delka = int(input("Zadejte délku lhůty: ")) # nedává tady smysl definovat jako int, když zkoušíš ValueError až potom, ValueError dostaneš už tady, chceš try: teprve tohle
            try:
                delka = get_time(gotten, delka)
                if delka is not False:
                    return delka
                else:
                    break
            except ValueError:
                print("Neplatná délka lhůty.")


def main():
    zacatek = datetime.strptime(input("Zadejte datum zahájení běhu lhůty: "), dateformat)
    delka = input_delka()
    posledni_den, dpravni_moc = export_handle(zacatek, delka)
    print(f"Poslední den lhůty bude {posledni_den}.")
    print(f"X nabude právní moci {dpravni_moc}.")

        

if __name__ == '__main__':
    main()
