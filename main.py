from conta_bancaria import ContaBancaria
from produto import Produto
from aluno import Aluno
from livro import Livro
from funcionario import Funcionario
from carro import Carro
from pessoa import Pessoa
from conta_de_luz import ContaDeLuz
from animal import Animal
from caixa import Caixa

# EXERCÍCIO I 
def criar_conta():
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    saldo = float(input("Digite o saldo inicial: "))
            
    conta = ContaBancaria(numero, titular, saldo)
    print(f"\nConta criada com sucesso!\nTitular: {conta.get_titular()}\nNúmero: {conta.get_numero_conta()}\nSaldo: R${conta.get_saldo():.2f}\n")
    return conta


def menu(conta):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Histórico")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Digite um valor válido.")
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Digite um valor válido.")
        elif opcao == "3":
            print(f"\nSaldo atual: R${conta.get_saldo():.2f}")
        elif opcao == "4":
            conta.mostrar_historico()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    minha_conta = criar_conta()
    menu(minha_conta)

#EXERCÍCIO II
def cadastrar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Digite um valor válido para o preço.")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Digite um valor válido para a quantidade.")
    
    produto = Produto(nome, preco, quantidade)
    estoque.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!\n")


def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        print("\n=== Lista de Produtos ===")
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto.get_nome()} - R${produto.get_preco():.2f} - Estoque: {produto.get_quantidade()}")


