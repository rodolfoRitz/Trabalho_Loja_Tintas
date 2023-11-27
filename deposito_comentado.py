'''Este programa é uma simulação de um sistema para um depósito de tintas com algumas classes e seus métodos executados por funções.'''
# Uma ideia é sincronizar o programa com o banco de dados "SQLite". Vou procurar fazer depois.

class Tinta:
    '''Classe que cria a partir do método construtor, os objetos do tipo Tinta, com seus respectivos atributos.'''
    def __init__(self, id, nome:str, cor:str, quantidade_peso:float, quantidade_estoque:int, preco:float, observacao=None):
        '''Este é o método construtor da classe Tinta.'''
        self.id = id
        self.nome = nome
        self.cor = cor
        self.quantidade_peso = quantidade_peso
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.observacao = observacao # A observacao é um atributo opcional, quando quiser basta passá-la como argumento ao criar uma instância da classe.

class LojaDeTintas:
    '''Classe que armazena todas as tintas criadas e as manipula com seus métodos.'''
    def __init__(self):
        self.tintas = []

    def adicionar_tinta(self, tinta):
        '''Método que adiciona um objeto tipo 'tinta' na 'LojaDeTintas'.'''
        self.tintas.append(tinta)

    '''def exibir_informacoes(self):
            # Este método exibe as informações do objeto pelo ID previamente informado.
            print(f"Product ID: {self.id}, Nome: {self.nome}, Cor: {self.cor}, Quantidade em litros: {self.quantidade_peso}, Quantidade no estoque: {self.quantidade_estoque}, Preço: {self.preco}")
            if self.observacao:      # O método exibir_informacoes verifica se há uma observação antes de tentar imprimi-la.
                return "Observação: {self.observacao}"'''

    def listar_tintas(self): 
        '''Método que retorna todas as tintas do estoque por linha em ordem crescente.'''
        for tinta in self.tintas:
            print(f"Product ID: {tinta.id}, Nome: {tinta.nome}, Cor: {tinta.cor}, Peso da tinta: {tinta.quantidade_peso}, Quantidade no estoque: {tinta.quantidade_estoque}, Preço: {tinta.preco}")

    def get_tinta_by_id(self, id):
        '''Método que retorna a tinta a partir do ID informado.'''
        for tinta in self.tintas:
            if tinta.id == id:
                return print(f"Product ID: {tinta.id}, Nome: {tinta.nome}, Cor: {tinta.cor}, Peso da tinta: {tinta.quantidade_peso}, Quantidade no estoque: {tinta.quantidade_estoque}, Preço: {tinta.preco}")
        return None

    def atualizar_tinta_by_id(self, id, novo_nome, nova_cor, nova_quantidade_peso, nova_quantidade_estoque, novo_preco):
        '''Método que atualiza as informações da Tinta pelo ID informado.'''
        tinta = self.get_tinta_by_id(id)
        if tinta:
            tinta.nome = novo_nome
            tinta.cor = nova_cor
            tinta.quantidade_peso = nova_quantidade_peso
            tinta.quantidade_estoque = nova_quantidade_estoque
            tinta.preco = novo_preco
            return "Tinta atualizada com sucesso!"
        else:
            return "Tinta não encontrada."

    def excluir_tinta_by_id(self, id):
        tinta = self.get_tinta_by_id(id)
        if tinta:
            self.tintas.remove(tinta)
            return "Tinta excluída com sucesso!"
        else:
            return "Tinta não encontrada."

class Cliente:
    def __init__(self, cpf:int, nome:str, endereco:str, email:str, telefone:float):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

