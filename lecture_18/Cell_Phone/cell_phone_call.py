class Call:
    def __init__(self,
                 _from,
                 to,
                 date,
                 time,
                 duration):
        self._from = _from
        self._to = to
        self._date = date
        self._time = time
        self._duration = duration
    
    @property
    def caller(self):
        return self._from
    
    @property
    def to(self):
        return self._to
    
    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time
    
    @property
    def duration(self):
        return self._duration

    

