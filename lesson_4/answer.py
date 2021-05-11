
a = 12

def getPriceA():
    # Q1: return 12
    # Q3: return a
    global a
    return a

# Q2
def setPriceA(price):
    global a
    a = price

# Q4
b = 13

def getPriceB():
    global b
    return b

def setPriceB(price):
    global b
    b = price

# Q5
def sum():
    return getPriceA() + getPriceB()

# Q6, Q7
def input_ab():
    # Q6
    print('Enter A:')
    a = int(input())
    print('Enter B:')
    b = int(input())
    setPriceA(a)
    setPriceB(b)
    # Q7
    print(sum())

def __main__():
    global a
    print("Q1:")
    a = 12
    print(getPriceA())
    print("Q2:")
    setPriceA(14)
    print("Q5:")
    setPriceB(13)
    print("Q6, Q7:")
    input_ab()

__main__()
