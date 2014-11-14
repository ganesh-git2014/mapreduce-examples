#!/usr/bin/python
 
def square(x):
    return x * x
 
def add(x, y):
    return x + y
 
def main():
    print reduce(add, map(square, range(20)))
 
if __name__ == "__main__":
    main()
