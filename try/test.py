class Mult():
    def __init__(self):
        self.n = None
        self.m = None

    def Gamma(self, n, m):
        if m == 0:
            return n
        else:
            print("Gamma: ", self.Gamma(n,m-1) + 1)
            return self.Gamma(n,m-1) + 1


    def Delta(self,n,m):
        if m == 0:
            return 0
        else:
            print("Delta: ",self.Gamma(n,self.Delta(n,m-1)) )
            return self.Gamma(n,self.Delta(n,m-1))

def main():
    mult = Mult()
    n = 2
    m = 3
    print(mult.Delta(n,m))
main()

