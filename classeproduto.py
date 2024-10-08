class Pessoa:
    
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
    def idademaior(self):
        if self.idade >= 18:
            print(f"{self.nome} parabens vc e adulto")
           
        elif self.idade <= 17 and self.idade >= 12:
            print(f"{self.nome} parabens vc e adolescente")
        else:
            print(f"{self.nome} parabens vc e criança")
            

