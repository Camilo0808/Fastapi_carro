

class Financiamento():

    def __init__(self, juros=0.3):
        self.juros = juros    


    def calculo_juros(self, preco, parcelas):
        self.preco = preco
        self.parcelas = parcelas
        preco_juros = preco+(preco*(self.juros/parcelas)*parcelas)
        juros_mensal = (self.juros/parcelas)*100     
        self.mostra_valores(preco_juros, juros_mensal)   

    def mostra_valores(self, preco_juros, juros_mensal):
        print(f'O valor total do carro é de R$:',format(preco_juros, '.2f'))
        print('O juros mensal será de:', format(juros_mensal,'.2f'),'%')


financiamento_marcelo = Financiamento()
financiamento_marcelo.calculo_juros(50000, 24)


