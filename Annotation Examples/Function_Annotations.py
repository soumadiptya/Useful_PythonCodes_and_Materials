# Annotations with default arguments
def func(a: int, b: int = 1, c: str = " ") -> float:
    return a + b + c

print(func(1,2,3))