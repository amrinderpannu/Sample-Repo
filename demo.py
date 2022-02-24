import sys
from http.server import executable

print(sys.version)
print(sys, executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

print("hello")


print(greet("World"))
