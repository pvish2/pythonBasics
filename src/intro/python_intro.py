"""
Python is a strongly-typed, dynamic interpreted language.

  - Python DOES DO type checking! But it does it at runtime
  - Python translates the code at runtime: it is an INTERPRETED language
"""

foo = "5" + 4   # Will raise an error


def bar(num):
    if num > 3:
        print(num + 2)
    else:
        print("5" + 4)


bar(4)   # Life is good
bar(2)   # Life is hell

# For reference, read:
# https://hackernoon.com/i-finally-understand-static-vs-dynamic-typing-and-you-will-too-ad0c2bd0acc7


"""
Duck typing: behaviour is more important than type
"""

class Duck:
    def quack(self):
        return 'Quack!'


class CrazyGoat:
    def quack(self):
        return 'Quack!'


class Dog:
    def bark(self):
        return 'Bau!'


class DuckRecogniser:
    def check_duck(self, animal):
        try:
            if animal.quack() == 'Quack!':
                print('Yes, it is a duck')
        except AttributeError:
            print('It is not a duck!')


duck = Duck()
crazy_goat = CrazyGoat()
dog = Dog()
dr = DuckRecogniser()

dr.check_duck(duck)
dr.check_duck(crazy_goat)
dr.check_duck(dog)


# This has deeper repercussions on OOP. Can read for further reference:
# https://hackernoon.com/python-duck-typing-or-automatic-interfaces-73988ec9037f

# For a detailed discussion on EAFP, please read:
# https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/


"""
Zoom on Python variables
"""

a = 5
b = a   # variable 'b' gets the value of 'a'?

b = b + 5

print(a)
print(b)   # All good so far, a=5 and b=10


w = [1, 2, 3]
z = w   # variable 'bz gets the value of 'w'?

w.append(4)

print(w)
print(z)   # What???


def simple_function(var_one, var_two):
    var_one = var_one + 4
    var_two = var_two + 5


simple_function(a, b)
print(a)
print(b)   # All good so far, a=5 and b=10


def another_simple_function(var_one, var_two):
    var_one.append(5)
    var_two.append(6)


another_simple_function(w, z)
print(w)
print(z)   # What???