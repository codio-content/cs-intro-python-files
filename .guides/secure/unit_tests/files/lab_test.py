import os
import subprocess
import sys

path = "code/files"
file = "lab-challenge.py"
student_code = os.path.join(path, file)

def reads_file(file):
  """Does the program read the text file"""
  read_command = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if ", 'r'" in line or ', "r"' in line and 'with' in line and 'open' in line:
        read_command = True
    
  return read_command

def check_output(file):
  """Checks output of student code"""
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == """Myanmar is a country in Southeast Asia.
The capital of Myanmar is Naypyidaw.
Its population is about 54 million people.
Myanmar is a former British colony.""":
    return True
  else:
    return False
  
def replaces_word(file):
  """Does student code replace Burma"""
  has_replace = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if ".replace" in line:
        has_replace = True
    
  return has_replace
  
if not reads_file(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not open the file in read mode.")

if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print the correct output.")

if not replaces_word(student_code):
  print("<h2>Test did not pass</h2>")
  print("Did not use 'replace' to substitute 'Myanmar' for 'Burma'.")

if check_output(student_code) and reads_file(student_code) and replaces_word(student_code):
  print("<h2>All tests passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)
