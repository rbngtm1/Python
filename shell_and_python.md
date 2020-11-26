### Get current working dir in python
```py
Import os
print(os.getcwd())
```
### list files and directory in cwd
```py
os.listdir()
```
### list only hidden files
```py
os.listdir(‘.’)
```
### list files and folder ignoring hidden files
```py
[f for f in os.listdir() if not f.startswith('.')]
```
### list only files in cwd ignoring hidden files
```py
[f for f in os.listdir() if os.path.isfile(f) and not f.startswith('.')]
```

* Replace isfile to isdir for directory

### Change the directory
```py
os.chdir('workspace’)   -> will switch the directory	to workspace dir.
```
# list only yml files in cwd
```py
[f for f in os.listdir() if f.endswith('.yml')]
```
# Copy files in python
```py
from shutil import copyfile
copyfile(‘my_stock_earning.xlsx', '/Users/rbngtm1/earning.xlsx')
```
To copy file permissions and metadata, use copy2
```py
import shutil
shutil.copy2(‘src’, ’dest’)
```
* Copies from source to destination

### Move a file by renaming it's path
```py
os.rename(’src’, ‘dest’)
```
### Move a file from the directory d1 to d2
```py
shutil.move(‘src’, ’dest’)
```


### Delete file.txt
```py
os.remove('/Users/rbngtm1/file.txt')
```
### Write to a file
```py
file1 = open("myfile.txt","w") 
file1.write("Hello \n") 
file1.close
```

### Write multiple lines to a file (Note you must open a file to write or read a file)
```py
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
file1.write(L)

# Read a file
file1 = open("myfile.txt","r+")  
file1.seek(0)    -> move cursor back to start of file

# Read a file in list
file1.readlines()
```
### Whenever you open a file, you must close it. But using “with” statement, python automatically closes the file. 

```py
with open(filename,'r') as fh
     all_lines = fh.readlines()
```
### To run linux commands using python
```py
os.system(‘ls -lart’)
```
But it’s recommended to use subprocess module

### we can use the Popen() command of the subprocess Module. By using Popen() we are capable to get the output of the script:
```py
import subprocess
x = subprocess.Popen(['ls', '-lart'])
```
### The shell command cp -r xyz abc can be send to the shell from Python by using the Popen() method of the subprocess-Module in the following way:
```py
p = subprocess.Popen(['cp','-r', “test.txt”, “mytest.png"])

Another way  is to use shell=True
x = subprocess.Popen('ls -lart', shell=True)

As we have mentioned above, it is also possible to catch the output from the shell command or shell script into Python. To do this, we have to set the optional parameter stdout of Popen() to subprocess.PIPE

process = subprocess.Popen(['ls','-l'], stdout=subprocess.PIPE)
directory_content = process.stdout.readlines()
print(directory_content)

Here you are getting b for bytes, rather than string of unicode characters.

You can use decode() method to get rid of it
directory_content = [el.decode() for el in directory_content]
print(directory_content)
```
### See this link for more description
  * https://www.python-course.eu/os_module_shell.php
