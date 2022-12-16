

class Financiamento():

    def __init__(self, preco, parcelas, juros, preco_juros=0):
        
        self. preco = preco
        self.parcelas = parcelas
        self.juros = juros
        preco_juros = preco+(preco*(juros/parcelas)*parcelas)
        juros_mensal = (juros/parcelas)*100     

        print(f'O valor total do carro é de R$:',format(preco_juros, '.2f'))
        print('O juros mensal será de:', format(juros_mensal,'.2f'),'%')

financiamento_marcelo = Financiamento(50000, 24, 0.20)



