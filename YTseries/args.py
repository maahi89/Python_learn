def add(*args):
    return sum(args)
print(add(1, 2, 3, 4))


def add(*numbers):
    total = 5
    for num in numbers:
        total = total + num
    return total
print(add(1, 2, 3, 4))


def message(*messages):
    for msg in messages:
        print(msg)
message("Hello", "Lets do it fast!")


def example(a, *args):
    print("a:", a)
    print("args:", args)

example(7, 2, 3, 4)