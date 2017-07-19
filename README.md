# Assignments for Chapter 4 of Summer App Space Curriculum
## `Problem1_Testing.py`
### PART 1:
* Run the code, save the file, exit, then execute from the bash console:
```python3.5 Problem1_Testing.py```
  * You WILL get a crash. We will fix this as an exercise in PART 3.

### PART 2:
* Wrap the entire code after the imports in a try/except block. 
* The exception should print the error and then on a new line "still working on it"

### PART 3: 
Currently as of 7/19/17 there is no crash because the data is back online! This part was to illustrate what to do if the DATA_URL changes. If you don't get a crash your first run, change the DATA_URL to something that doesn't exist and reinstall `astroML` so that you do get a crash. Then change it back and reinstall. You've practiced fixing a crash in a python module!
 There is something wrong with the astroML package that is causing it to crash! We will fix this error and then try again
* A) Go to the directory astroML in which the git respository is located for the code. Go to the subdirectory datasets.
  * open the file sdss_specgals.py and edit the DATA_URL tuple to be correct
* B) Reinstall astroML by executing on the bash console:
```python3.5 setup.py install --user```
* C) Execute this file again. Look at the image that the code prints out.

### PART 4:
* A) Put all the code after the imports in a function that takes a single argument, the projection
* B) Add documentation to your function indicating what values of the projection are allowed. Options are: 'hammer', 'aitoff', 'mollweide', 'lambert'
* C) Call your new function with each projection one at a time, verify it is working
* D) Change your function to change the name of the figure depending on the projection, so that when you call it 4 times you get 4 figures
* E) Add an assertion to check to make sure that the projection is one of the options
* F) Call your function with the argument "sillyprojection" and verify your assertion cause the code to crash
# `Problem2_MoreFunctions.py`
 Put all the code inside a function, with the name of your choice
* A) put all of this code into a function that takes a few arguments, namely the marker, markersize, lignstyle and color call this function plot_quasars
* B)  have all the arguments be default arguments set to the defaults that they are within plot currently.
* C) change the name of the figure depending on the combination of arguments given so that with each combination a new figure name is produced
* D) Try this out with many different combinations of arguments. Research the plot command to try to change the marker, markersize, linestyle, etc. appropriately
# `Problem3_UsingHandwrittenModules.py`
 Using your own module
* A) Creating your module: Good news! We are already done with this, it is our code in problem 2!
* B) Import the function plot_quasars from your module
* C) Using your module: go ahead an use plot_quasars here.
 NOTE: if your module wasn't in the same directory as the directory from which you run the python interpreter, you will have to make sure the directory it is in is on the PYTHONPATH
# `Problem4_PythonScript.py`
* A) You will need to install healpy from the bash console with `pip3.5 install --user healpy`
  * This installation may fail. It is common for software you work with to fail in its automatic install.
  * See if you can debug the failure. Ask for help and ideas. Hint: put -v after install to get a verbose output
  * If there is a requirement that is not being satisfied, consider downloading and building it yourself. You may need some additional bash commands to unpack the software and some hints for building it. When you get stuck ask
  * When you build software yourself ask for some advice or look up in the README. If you get stuck, ask.
* B) Next run the code
* C) Put the body of the code in a function that has one parameter: the title of the plot. Give this parameter a default equal to the current plot title
* D) Practice calling your function.
* E) Use sys.argv (don't forget to import sys first) to access arguments from the commandline. When the function is called as a script, require one argument the plot title, and access it with sys.argv
* F) Now make the argument on the commandline optional.
