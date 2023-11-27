from database import Database
from models import Tinta, LojaDeTintas

db = Database('./banco.db')
loja = LojaDeTintas(db)
# cli = Cliente(db)

tinta_1 = Tinta(1, "Tinta Suvinil", "Azul")
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho")
tinta_3 = Tinta(3, "Tinta Coral", "Verde")

# loja.adicionar_tinta(tinta_1)
# loja.adicionar_tinta(tinta_2)
# loja.adicionar_tinta(tinta_3)

tintas = loja.listar_tintas()
for tinta in tintas:
    print(tinta.codigo, tinta.nome, tinta.cor)
