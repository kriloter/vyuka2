class Uzivatel:

    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def __str__(self):
        return self.meno

u = Uzivatel("Banan Bananovic", 33)
v = Uzivatel("Jozko Mrkvicka", 22)
print("u: {0}\nv: {1}".format(u, v))
print("u: {0}\nv: {1}\n".format(id(u), id(v)))

u = v
print("u: {0}\nv: {1}".format(u, v))
print("u: {0}\nv: {1}\n".format(id(u), id(v)))

v.meno = "Alfonz Mucha"
print("u: {0}\nv: {1}".format(u, v))
print("u: {0}\nv: {1}\n".format(id(u), id(v)))

v.meno = "John Doe"
v = None
print("u: {0}\nv: {1}".format(u, v))
print("u: {0}\nv: {1}\n".format(id(u), id(v)))
