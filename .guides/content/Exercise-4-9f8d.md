## Files Exercise 4

**Problem**
Write a program that reads a tab delimited CSV file and prints the name of the oldest person in the file.

**Expected Output**
The CSV file will look something like the one below. **Note**, there will be a row with header titles.

|Name |Age |Career|
|-----|:--:|------|
|Peter|38  |Doctor|
|Paul |41  |Lawyer|
|Mary |32  |Systems Engineer|

The first two lines of your code **must** look like this:

```python
import sys, csv

test_file = sys.argv[1]
```
This allows for different text files to be sent to your program for testing. **Hint**, to open the file use `with open(test_file, "r"...`. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
The oldest person is Paul.
```

<details><summary>**Where is the code visualizer?**</summary>Unfortunately, the code visualizer does not work with the `open` command, so it cannot be used for this problem.</details>

{try it}(python3 code/files/exercise4.py student_folder/.exercises/test4.csv)

{Check It!|assessment}(code-output-compare-135786605)
