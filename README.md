# 🦸‍♂️ Desafio de Lógica: Classes de Heróis (Python)

Este repositório contém a resolução de um desafio prático de lógica de programação e orientação a objetos. O objetivo do projeto foi criar uma classe genérica de herói que possui atributos básicos e um método de ataque que varia de acordo com a sua classe (tipo).

O código foi desenvolvido em **Python**, aplicando boas práticas da linguagem (PEP 8), conceitos de Clean Code e tratamento de erros para a entrada de dados.

## 🎯 Objetivo do Desafio

Criar uma estrutura que atenda aos seguintes requisitos:
1. **Atributos:** O herói deve ter `nome`, `idade` e `tipo` (ex: mago, guerreiro, monge, ninja).
2. **Ação:** O herói deve ter um método/ação de `atacar()`.
3. **Regra de Negócio:** O tipo de ataque deve mudar conforme o `tipo` do herói:
   - Mago ➔ ataca usando Magia
   - Guerreiro ➔ ataca usando Espada
   - Monge ➔ ataca usando Artes Marciais
   - Ninja ➔ ataca usando Shuriken
4. **Saída de Dados:** O programa deve exibir a mensagem: `"O {nome}, com {idade} anos, do tipo {tipo}, atacou usando {ataque}"`.

---

## 🛠️ Soluções Aplicadas no Código

Para garantir um código limpo e funcional, as seguintes abordagens foram utilizadas:
- **Uso de Dicionários:** Em vez de uma longa cadeia de `if/elif/else`, foi criado um dicionário (`ATAQUES`) como atributo de classe. Isso facilita a leitura e permite adicionar novos tipos de heróis no futuro sem alterar a lógica do método principal.
- **Validação Segura:** Utilização da estrutura `in` para verificar se o tipo digitado existe no dicionário antes de tentar buscar o ataque, evitando que o programa quebre.
- **Tratamento de Case-Sensitive:** Uso do `.lower()` na entrada do usuário para garantir que "Mago", "mago" ou "MAGO" funcionem da mesma forma.
- **Type Hints:** Adição de tipagem estática (ex: `nome: str`) nos parâmetros para melhor suporte da IDE e legibilidade.
- **Padronização:** Nome da classe em `PascalCase` (`Heroi`) e uso do bloco `if __name__ == "__main__":`, seguindo as convenções oficiais do Python.

---

## 💻 Código Final (Python)

```python
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