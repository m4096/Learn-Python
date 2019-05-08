class A:
    def __init__(self,**kwargs):
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.c = kwargs['c']
    def verify(self):
        print(self.a,self.b,self.c)

args = {'a':10,'b':20,'c':30,'extra':'unexpected'}
x = A(**args)
x.verify()
