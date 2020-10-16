----------

## Printing CSV Data

Previously, printing the contents of the CSV file would return lists of strings. This is not visually pleasing way of presenting the data. In the code below, `row` is a list. So you can reference each element with an index. This keeps Python from printing square brackets, quotation marks, etc. Instead, it prints just the contents of the CSV file.

```python
import csv

with open("student_folder/csv/home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row[0], row[1], row[2])
```

{try it}(python3 code/files/printing-csv.py 1)

|||challenge
## What happens if you:
* Add a space between each column of data:
`print(row[0], " ", row[1], " ", row[2])`
* Add a tab between each column of data:
`print(row[0], "\t", row[1], "\t", row[2])`
* Change the print statement to:
`print("{:<14} \t {:<9} \t {:^12}".format(row[0], row[1], row[2]))`

|||

<details>
  <summary><strong>What does <code>{:&lt;14}</code> mean?</strong></summary>
    Printing output that is aligned into columns may not work if you try to use just spaces and tabs to separate the columns. <code>{:&lt;14}</code> means left-justify the text and use a width of 14. 14 was chosen because that is the length of the longest names (Alex Rodriguez and Frank Robinson). Names shorter than 14 will "fill" the rest of the width with spaces. <code>{:&gt;14}</code> means the text will be right-justified with a width of 14. <code>{:^14}</code> means the text will be centered across 14 spaces. Note, the <code>format</code> method needs to be used when aligning text.
</details><br>

{try it}(python3 code/files/printing-csv.py 2)

## Unpacking 

In the code above, the variable `row` represents a list of data. The first element is the name of the player, the second element is the number of career home runs, and the third element states they are currently an active player. Python provides a way to take the descriptions of the each element and use it in the for loop.

![Unpacking CSV Info](.guides/images/unpacking-csv-info.png)

The for loop has three variables:`name`, `hr`, and `active`. The first variable, `name`, represents the first element in the list, the second variable, `hr`, represents the second element of the list, and the third variable, `active`, represents the third element. This is called unpacking.

```python
import csv

with open("student_folder/csv/home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader) #skip the header names
    for name, hr, active in reader:
        print("{} hit {} home runs.".format(name, hr))
```

{try it}(python3 code/files/printing-csv.py 3)

|||challenge
## What happens if you:
* Remove `next(reader)` from the program?
* Remove the variable `active`?

|||

{try it}(python3 code/files/printing-csv.py 4)

<details>
  <summary><strong>Unpacking and list length</strong></summary>
  Unpacking only works if you know how many elements are in the list. You must have the same number variables in the for loop as there are elements in the list. If you don't know how long a list is, you can always iterate over the list to access all of the elements.
</details>

{Check It!|assessment}(multiple-choice-3850148086)
