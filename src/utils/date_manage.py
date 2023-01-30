from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



def get_date_now():
    return datetime.now()

def create_date(year, month, day):
    return datetime(year, month, day)

def get_day(date):
    return datetime.strftime(date, '%A')

#Last day month
def last_day_of_month(date):
    next_month = date.replace(day=28) + timedelta(days=4) # this will never fail return next_month - datetime.timedelta(days=next_month.day)
    return next_month - timedelta(days=next_month.day)



def get_presentation_date(enrollment_date, carnet_last_digit, poetry_genre):
    #Lyric, Epic, Drama, Saturday, Sunday

    if carnet_last_digit == '1' and poetry_genre == 'Drama':
        date = enrollment_date + timedelta(days=5)
        if get_day(date) == 'Saturday':
            date = enrollment_date + timedelta(days=2)
        elif get_day(date) == 'Sunday':
            date = enrollment_date + timedelta(days=1)
        return date


    elif carnet_last_digit == '3' and poetry_genre == 'Epic':
        date = last_day_of_month(enrollment_date)

        if get_day(date) == 'Saturday':
            date = date + timedelta(days=-1)
        elif get_day(date) == 'Sunday':
            date = date + timedelta(days=-2)
        
        return date


    day = enrollment_date.isoweekday()

    next_friday = None
    if day >= 5:
        next_week = enrollment_date + timedelta(weeks=1)
        days_to_friday = next_week.isoweekday()
        if days_to_friday > 5:
            days = (5 - int(days_to_friday))
            next_friday = next_week + timedelta(days=days)
            return next_friday

        return next_week
    

    next_friday = enrollment_date + timedelta(days = (5 - day))
    return next_friday

    

def get_age(year, month, day):
    date_born = datetime(year, month, day)
    age = relativedelta(get_date_now(), date_born)
    return int(age.years)

