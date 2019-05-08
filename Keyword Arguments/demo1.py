class A:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def verify(self):
        print(self.a,self.b,self.c)

args = {'a':10,'b':20,'c':30}
x = A(**args)
x.verify()