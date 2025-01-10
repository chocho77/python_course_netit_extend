import unittest
from cell_phone import CellPhone
from phone_battery import PhoneBattery
from phone_screen import PhoneScreen


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



if __name__ == '__main__':
    unittest.main()


