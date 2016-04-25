__author__ = 'takacs'

def print_keyword_args(**kwargs):
     # kwargs is a dict of the keyword args passed to the function
    for key, value in kwargs.items():
        print ("%s = %s" % (key, value))

def f(a = 0, *args, **kwargs):
    print("Received by fn(a, *args, **kwargs)")
    print("=> f(a=%s, args=%s, kwargs=%s" % (a, args, kwargs))
    print("Calling g(10, 11, 12, *args, d = 13, e = 14, **kwargs)")
    g(10, 11, 12, *args, d = 13, e = 14, **kwargs)

def g(f, g = 0, *args, **kwargs):
    print("Received by g(f, g = 0, *args, **kwargs)")
    print("=> g(f=%s, g=%s, args=%s, kwargs=%s)" % (f, g, args, kwargs))

def args_kwargs_test(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def test(**kwargs):
    print(kwargs['a'])
    print(kwargs['b'])
    print(kwargs['c'])

def returnexample():
    return 5+6

if __name__ == "__main__":
    print ('Kwarg tutorial examples....')
    #You can use **kwargs to let your functions take an arbitrary number of keyword arguments:
    print_keyword_args(first_name="John", last_name="Doe")
    print_keyword_args(gyumolcs="alma", zoldseg="retek")
    print_keyword_args(gyumolcs="alma", zoldseg="retek", gabona="buza")
    '''
    You can also use the **kwargs syntax when calling functions by constructing a dictionary of keyword arguments
    and passing it to your function:
    '''
    kwargs = {'first_name': 'Bobby', 'last_name': 'Smith'}
    print_keyword_args(**kwargs)
    print("Calling fn(1, 2, 3, 4, b = 5, c = 6)")
    f(1, 2, 3, 4, b = 5, c = 6)
    print("args_kwargs_test():: *args has no intelligence, it simply interpolates the passed args to the parameters(in left-to-right order) while **kwargs behaves intelligently by placing the appropriate value @ the required place")
    args =("two", 3, 5)
    args_kwargs_test(*args)
    kwargs = {"arg3":3, "arg2":'two', "arg1":5}
    args_kwargs_test(**kwargs)
    args = { 'c': 5, 'b': 7}
    test(a=1, **args )
    osszeg = returnexample()
    print("Osszeg::" + repr(osszeg) )


