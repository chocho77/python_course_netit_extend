import unittest
from cell_phone import CellPhone
from phone_battery import PhoneBattery
from phone_screen import PhoneScreen
from phone_battery_type import BatteryType


class CellPhoneTest(unittest.TestCase):
    def test_battery(self):
       phone_baterry = PhoneBattery("551model", 160, 20)
       phone = CellPhone("Nokia", "3310", 110, "me", phone_baterry, None)
       self.assertEqual(phone.battery.model, "551model")
       self.assertEqual(phone.battery.idle_time, 160)
       self.assertEqual(phone.battery.hours_talk, 20)
      
    def test_screen(self):
         phone_screen = PhoneScreen(640,480,16_000_000)
         phone = CellPhone("Nokia", "3310", 110, "me", None,phone_screen)
         self.assertEqual(phone.screen.width, 640)
         self.assertEqual(phone.screen.height, 480)
         self.assertEqual(phone.screen.colors, 16_000_000)

    def  test_nokia_n95(self):
        phone = CellPhone.nokia_n95()
        self.assertEqual(phone.model, "N95")
        self.assertEqual(phone.manufacturer, "Nokia")
        self.assertEqual(str(phone), "Nokia N95")
    
    def test_cell_phone_battery_type(self):
        phone_baterry = PhoneBattery("551model", 160, 20,BatteryType.Li_ION)
        phone = CellPhone("Nokia", "3310", 110, "me", phone_baterry, None)
        self.assertEqual(phone.battery.type, BatteryType.Li_ION)
        self.assertEqual(phone.battery.type.value, "Li-Ion")
        self.assertEqual(phone.battery.type.name, "Li_ION")


if __name__ == '__main__':
    unittest.main()


