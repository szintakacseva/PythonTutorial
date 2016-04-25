import sys

def fileio_exception1():
  try:
    f = open('E:\Temp\integer.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
  except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
    # e can be printed directly without using .args:
    # print(e)
  except ValueError:
    print("No valid integer in line.")
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

def fileio_ex2():
 try:
    f = open('integer.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
 except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
 except:
    print("An unexpected error occurred")
    raise

def fint():
    x = int("klol")

'''
try:
    fint()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")
'''

def fintex():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)
        #info:: if we add raise then the exception is propagated to the caller
        raise

def finally_ex():
    try:
      x = float(23)
      inverse = 1.0 / x
      print (inverse)
    except ValueError as e:
      print("You should have given either an int or a float", e)
    except ZeroDivisionError as e:
      print("Infinity")
    finally:
      print("There may or may not have been an exception.")

'''
try:
    fintex()
except ValueError as e:
    print("got it :-) ", e)
print("Let's get on")
'''

def fileio_ex3():
    file_name = "integer.txt"
    text = []
    try:
      fh = open(file_name, 'r')
      text = fh.readlines()
      fh.close()
    except IOError as e:
      #print('cannot open', file_name, e)
      raise
    except FileNotFoundError as e:
      print('FILE:::::', file_name, e)
      raise
    return  text[100]

def fileio_ex4():
    file_name = "integer.txt"
    text = []
    try:
      fh = open(file_name, 'r')
    except IOError as e:
      print('cannot open', file_name, e)
      raise
    except FileNotFoundError as e:
      print('FILE:::::', file_name, e)
      raise
    else:
      text = fh.readlines()
      fh.close()
    return  text[1]


def greet_person(sPersonName):
    """
    says hellos
    """
    if sPersonName == "Robert":
        raise Exception("we don't like you, Robert")
    print ("Hi there {0}".format(sPersonName))

class MyException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class MyIndexError(IndexError):
    def __init__(self,*args,**kwargs):
        IndexError.__init__(self,*args,**kwargs)


'''
try:
     print(fileio_ex4())
except IndexError as e:
     print("The file contains fewer elements", e)
     raise
'''

#fileio_exception1()
#fileio_ex2()
#finally_ex()
#fileio_ex3()
#greet_person("Maria")