name = "name"
name_one = "name_one"
name_two = "name_two"
name_three = "name_three"

space_btn = " " * 15
space_text = " " * 50
space_btn_one = " " * (15 - len(name))
space_text_one = " " * (50 - 2 * len(name))
space_btn_two = " " * (15 - len(name) - 2)
space_text_two = " " * (48 - 2 * len(name))
space_btn_three = " " * (17 - len(name))

print(f"{name} {space_btn} {name} {space_text} {name} {space_btn} {name}")
print(f"{name_one} {space_btn_one} {name_one} {space_text_one} {name_one} {space_btn} {name_one}")
print(f"{name_two} {space_btn_one} {name_two} {space_text_one} {name_two} {space_btn} {name_two}")
print(f"{name_three} {space_btn_two} {name_three} {space_text_two} {name_three} {space_btn_three} {name_three}")