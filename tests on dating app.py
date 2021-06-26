"""
class a :

    c = ["A","B","C","D"]
    cS = set(c)

    def add(self, u):
        self.c.append(u)

class b :

    c = ["Z","U","C","I"]
    cS = set(c)


la = a()
la.add("robe")
print(la.cS)

lo = b()


'''
def Match(x,y):
    if isinstance(x,a) and isinstance(y,b):
        c = x.cS & y.cS
        if len(c) >= 2:
            print("It's a match")
        elif len(c) == 1 :
            print("Maybe")
        elif len(c) == 0 :
            print("dead on")


Match(la,lo)
'''
"""
'''
dic = set()

dic.add("i like march")
print(dic)
'''

li = []

li.extend([i for i in range(ord('A'),ord('Z'))])

print(li)




















