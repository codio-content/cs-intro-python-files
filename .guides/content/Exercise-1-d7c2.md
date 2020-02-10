## Files Exercise 1

**Problem**
Write a program that reads a text file and returns the number of lines as well as the total number of characters in the file.

**Expected Output**
The first two lines of your code **must** look like this:

```python
import sys

test_file = sys.argv[1]
```
This allows for different text files to be sent to your program for testing. **Hint**, to open the file use `with open(test_file, "r"...`. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
4 lines
231 characters
```

<details><summary>**Where is the code visualizer?**</summary>Unfortunately, the code visualizer does not work with the `open` command, so it cannot be used for this problem.</details>

{try it}(python3 code/files/exercise1.py student_folder/.exercises/test1.txt)

{Check It!|assessment}(code-output-compare-3508746783)
