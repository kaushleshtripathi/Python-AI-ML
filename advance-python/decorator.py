import random 

def randomnumberGenerator(function):
    def wrapper():
        random_number = random.randint(100,1000)
        function(random_number)
    return wrapper


@randomnumberGenerator
def functionA(num):
    print(f"Random number is for functionA: {num}")

@randomnumberGenerator
def functionB(num):
    print(f"Random number is for functionB: {num}")

@randomnumberGenerator
def functionC(num):
    print(f"Random number is for functionC: {num}")


functionA()
functionB()
functionC()