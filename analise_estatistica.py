import json

usuarios = [
    {"nome": "Ana", "idade": 18, "tempo_medio_uso": 35, "acessos": 5},
    {"nome": "Carlos", "idade": 25, "tempo_medio_uso": 50, "acessos": 8},
    {"nome": "João", "idade": 17, "tempo_medio_uso": 20, "acessos": 3},
    {"nome": "Marina", "idade": 30, "tempo_medio_uso": 45, "acessos": 6},
    {"nome": "Beatriz", "idade": 22, "tempo_medio_uso": 38, "acessos": 4},
    {"nome": "Rafaela", "idade": 19, "tempo_medio_uso": 41, "acessos": 7}
]

with open("usuarios.json", "w") as arquivo:
    json.dump(usuarios, arquivo, indent=4)

import json
import statistics
import matplotlib.pyplot as plt

# Lê os dados do arquivo JSON
with open('usuarios.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Separa os dados em listas
idades = [usuario["idade"] for usuario in dados]
acessos = [usuario["acessos"] for usuario in dados]
tempos = [usuario["tempo_medio_uso"] for usuario in dados]
nomes = [usuario["nome"] for usuario in dados]

# Função para mostrar estatísticas
def mostrar_estatisticas(nome, lista):
    print(f"\n{nome.upper()}")
    print("Média:", statistics.mean(lista))
    print("Mediana:", statistics.median(lista))
    try:
        print("Moda:", statistics.mode(lista))
    except statistics.StatisticsError:
        print("Moda: Não existe moda (valores únicos)")

# Estatísticas
mostrar_estatisticas("Idades", idades)
mostrar_estatisticas("Acessos", acessos)
mostrar_estatisticas("Tempo Médio de Uso (min)", tempos)

# Gráfico 1 - Acessos por usuário
plt.figure(figsize=(8,4))
plt.bar(nomes, acessos, color='skyblue')
plt.title("Acessos por Usuário")
plt.xlabel("Usuário")
plt.ylabel("Quantidade de Acessos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2 - Tempo médio de uso
plt.figure(figsize=(8,4))
plt.bar(nomes, tempos, color='lightgreen')
plt.title("Tempo Médio de Uso (min) por Usuário")
plt.xlabel("Usuário")
plt.ylabel("Tempo (min)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()