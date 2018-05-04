def func(a):
    l = []
    while a < 10:
        a += 1
        l.append(a)
    return l

class Iter:
    def __init__(self, a):
        self.a = a

    def __iter__(self):
            return self

    def __next__(self):
        a = self.a
        if a < 10:
            a += 1
            self.a = a
            return a
        else:
            raise StopIteration

    def gen(self):
        a = self.a
        a += 2
        yield a
        a += 3
        yield a
        a += 7
        yield a

    def gen2(self):
        a = self.a
        if a < 10:
            a += 1
            self.a = a
            yield a 
        

def generat(a):
        a += 1
        yield a
        a += 2
        yield a
        a += 3
        yield a

def generat2(a):
    if a < 10:
        a += 1
        yield a 

a = 0
i = None
fu = func(a)
it = Iter(a)
# print(f)

gn = generat(a)

def for2(i, gn):
    for i in gn:
        print(i)

#for i in it.gen2():
    #print(i)

for2(i, gn)
for2(i, gn)

