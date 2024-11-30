from Practice.Dictonary import values

a=values.a
b=values.b
c=values.c
b.update(c)
alist=list(a)
a.add(555)
print(a)
alist.pop(0)
print(alist)
a.update(b)
print(a)

if 21 in a:

        print(f"num {a} iss present")

f=b.union(c)
print("ee",f)

g=b.intersection(c)
print(g)

w= b.difference(c)
print(w)
