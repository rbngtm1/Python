# don't use global keyword inside function for defining global variables,
# instead use local variables, and parameters; see below eg:
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