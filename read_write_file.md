#### Set file location
  * On windows, open ("C:\\Users\\UserName\\Folder\\test.txt")
  * On MacOs or Linux, ("/Users/YourUserName/Folder/myfile.txt")

#### Alternative for closing file
  * When you open a file let's say, myfile = open('myfile.txt') , in order for it to access it later you need to close it with myfile.close() because it is kind of moving cursor towards end of your content in file. Best way is below:
```
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
```
#### Using mode, inside open function, by default the value is read.
  * Reading, Writing, Appending Modes
    * mode = 'r' is read only
    * mode = 'w' is write only (will overwrite files or create new)
    * mode = 'a' is append only (will add on to files)
    * mode = 'r+' is reading and writing
    * mode = 'w+' is writing and reading (overwrites existing files or creates a new file)
#### Add on to existing file 
    
```
with open ('my_new_file.txt', mode = 'a') as f:
    f.write('random lines')
```
   
#### Only Write modes creates a new file even if you don't have any
```
with open('blabla.txt', mode='w') as f:
    f.write('I just created a new file')
```
  
