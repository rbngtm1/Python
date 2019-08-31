#### Set file location
  * On windows, open ("C:\\Users\\UserName\\Folder\\test.txt")
  * On MacOs or Linux, ("/Users/YourUserName/Folder/myfile.txt")

#### Alternative for closing file
  * When you open a file let's say, myfile = open('myfile.txt') , in order for it to access it later you need to close it with myfile.close() because it is kind of moving cursor towards end of your content in file. Best way is below:
  * with open('myfile.txt') as my_new_file:
  *     contents = my_new_file.read()
#### Using mode, inside open function, by default the value is read.
```
 df
 \asd
```
   
  
  
