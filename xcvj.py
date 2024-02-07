# class Wzory:
#     def __init__(self,_m,_v,_F,_A,_V,_p,_I,_w,_g,_s) -> None:
#         self.m = _m
#         self.v = _v
#         self.F = _F
#         self.A = _A
#         self.V = _V
#         self.p = _p
#         self.I = _I
#         self.w = _w
#         self.g = _g
#         self.s = _s
#         self.ped = _m*_v
#         self.cisnienie = _F/_A
#         self.gestosc = _m/_V
#         self.objetosc = _m/_p
#         self.masa = _V*_p
#         self.pole_powiezchni = _I*_w
#         self.ciezar = _m*_g
#         self.praca = _F*_s

#     def inf(self):
#         print(f"ped = {self.ped}")
#         print(f"cisnienie = {self.cisnienie}")
#         print(f"gestosc = {self.gestosc}")
#         print(f"objetosc = {self.objetosc}")
#         print(f"masa = {self.masa}")
#         print(f"pole powiezchni = {self.pole_powiezchni}")
#         print(f"ciezar = {self.ciezar}")
#         print(f"praca = {self.praca}")



# w1 = Wzory(1,2,3,4,5,6,8,7,9,10)
# w1.inf

class Wzory:

    @staticmethod
    def ped(m,f):
        print(m*f)

    @staticmethod
    def cisnienie(F,A):
        print(F/A)
    
    @staticmethod
    def gestosc(m,V):
        print(m/V)

    @staticmethod
    def objetosc(m,p):
        print(m/p)

    @classmethod
    def masa(V,p):
        print(V*p)

    @classmethod
    def pole_powiezchni(I,w):
        print(I*w)

    @classmethod
    def ciezar(m,g):
        print(m,g)


    @classmethod
    def praca(F,s):
        print(F*s)




w1 = Wzory
w1.inf
