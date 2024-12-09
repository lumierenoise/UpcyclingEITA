
import pandas as pd
from sklearn.cluster import KMeans

# Carregar os dados reais
data_path = "../DataMart/dados_reais_processados.csv"
data = pd.read_csv(data_path)

# Selecionar coordenadas para clustering
coords = data[["latitude", "longitude"]].dropna()

# Aplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
data["cluster"] = kmeans.fit_predict(coords)

# Salvar os resultados com clusters
output_path = "../DataMart/dados_com_clusters.csv"
data.to_csv(output_path, index=False)
print(f"Clustering completo! Resultados salvos em {output_path}")
