from pathlib import Path
filepath = r"/home/chavdar/python_course_netit/lecture_21/Hello.txt"
file_obj = Path(filepath)

if file_obj.exists():
    with open("Hello.txt", "a") as f:
        f.write("Hello, python!")
    

