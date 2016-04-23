## 1.0. Solution
The solution was developed and tested on Python version 2.7.9 and version 3.4.2 on Windows.


## 2.0. Execution
Simply open a console then type `python solution.py`. 
It expects that there is a folder named `data/` containing the JSON files in the current working directory.
The `data/` folder is included with the submission but you can change the path to a different folder on line 115.
The results will be printed to the screen.


## 3.0. Explanation
Although the instructions clearly stated that all 3-ples with "__a count of 5 or less__" should be removed, 
the results of running `solution.py` was:

```
[(u'airline', 150, 10)]
max: 150
min: 150
mean: 150
median: 150
```
which makes the statistical properties obtained somewhat useless since the same value was returned for each property.
...