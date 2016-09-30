#calculate meet-up date given nth day of the week for a given month and year:
#e.g. 1st Monday of February 2012 = 06/02/2012
#a "teenth" day of the week refers to 13th-19th of the month.

from datetime import date, timedelta

day_to_num = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
pos_to_num = {'1st':0,'2nd':7,'3rd':14,'4th':21,'5th':28,'last':-1,}

class MeetupDayException(Exception):
    pass

def max_days(year,month):
    m_len = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and (year%4 == 0 and year%100 != 0 or year%400 == 0):
        return 29
    else:
        return m_len[month-1]

def meetup_day(m_year,m_month,m_day,m_pos):
    day = day_to_num[m_day]
    offset = 0
    if m_pos != 'teenth':
        offset = pos_to_num[m_pos]
        if offset >= 0:
            start_date = date(m_year,m_month,1)
            delta = (day - start_date.weekday())%7 + offset
            if delta + 1 > max_days(m_year,m_month):
                raise MeetupDayException('Meetup day is not possible')
            else:
                return start_date + timedelta(days= delta)
        else:
            end_date = date(m_year,m_month,max_days(m_year,m_month))
            return end_date - timedelta(days=(end_date.weekday() - day)%7)
    else:
        teenth_date = date(m_year,m_month,13)
        return teenth_date + timedelta(days=(day - teenth_date.weekday())%7)
