
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Carregar os dados
data_path = "../DataMart/residuos_solidos.csv"
dataset = pd.read_csv(data_path)

# Codificar variáveis categóricas
encoder = LabelEncoder()
dataset["tipo_residuo_encoded"] = encoder.fit_transform(dataset["tipo_residuo"])
dataset["localizacao_encoded"] = encoder.fit_transform(dataset["localizacao"])

# Selecionar colunas para clustering
features = dataset[["quantidade_kg", "tipo_residuo_encoded", "localizacao_encoded"]]

# Padronizar os dados
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
dataset["cluster"] = kmeans.fit_predict(features_scaled)

# Salvar os resultados
output_path = "../DataMart/residuos_com_clusters.csv"
dataset.to_csv(output_path, index=False)
print(f"Clustering completo! Resultados salvos em {output_path}")
