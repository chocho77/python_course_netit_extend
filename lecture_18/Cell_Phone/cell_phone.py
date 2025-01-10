from phone_battery import PhoneBattery
from phone_screen import PhoneScreen

class CellPhone:

    @staticmethod
    def nokia_n95():
        return CellPhone("N95", "Nokia", 2000, None, None)
    
    def __init__(self,
                 model="",
                 manufacturer="Nokia",
                 price=0,
                 owner="",
                 battery: PhoneBattery = None,
                 screen: PhoneScreen = None):
        self._model = model
        self._manufacturer = manufacturer
        self._price = price
        self._owner = owner
        self._battery = battery
        self._screen = screen

    @property
    def model(self):
        return self._model
    
    @property
    def battery(self):
        return self._battery
    
    @property
    def screen(self):
        return self._screen
    
    
        

    