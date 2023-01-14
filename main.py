import random

def getResult():
    random.seed()
    i = random.choice([0,1])
    print(i)
    if (i == 1):
        return "Heads!"
    else:
        return "Tails!"

if __name__ == '__main__':
    print(getResult())
