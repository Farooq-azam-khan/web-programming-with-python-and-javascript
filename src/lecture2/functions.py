def square(x):
    return x*x
    
if __name__ == "__main__":
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))