class Magazine:
    def __init__(self,name,opis,kol,summa):
        self.name = 'POCO x4 Pro 5G'
        self.opis = 'bolshay kamera na 108 mg'
        self.kol = 4
        self.summa = 3000000
    def kolvo(self):
        return self.kol * self.summa
kolichestvo=4*3000000
obssumm=f'Покупатель купил 4 POCO x4 Pro 5G'
print(obssumm)
print(f'общая сумма {kolichestvo}')



        
    