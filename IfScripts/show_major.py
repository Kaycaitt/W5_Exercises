student_name = str(input("Please enter your name: "))
student_major = str(input("Please enter the student major code: ").upper())

if student_major == 'BIOL':
    print(f'''Name of Major: Biology
Department Office: Science Bldg, Room 310''')
elif student_major == 'CSCI':
    print(f'''Name of Major: Computer Science
Department Office: Sheppard Hall, Room 314''')
elif student_major == 'ENG':
    print(f'''Name of Major: English
Department Office: Kerr Hall, Room 201''')
elif student_major == 'HIST':
    print(f'''Name of Major: History
Department Office: Kerr Hall, Room 114''')
elif student_major == 'MKT':
    print(f'''Name of Major: Marketing
Department Office: Westly Hall, Room 310''')
else:
    print(f'''Name of Major: <unknown> 
Department Office: Nothing''')