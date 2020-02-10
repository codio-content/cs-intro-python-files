## Files Exercise 5

**Problem**
Write a program that reads a comma delimited CSV file and prints all of the cities which reside in the Southern Hemisphere. **Note**, any latitude with a negative value is south of the equator.

**Expected Output**
The CSV file will look something like the one below. **Note**, there will be a row with header titles.

|City |Country |Latitude |Longitude |
|-----|--------|:-------:|:--------:|
|Beijing|China|39|116
|Perth|Australia|-57|115|
|Port Moresby|Papua New Guinea|-25|147|
|Tokyo|Japan|35|139|

The first two lines of your code **must** look like this:

```python
import sys, csv

test_file = sys.argv[1]
```
This allows for different text files to be sent to your program for testing. **Hint**, to open the file use `with open(test_file, "r"...`. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
The following cities are in the Southern Hemisphere: Perth, Port Moresby.
```

<details><summary>**Where is the code visualizer?**</summary>Unfortunately, the code visualizer does not work with the `open` command, so it cannot be used for this problem.</details>

{try it}(python3 code/files/exercise5.py student_folder/.exercises/test5.csv)

{Check It!|assessment}(code-output-compare-4037337142)
