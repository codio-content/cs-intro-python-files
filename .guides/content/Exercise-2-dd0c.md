## Files Exercise 2

**Problem**
Write a program that reads a comma delimited CSV file with four columns and returns the average of each column in the file.

**Expected Output**
The first two lines of your code **must** look like this:

```python
import sys

test_file = sys.argv[1]
```

This allows for different text files to be sent to your program for testing. **Hint**, to open the file use `with open(test_file, "r"...`. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
10.0 8.0 6.0 20.0
```

<details>
  <summary><strong>Where is the code visualizer?</strong></summary>
  Unfortunately, the code visualizer does not work with the <code>open</code> command, so it cannot be used for this problem.
</details><br>

{try it}(python3 code/files/exercise2.py student_folder/.exercises/test2.csv)

{Check It!|assessment}(code-output-compare-3072203434)
