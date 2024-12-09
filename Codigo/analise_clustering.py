
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carregar os dados reais
data_path = "../DataMart/dados_reais_processados.csv"
data = pd.read_csv(data_path)

# Filtrar coordenadas para clustering
coords = data[["latitude", "longitude"]].dropna()

# Aplicar KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data["cluster"] = kmeans.fit_predict(coords)

# Salvar os resultados com os clusters
output_path = "../DataMart/dados_com_clusters.csv"
data.to_csv(output_path, index=False)
print(f"Clustering concluído! Dados salvos em {output_path}")

# Gerar gráfico de clusters
plt.figure(figsize=(10, 6))
for cluster in data["cluster"].unique():
    cluster_data = data[data["cluster"] == cluster]
    plt.scatter(cluster_data["longitude"], cluster_data["latitude"], label=f"Cluster {cluster}")
plt.title("Clusters de Pontos de Descarte")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.tight_layout()
plt.savefig("../Resultados/clusters_pontos_descarte.png")
plt.close()
