## Final Project Report: Software Quality Assurance

# 1
Unpacked MLForensics.zip.

# 2
Created this repository and put the contents of MLForensics.zip into it

# 3
Created README.md and displayed our team members

# 4a
A pre-commit git hook was created that confirms any commit made to the repository. We weren't sure how to confirm that the hook was working correctly, so we had to ask the professor and he told us to output it to a text file. Getting the ouput to a text file was a bit confusing at first, but we were able to modify the existing code.
We have learned the importance and usefulness of looking over changes and additions before making them permanent.

# 4b
Fuzz methods were created to test the Average, Median, reportProp, and reportDensity methods in report.py and the reportProportion in frequency.py. The main focus was to test and catch invalid inputs into these methods.
By working with fuzzing we have learned how important it is to catch errors and examine edge cases in code.

# 4c
Lots of files from the MLForensics folder had indention errors, so we put all of our forensics into the methods of the main.py file. Since the paths in the main method for main.py were not the paths to directories on our local machines, so our forensics outputs are not listed in this repository. However, all the methods on the main.py have logging functions in them.
Forensics is important because it allows us to carefully observe and log our code. Through doing these assignments we have learned how to better investigate our code.

# 4d
Implemented continuous integration with codacy at codacy-analysis.yaml. The first couple of times it ran, it took a bit longer than we expected it to, but after a couple more tries, we were able to see that it ran successfully.
Using codacy we have learned the value of tools that provide quality analysis and static integration. We will be using tools like this in the future.
