class Produto:
    def __init__(self,nome, preco = 1.99, desc=0):
        self.nome = nome
        self.preco = preco
        self.desc = desc
    @property
    def preco(self):
        return self.__preco #esconder o nome, tornar privado
    
    # @property
    # def preco(self, novo_preco):
    #     if novo_preco > 0:
    #      self.__preco = novo_preco #conseguir controlar como esses dados estao apresentando, nesse caso eu proibo o preco ser menor que 0
    @property #faz eu conseguir passar como um atributo e nao uma funcao
    def preco_final(self):
        return (1-self.desc)* self.preco    

p1 = Produto('Caneta', 10, 0.1) # Produto.__init__(p1)
p2 = Produto('Caderno', 14, 0.5)

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)