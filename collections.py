import pickle

class Serch:
    def __init__(self, text, string):
            self.__result = False
            self.serch(text, string)
            self.result()
        
    def serch(self, text, string):
        textT = text
        strL = string

        if strL in textT:
            self.__result = True
            return self.__result

    def result(self):
        result = self.__result
        return result

    def resultStr(self):
        result = self.__result
        if result == True:
            result = 'True'
            return result
        else:
            result = 'False'
            return result
        
s = Serch('I am a Andrey', 'An')
c = Serch('vvv', '_')
y = Serch('abcd 4', 'd 4')

"""f = open('serch.txt', 'a')
f.write('\n' + s.resultStr())
f.close()

f = open('serch.txt')

while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close()"""

"""t = ('name', 'keywords')
t1 = ('content', 'lalala')
attrs = [t, t1]

a = {attrs[0][0] : attrs[0][1],
     attrs[1][0] : attrs[1][1]}
print(a)
print(a.values())
print(a)"""

l = [s, c, y]

filename = 'serch.pnp42'

f = open (filename, 'wb')
pickle.dump(l, f)
f.close

del s, c, y, l

f = open(filename, 'rb')
l = pickle.load(f)

for i in l:
    print(i.result())
        

