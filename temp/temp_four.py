width = 15
name = "Chavdar"
name_one = "Mom"

delta = len(name) - len(name_one)
space_btn = " " * width
space_btn_one = " " * (width + delta)
print(f"{name} {space_btn} {name}")
print(f"{name_one} {space_btn_one} {name_one}")
