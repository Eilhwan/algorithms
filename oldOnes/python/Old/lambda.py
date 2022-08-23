
def call_10_times(func):
    for _ in range(10):
        func()

def print_hello():
    print("hello")


# call_10_times(print_hello)


def power(number):
    return number * number

def under_3(number):
    return number < 3

list_a = [1, 2, 3, 4, 5]

# print(list(map(power, list_a)))

# print(list(filter(under_3, list_a)))

# print(list(map(lambda x: x * x, list_a)))
print(list(filter(lambda x: x < 3, list_a)))