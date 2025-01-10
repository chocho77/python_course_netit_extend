from typing import List
from phone_battery import PhoneBattery
from phone_screen import PhoneScreen
from  cell_phone_call import Call

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
        self._call_history = []

    def __str__(self) -> str:
        return f"{self._manufacturer} {self._model}"
    
    def call(self, to):
        print(f"Calling {to}")
        self._call_history.append(Call("me",to,"Today","An hour ago", 20))
 
    @property
    def model(self):
        return self._model
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def price(self):
        return self._price
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def battery(self):
        return self._battery
    
    @property
    def screen(self):
        return self._screen
    
    @property
    def type(self):
        return self._type
    
    @property
    def call_history(self) -> List[Call]:
        return self._call_history
    
    
        

    