class Contador:
    contador = 0  # atributo de classe
    
    def inst(self):
        return 'Estou bem!'
        
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    @classmethod
    def mais_um(cls,n):
        return n + 1

# c1 = Contador()
# print(c1.inst())

print(Contador.inc())  # 1
print(Contador.inc())  # 2
print(Contador.inc())  # 3
print(Contador.dec())  # 2
print(Contador.dec())  # 1
print(Contador.dec())  # 0
print(Contador.mais_um(99)) # 100