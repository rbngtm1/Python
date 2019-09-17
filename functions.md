#### Functions
```
def testfunc():
    a = 10
    b = 20
    c = 30
    print("the value of a is:", a, b, c)
    return a, b, c

def testagain(*numbers):
    total = sum(numbers)
    print("total is", total)
    return total

def main():
    a, y, z = testfunc()
    testagain(a, y, z)
main()

```
#### OUTPUT
the value of a is: 10 20 30
total is 60

=====================================
```
def lambda_test():
    print("blabla")
    a=5
    return a

def add(num):
    b=10
    sum=num+b
    print(sum)

def main():
    x=lambda_test()
    add(x)
main()
```
#### OUTPUT
blabla
15
