class osztaly():
    def __init__(self, *args, **kwargs):
       super(osztaly, self).__init__(*args, **kwargs)
       initial = kwargs.pop('initial')
       self.valtozo = initial['valtozo']


#instance = osztaly(initial={"valtozo": "ertek"})
#print (instance.valtozo)

'''
def test(*args, **kwargs):
    initial = kwargs.pop('initial')
    keresztnev = initial['keresztnev']
    return keresztnev

print (test, {'keresztnev': "Éva"})


def test(**kwargs):
    print (kwargs['a'])
    print (kwargs['b'])
    print (kwargs['c'])


args = { 'b': 2, 'c': 3}

test( a=1, **args )
'''

def test(**kwargs):
    print (kwargs['a'])
    print (kwargs['b'])
    print (kwargs['c'])

initial = {'nev': "Éva"}
args = initial



def mytest(*args, **kwargs):
    initial = kwargs.pop('initial')
    nev = initial['nev']
    return nev


print(mytest(initial = {"nev": "Eva"}))