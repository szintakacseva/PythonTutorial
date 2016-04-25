from iterators.fibonacci2 import Fib
from iterators.plural6 import LazyRules

fib1 = Fib(100)
fib2 = Fib(200)

'''
print(fib1.max)
print(fib2.max)
for n in Fib(78):
    print(n, end = ' ')
'''
'''
r1 = LazyRules()
r2 = LazyRules()

r2.rules_filename = 'r2-override.txt'
r2.__class__.rules_filename = 'papayawip.txt'


print(r1.rules_filename)
print(r2.rules_filename)
print(r2.__class__.rules_filename)
'''

rules = LazyRules()

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


print(plural('dog'))


