from phone_battery_type import BatteryType

class PhoneBattery:
    def __init__(self,
                 model,
                 idle_time,
                 hourse_talk,
                 type:BatteryType = BatteryType.UNKNOWN):
        self._model = model
        self._idle_time = idle_time
        self._hours_talk = hourse_talk
        self._type = type

    @property
    def model(self):
        return self._model
    
    @property
    def idle_time(self):
        return self._idle_time
    
    @property
    def hours_talk(self):
        return self._hours_talk
    
    @property
    def type(self):
        return self._type

