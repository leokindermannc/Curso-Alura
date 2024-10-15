class ContaBancaria:
    
    contas = []
    
    def __init__(self,saldo,despesas,ativo):
        self.saldo = saldo
        self.despesas = despesas
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return  f'{self.saldo} | {self.despesas}'
    @classmethod
    def listar_contas(cls):
        print(f'{'saldo'.ljust(33)} | {'despesas'.ljust(33)} | {'status'}')
        for contas in cls.contas:
            print(f'{contas.saldo.ljust(33)} | {contas.despesas.ljust(33)} | {contas.ativo}')
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alterna_estado(self):
        self._ativo = not self._ativo




ContaBancaria1 = ContaBancaria('R$100','R$200','')
ContaBancaria2 = ContaBancaria('R$10000000', 'R$1000','')
ContaBancaria1.alterna_estado()
ContaBancaria.listar_contas()

