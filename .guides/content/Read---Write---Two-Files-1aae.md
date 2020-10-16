----------

## Read from One File and Write to Another

It is possible to open a file in read mode and another in write mode. Information can be passed from the reading file to the writing file. Like previous examples, `with open` will be used to open both files at once. The code below will open the file `read_practice` in read mode, create `destination.txt` in write mode, read the lines from the source file, and write these lines to the destination file. 

```python
with open("student_folder/text/read_practice.txt", "r") as source, open("student_folder/text/destination.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)
```

<details>
  <summary><strong><code>write</code> vs <code>writelines</code></strong></summary>
  In the code above the <code>write</code> method is being used to write text to a file. Previously, the method <code>writelines</code> was used to write text to a file. What's the difference? <code>writelines</code> can accept a single string or a list of strings as shown in previous lessons. <code>write</code>, however, can only accept a single string.
</details><br>

{try it}(python3 code/files/read-write-two-files.py 1)
[Open destination.txt](open_preview student_folder/text/destination.txt)

|||challenge
## What happens if you:
* Change the for loop to:
```python
for line in source.readlines():
    dest.write(line.upper())
```

* Change the for loop to:
```python
for line in source.readlines():
    line += "\n"
    dest.write(line)
```

|||

{try it}(python3 code/files/read-write-two-files.py 2)
[Open destination.txt](open_preview student_folder/text/destination.txt)

{Check It!|assessment}(fill-in-the-blanks-810907680)
