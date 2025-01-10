from phone_battery import PhoneBattery
from phone_screen import PhoneScreen

class CellPhone:
    def __init__(self,
                 model,
                 manufacturer,
                 price,
                 owner,
                 battery: PhoneBattery,
                 screen: PhoneScreen):
        self._model = model
        self._manufacturer = manufacturer
        self._price = price
        self._owner = owner
        self._battery = battery
        self._screen = screen

    @property
    def battery(self):
        return self._battery
    
    @property
    def screen(self):
        return self._screen
    
    
        

    