
# def add(n1, n2):
#     return n1 + n2

# CHANGE ABOVE TO:

# def add(*args):
#     for n in args:
#         print(n)
#
# add(n1=5, n2=3)

def add(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        total += value
    print("Total:", total)

add(n1=5, n2=3, n3=15, n4=82)