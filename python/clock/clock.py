#create a clock function. ?
#must keep track of time, in hours and minutes, and be able to add or subtract minutes
#must handle roll-over and negative times

class Clock:
    def __init__(self, hours, minutes):
        self._hours = self._set_hours(hours)
        self._minutes = self._set_minutes(minutes)

    def _set_hours(self,hours):
        return hours%24

    def _set_minutes(self,minutes):
        if 0 <= minutes < 60:
            #minutes are 0 to 59, so don't affect the hours
            pass
        elif minutes >= 60:
            #more than an hour's worth of minutes, so need to account for roll-over
            self._hours = (self._hours + minutes//60)%24
        elif -60 < minutes < 0:
            #we've gone back less than one hour
            self._hours = (self._hours -1)%24
        else:
            #we've gone back more than one hour so:
            self._hours = (self._hours + self._ceildiv(minutes, 60) -1)%24
        return minutes%60

    def _ceildiv(self,a,b):
        #for use with negative minutes only
        return -(-a // b)

    def add(self,minutes):
        totmin = self._minutes + minutes
        self._minutes = self._set_minutes(totmin)
        return self

    def __str__(self):
        return '{0:02}:{1:02}'.format(self._hours,self._minutes)

    def __eq__(self,other):
        return self._hours == other._hours and self._minutes == other._minutes
