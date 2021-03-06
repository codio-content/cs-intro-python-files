import os
import subprocess
import sys

path = "code/fundamentals"
file = "exercise4.py"
student_code = os.path.join(path, file)

def check_variable(file):
  correct_var = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if line.find("my_float") != -1:
        correct_var = True
    
  return correct_var

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "3.0":
    return True
  else:
    return False

if check_variable(student_code):
  if check_output(student_code):
    print("<h2>Test passed!</h2>")
    sys.exit(0)
  else:
    print("<h2>Test did not pass</h2>")
    print("Program did not print '3.0'")
    sys.exit(1)
else:
  print("<h2>Test did not pass</h2>")
  print("Variable was not properly named 'my_float'")
  sys.exit(1)
