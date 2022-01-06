def zero(operation = None): return 0 if not operation else operation(0)
def one(operation = None): return 1 if not operation else operation(1)
def two(operation = None): return 2 if not operation else operation(2)
def three(operation = None): return 3 if not operation else operation(3)
def four(operation = None): return 4 if not operation else operation(4)
def five(operation = None): return 5 if not operation else operation(5)
def six(operation = None): return 6 if not operation else operation(6)
def seven(operation = None): return 7 if not operation else operation(7)
def eight(operation = None): return 8 if not operation else operation(8)
def nine(operation = None): return 9 if not operation else operation(9)

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y
