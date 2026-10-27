class Heroi:
    # Dicionário de ataques (Facilita a manutenção e leitura)
    ATAQUES = {
        "mago": "Magia",
        "guerreiro": "Espada",
        "monge": "Artes Marciais",
        "ninja": "Shuriken",
    }

    def __init__(self, nome: str, idade: int, tipo: str):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self) -> None:
        # Converte o tipo para minúsculo para evitar erros de digitação
        tipo_formatado = self.tipo.lower()
        
        # Verifica se o tipo existe no dicionário
        if tipo_formatado in self.ATAQUES:
            ataque = self.ATAQUES[tipo_formatado]
            print(f"O {self.nome}, com {self.idade} anos, do tipo {self.tipo}, atacou usando {ataque}")
        else:
            print(f"[Erro] O tipo '{self.tipo}' não existe. Escolha entre: mago, guerreiro, monge ou ninja.")

# Bloco principal de execução
if __name__ == "__main__":
    print("--- Criação de Herói ---")
    nome_input = input("Digite o nome do Herói: ")
    idade_input = input("Digite a idade do Herói: ")
    tipo_input = input("Digite o tipo (mago, guerreiro, monge, ninja): ")

    # Instanciando o objeto
    heroi = Heroi(nome_input, idade_input, tipo_input)
    
    # Executando a ação
    heroi.atacar()