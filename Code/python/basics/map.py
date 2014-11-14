#!/usr/bin/python
 
def square(x):
    return x * x
 
def main():
    print map(square, range(20))
 
if __name__ == "__main__":
    main()