def menu_estoque():
    estoque = []
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Adicionar estoque")
        print("4 - Remover estoque")
        print("5 - Alterar preço")
        print("6 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            listar_produtos(estoque)
            if estoque:
                try:
                    idx = int(input("Escolha o produto pelo número: ")) - 1
                    qtd = int(input("Quantidade a adicionar: "))
                    estoque[idx].adicionar_estoque(qtd)
                except (ValueError, IndexError):
                    print("Opção inválida.")
        elif opcao == "4":
            listar_produtos(estoque)
            if estoque:
                try:
                    idx = int(input("Escolha o produto pelo número: ")) - 1
                    qtd = int(input("Quantidade a remover: "))
                    estoque[idx].remover_estoque(qtd)
                except (ValueError, IndexError):
                    print("Opção inválida.")
        elif opcao == "5":
            listar_produtos(estoque)
            if estoque:
                try:
                    idx = int(input("Escolha o produto pelo número: ")) - 1
                    preco = float(input("Novo preço: "))
                    estoque[idx].set_preco(preco)
                except (ValueError, IndexError):
                    print("Opção inválida.")
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_estoque()

# EXERCÍCIO III
def menu_alunos():
    alunos = []

    def cadastrar_aluno():
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        while True:
            try:
                media = float(input("Digite a média final do aluno: "))
                if media < 0 or media > 10:
                    print("A média deve estar entre 0 e 10. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Digite um número válido para a média.")

        aluno = Aluno(nome, matricula, media)
        alunos.append(aluno)
        print(f"\nAluno '{aluno.get_nome()}' cadastrado com sucesso!\n")

    def listar_alunos():
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n=== Lista de Alunos ===")
            for i, aluno in enumerate(alunos, 1):
                print(f"{i}. {aluno.get_nome()} - Matrícula: {aluno.get_matricula()} - Média: {aluno.get_media()}")

    def consultar_media():
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        listar_alunos()
        try:
            idx = int(input("Escolha o aluno pelo número: ")) - 1
            aluno = alunos[idx]
            print(f"Média do aluno {aluno.get_nome()}: {aluno.get_media()}")
        except (ValueError, IndexError):
            print("Opção inválida.")

    def consultar_situacao():
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        listar_alunos()
        try:
            idx = int(input("Escolha o aluno pelo número: ")) - 1
            aluno = alunos[idx]
            aluno.esta_aprovado()
        except (ValueError, IndexError):
            print("Opção inválida.")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Consultar média de um aluno")
        print("4 - Consultar situação de um aluno")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            consultar_media()
        elif opcao == "4":
            consultar_situacao()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_alunos()

# EXERCÍCIO IV 
def criar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação: "))
    
    livro = Livro(titulo, autor, ano)
    print(f"\nLivro '{livro.get_titulo()}' criado com sucesso!\nAutor: {livro.get_autor()}\nAno: {livro.get_ano()}")
    return livro

def menu_livros():
    livros = []
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Consultar livro")
        print("4 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            livro = criar_livro()
            livros.append(livro)
        elif opcao == "2":
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                print("\n=== Lista de Livros ===")
                for i, livro in enumerate(livros, 1):
                    print(f"{i}. {livro.get_titulo()} - Autor: {livro.get_autor()} - Ano: {livro.get_ano()}")
        elif opcao == "3":
            if not livros:
                print("Nenhum livro cadastrado.")
                continue
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.get_titulo()}")
            try:
                idx = int(input("Escolha o livro pelo número: ")) - 1
                livro = livros[idx]
                print(f"\nTítulo: {livro.get_titulo()}")
                print(f"Autor: {livro.get_autor()}")
                print(f"Ano de publicação: {livro.get_ano()}")
            except (ValueError, IndexError):
                print("Opção inválida.")
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_livros()

# EXERCÍCIO V
def criar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário inicial: "))

    funcionario = Funcionario(nome, cargo, salario)
    print(f"\nFuncionário '{funcionario.get_nome()}' criado com sucesso! Cargo: {funcionario.get_cargo()}, Salário: {funcionario.get_salario()}\n")
    return funcionario

def menu(funcionario):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver salário")
        print("2 - Aumentar salário")
        print("3 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print(f"Salário do funcionário {funcionario.get_nome()}: {funcionario.get_salario()}")
        elif opcao == "2":
            try:
                percentual = float(input("Digite o percentual de aumento: "))
                funcionario.aumentar_salario(percentual)
            except ValueError:
                print("Digite um número válido para o percentual.")
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    meu_funcionario = criar_funcionario()
    menu(meu_funcionario)

# EXERCÍCIO VI 
if __name__ == "__main__":
    carro1 = Carro("Fiesta", 2015)

    print("Modelo:", carro1.get_modelo())
    print("Ano:", carro1.get_ano())
    print("Velocidade inicial:", carro1.get_velocidade())

    carro1.acelerar(50)
    print("Após acelerar 50 km/h:", carro1.get_velocidade())

    carro1.acelerar(180) 
    print("Após acelerar mais 180 km/h:", carro1.get_velocidade())

    carro1.frear(30)
    print("Após frear 30 km/h:", carro1.get_velocidade())

    carro1.frear(500) 
    print("Após frear muito forte:", carro1.get_velocidade())

# EXERCÍCIO VII
def criar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    cpf = input("Digite o CPF (apenas números): ")
    idade = int(input("Digite a idade: "))

    pessoa = Pessoa(nome, idade, cpf)
    print(f"\nPessoa '{pessoa.get_nome()}' criada com sucesso! Idade: {pessoa.get_idade()}, CPF: {pessoa.get_cpf()}\n")
    return pessoa

def menu(pessoa):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver nome")
        print("2 - Ver idade")
        print("3 - Atualizar idade")
        print("4 - Ver CPF")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print(f"Nome: {pessoa.get_nome()}")
        elif opcao == "2":
            print(f"Idade: {pessoa.get_idade()}")
        elif opcao == "3":
            try:
                nova_idade = int(input("Digite a nova idade: "))
                pessoa.set_idade(nova_idade)
                print(f"Idade atualizada para {pessoa.get_idade()}")
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "4":
            print(f"CPF: {pessoa.get_cpf()}")
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    pessoa_criada = criar_pessoa()
    menu(pessoa_criada)

# EXERCÍCIO VIII 
def criar_conta():
    numero = input("Digite o número da instalação: ")
    consumo = float(input("Digite o consumo em kWh: "))

    conta = ContaDeLuz(numero, consumo)
    print(f"\nConta de luz criada! Número: {conta.get_numero_instalacao()}, Consumo: {conta.get_consumo()} kWh, Valor: R$ {conta.get_valor():.2f}\n")
    return conta

def menu(conta):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver consumo")
        print("2 - Atualizar consumo")
        print("3 - Ver valor da conta")
        print("4 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print(f"Consumo atual: {conta.get_consumo()} kWh")
        elif opcao == "2":
            try:
                novo_consumo = float(input("Digite o novo consumo em kWh: "))
                conta.set_consumo(novo_consumo)
                print(f"Consumo atualizado: {conta.get_consumo()} kWh. Valor: R$ {conta.get_valor():.2f}")
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "3":
            print(f"Valor da conta: R$ {conta.get_valor():.2f}")
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    conta_criada = criar_conta()
    menu(conta_criada)

# EXERCÍCIO IX 
def criar_animal():
    nome = input("Digite o nome do animal: ")
    especie = input("Digite a espécie do animal: ")
    idade = int(input("Digite a idade do animal: "))

    animal = Animal(nome, especie, idade)
    print(f"\nAnimal '{animal.get_nome()}' criado! Espécie: {animal.get_especie()}, Idade: {animal.get_idade()} anos\n")
    return animal

def menu(animal):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver nome")
        print("2 - Ver espécie")
        print("3 - Ver idade")
        print("4 - Envelhecer")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print(f"Nome: {animal.get_nome()}")
        elif opcao == "2":
            print(f"Espécie: {animal.get_especie()}")
        elif opcao == "3":
            print(f"Idade: {animal.get_idade()} anos")
        elif opcao == "4":
            animal.envelhecer()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    animal_criado = criar_animal()
    menu(animal_criado)

# EXERCÍCIO X 
def menu_caixa():
    caixa = Caixa()
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar produto")
        print("2 - Ver total da compra")
        print("3 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço do produto: "))
                caixa.adicionar_produto(nome, preco)
            except ValueError:
                print("Digite um valor válido para o preço.")
        elif opcao == "2":
            print(f"Total da compra: R$ {caixa.get_total():.2f}")
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_caixa()
