class Tinta:
    def __init__(self, codigo, nome:str, cor:str):
        self.codigo = codigo
        self.nome = nome
        self.cor = cor
        
    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Nome: {self.nome}, Cor: {self.cor}, Quantidade em litros: {self.quantidade_peso}, Quantidade no estoque: {self.quantidade_estoque}, Preço: {self.preco}")
        if self.observacao: # O método exibir_informacoes verifica se há uma observação antes de tentar imprimi-la.
            print(f"Observação: {self.observacao}")
    
    def listar_tintas(self):             # O método "listar tintas" é aqui dentro da classe Tinta?
        for tinta in self.tintas:
            print(f"Código: {tinta.codigo}, Nome: {tinta.nome}, Cor: {tinta.cor}, Quantidade: {tinta.quantidade}, Preço: {tinta.preco}")




from database import Database


class LojaDeTintas:
    def __init__(self, db: Database):
        self.db = db
        self.__criar_tabela_tinta()
    
    def __criar_tabela_tinta(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS tintas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                cor VARCHAR(255) NOT NULL
            ) ''')

    def adicionar_tinta(self, tinta: Tinta):
        # cursor = self.conx.cursor()
        
        # cursor.execute('''
        #     INSERT INTO tintas (nome, cor) 
        #     VALUES (?, ?)
        # ''', [tinta.nome, tinta.cor])

        # cursor.close()
        # self.conx.commit()
        self.db.execute('''
            INSERT INTO tintas (nome, cor) 
            VALUES (?, ?)
        ''', tinta.nome, tinta.cor)

    def listar_tintas(self) -> list[Tinta]:             # Ou dentro da classe LojaDeTintas?
        tintas_tuplas = self.db.get_all('SELECT * FROM tintas')

        tintas = []
        for tinta in tintas_tuplas:
            tintas.append(Tinta(tinta[0], tinta[1], tinta[2]))

        return tintas

    def buscar_tinta_by_id(self, codigo):
        for tinta in self.tintas:
            if tinta.codigo == codigo:
                return tinta
        return None

    def atualizar_tinta_by_id(self, codigo, novo_nome, nova_cor, nova_quantidade, novo_preco):
        tinta = self.buscar_tinta_by_id(codigo)
        if tinta:
            tinta.nome = novo_nome
            tinta.cor = nova_cor
            tinta.quantidade = nova_quantidade
            tinta.preco = novo_preco
            print("Tinta atualizada com sucesso!")
        else:
            print("Tinta não encontrada.")

    def excluir_tinta_by_id(self, codigo):
        tinta = self.buscar_tinta_by_id(codigo)
        if tinta:
            self.tintas.remove(tinta)
            print("Tinta excluída com sucesso!")
        else:
            print("Tinta não encontrada.")