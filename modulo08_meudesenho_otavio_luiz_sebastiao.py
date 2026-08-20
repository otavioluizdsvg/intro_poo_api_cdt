'''
ben10 - ben10
coragem o cão covarde - coragem
steven universo - steven
'''


class BonecoToyStory:
    def __init__(self, nome, dono, frase_de_efeito):
        self.nome = nome
        self.dono = dono
        self.frase_de_efeito = frase_de_efeito



senhor_potato = BonecoToyStory(
           
nome='Sr_Potato',
dono='Andy',
frase_de_efeito='Eu sou o Senhor Batata!'
)

woody = BonecoToyStory(
    nome='Woody',
    dono='Andy',
    frase_de_efeito='Há uma cobra no meu bota!'
)


buzlaitir = BonecoToyStory(
    nome='Buzz Lightyear',
    dono='Andy',
    frase_de_efeito='Ao infinito e além!'
)

print(f'Nome: {woody.nome} | Dono: {woody.dono} | frase {woody.frase_de_efeito}')





