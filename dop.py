def func():
    a = 1
    b = ['bnvn', 'a', 'b', 'cde', 'c', 'deg']
    return b

def sortf(i):
    i = len(i)
    return i
    
a, *b = func()
print(a)
print('b: ', b)

b.sort(key=lambda i : sortf(i), reverse = True)
print('b: ', b)

c = [i+'1' for i in b if 'e' in i]
print('c:', c)

for i in range(0, len(b)-1):
    b[i] = b[i] + '1'
print(b)