class ListaClientes:
    '''Esta Classe obtém os dados dos clientes cadastrados em 'Cliente' e o coloca em uma lista.'''  
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        '''Método que adiciona o objeto (cliente) na lista 'ListaClientes'.'''
        self.clientes.append(cliente)
    
    def listar_clientes(self):
        '''Método que mostra todos os clientes cadastrados.'''
        for cliente in self.clientes:
            print(f"Client CPF: {cliente.cpf}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, E-mail: {cliente.email}, Telefone: {cliente.telefone}")

    def buscar_cliente_by_cpf(self, cpf):
        '''Método que mostra o cliente cadastrado no número de identificação ÚNICO: CPF informado.'''
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return print(f"Client CPF: {cliente.cpf}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, E-mail: {cliente.email}, Telefone: {cliente.telefone}")
        return None

    def atualizar_cliente_by_cpf(self, cpf, novo_nome, novo_endereco, novo_email, novo_telefone):
        '''Método que atualiza os dados do cliente pelo número de identificação ÚNICO: CPF'''
        cliente = self.buscar_cliente_by_cpf(cpf)
        if cliente:
            cliente.nome = novo_nome
            cliente.endereco = novo_endereco
            cliente.email = novo_email
            cliente.telefone = novo_telefone
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def excluir_cliente_by_cpf(self, cpf):
        '''Método que exclui o cadastro do objeto cliente pelo número de identificação ÚNICO: CPF'''
        cliente = self.buscar_cliente_by_cpf(cpf)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def pesquisar_by_cargo():
        ...

class Fornecedor:
    def __init__(self, nome, contato, produtos_fornecidos):
        self.nome = nome
        self.contato = contato
        self.produtos_fornecidos = produtos_fornecidos

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedor.append(fornecedor)

class Venda:
    def __init__(self, cliente, tintas_vendidas, data):
        self.cliente = cliente
        self.tintas_vendidas = tintas_vendidas
        self.data = data

    def vender_tinta(self, nome_tinta, quantidade):                 # TESTAR !!
        '''Vende uma quantidade específica de uma tinta do estoque'''
        if nome_tinta in self.estoque_tintas and quantidade <= self.estoque_tintas[nome_tinta]:
            self.estoque_tintas[nome_tinta] -= quantidade
            print(f'{quantidade} litros de {nome_tinta} vendidos.')
        elif nome_tinta not in self.estoque_tintas:
            print(f'Erro: A tinta {nome_tinta} não está no estoque.')
        else:
            print(f'Erro: Estoque insuficiente para vender {quantidade} litros de {nome_tinta}.')

class TransacaoCompra:
    '''Classe que cria um objeto com as informações da compra.'''
    def __init__(self, fornecedor, tinta, quantidade, data):
        self.fornecedor = fornecedor
        self.tinta = tinta
        self.quantidade = quantidade
        self.data = data

class CarrinhoCompras:
    '''Classe que armazena os objetos com as informações da compra.'''
    def __init__(self):
        self.itens = []

    def adicionar_item(self, tinta, quantidade):
        self.itens.append((tinta, quantidade))   # Coloca no "append" só o código ou todas as caracteríscticas?

class CupomDesconto:
    '''Classe que aplica um desconto a partir do ID da compra.'''
    def __init__(self, id, desconto_percentual, data_validade):
        self.id = id
        self.desconto_percentual = desconto_percentual
        self.data_validade = data_validade

    def lancar_desconto():
        '''Teoricamente aplica o desconto no produto selecionado.'''
        ...

loja = LojaDeTintas()
client = ListaClientes()

# Exemplo de uso:
tinta_1 = Tinta(1, "Tinta Suvinil", "Azul", 5, 50, 10.99, "Essa tinta é resistente à água.")
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho", 5, 30, 8.99)
tinta_3 = Tinta(3, "Tinta Coral", "Verde", 10, 50, 18.99)
loja.adicionar_tinta(tinta_1)
loja.adicionar_tinta(tinta_2)
loja.adicionar_tinta(tinta_3)

cliente_1 = Cliente(42125452634, "Joao", "rua Estoril", "jonas@tmail.com", 1146798678967)
cliente_2 = Cliente(52125452634, "Maria", "rua dos Otoni", "marrie@umail.com", 5546798678967)
cliente_3 = Cliente(62125452634, "Serena", "rua Estoril", "serenity@kmail.com", 2146798678967)
client.adicionar_cliente(cliente_1)
client.adicionar_cliente(cliente_2)
client.adicionar_cliente(cliente_3)

loja.get_tinta_by_id(2)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()
loja.atualizar_tinta_by_id(1, "Tinta C", "Yellow", 20, 20, 15.99)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()
loja.excluir_tinta_by_id(2)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()

client.listar_clientes()
client.atualizar_cliente_by_cpf(1, "Bruno", "rua das Margaridas", "bru@imail.com", 20159971843)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
client.listar_clientes()
client.excluir_cliente_by_cpf(62125452634)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
client.listar_clientes()

# Pendente
Venda.vender_tinta('Tinta Coral', 10)