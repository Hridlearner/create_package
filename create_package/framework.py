class Calculator:


    def add(self, x, y):
        print(f"sum of {x} and {y} is {x+y}")
        return x + y

    def mul(self, x, y):
        print(f"multiplication of {x} and {y} is {x*y}")
        return x+y

    def div(self, x, y):
        print(f"divison of {x} and {y} is {x/y}")
        return x+y

    def minus(self, x, y):
        print(f"minus of {x} and {y} is {x-y}")
        return x+y


def main():

    cal =Calculator()
    res = cal.add(5,6)


if __name__=='__main__':
    main()
    
    