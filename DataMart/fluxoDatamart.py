import matplotlib.pyplot as plt
import networkx as nx

# Criar um fluxo visual usando NetworkX
G = nx.DiGraph()

# Adicionar etapas do fluxo
G.add_node("1. Coleta de Dados", pos=(0, 4))
G.add_node("2. Pré-Processamento", pos=(0, 3))
G.add_node("3. Clustering (KMeans)", pos=(-1, 2))
G.add_node("4. Predição (Random Forest)", pos=(1, 2))
G.add_node("5. Criação do DataMart", pos=(0, 1))
G.add_node("6. Visualização de Resultados", pos=(0, 0))

# Adicionar conexões entre as etapas
G.add_edges_from([
    ("1. Coleta de Dados", "2. Pré-Processamento"),
    ("2. Pré-Processamento", "3. Clustering (KMeans)"),
    ("2. Pré-Processamento", "4. Predição (Random Forest)"),
    ("3. Clustering (KMeans)", "5. Criação do DataMart"),
    ("4. Predição (Random Forest)", "5. Criação do DataMart"),
    ("5. Criação do DataMart", "6. Visualização de Resultados")
])

# Configurar posições dos nós
pos = nx.get_node_attributes(G, 'pos')

# Configurar visualização
plt.figure(figsize=(12, 8))
nx.draw(
    G, pos, with_labels=True, node_size=4000, node_color='lightblue',
    font_size=10, font_weight='bold', edge_color='gray', arrowsize=20
)
plt.title("Fluxo Visual: Construção do DataMart", fontsize=14, fontweight='bold')

# Salvar ou mostrar o gráfico
plt.savefig("fluxo_construcao_datamart.png")  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico
