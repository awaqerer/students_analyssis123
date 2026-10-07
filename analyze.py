import csv
INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
dict = {}
avarage_math = 0
avarage_python = 0
avarage_eng = 0
line_count = 0
best_gpa = 0
best_student = ""
with open("students.csv", "r") as f:
    next(f)

    for line in f:
        line = line.strip("\n")
        line = line.split(",")
        avarage_math += int(line[1])
        avarage_python += int(line[2])
        avarage_eng += int(line[3])
        dict[line[0]] = round( ((int(line[1])+int(line[2])+int(line[3])) / 3), 3)
        line_count += 1

    best_gpa = max(dict.values())
    for key, value in dict.items():
        if dict[key] == best_gpa:
            best_student = key

    avarage_math = round(avarage_math/line_count,3)
    avarage_python =round( avarage_python/line_count,3)
    avarage_eng = round(avarage_eng/line_count,3)
with open(OUTPUT_FILE,"w") as f:
    f.write(f"Середній бал по класу:"+ "\n")
    f.write(f"math:  {round(avarage_math,1)}" + "\n")
    f.write(f"python:  {round(avarage_python,1)}" + "\n")
    f.write(f"english:  {round(avarage_eng,1)}"+ "\n")
    f.write(f" Найкращий студент: {best_student} ({best_gpa})"  + "\n")
    print(f"Середній бал по класу:")
    print(f"math:  {round(avarage_math,1)}")
    print(f"python:  {round(avarage_python,1)}" )
    print(f"english:  {round(avarage_eng,1)}")
    print(f" Найкращий студент: {best_student} ({best_gpa})")