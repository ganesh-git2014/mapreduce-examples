#!/usr/bin/python
 
def add(x, y):
    return x + y
 
def main():
    print reduce(add, range(20))
 
if __name__ == "__main__":
    main()
