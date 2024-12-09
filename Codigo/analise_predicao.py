
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Carregar os dados reais
data_path = "../DataMart/dados_reais_processados.csv"
data = pd.read_csv(data_path)

# Criar variável alvo baseada no número de pontos por bairro
data["residuos_total"] = data[
    ["residuo_construcao_civil", "residuo_solido_organico", "residuo_volumoso", "residuo_reciclavel"]
].apply(lambda row: sum(row == "SIM"), axis=1)

X = data[["latitude", "longitude", "residuos_total"]]
y = (data["bairro"].value_counts() > 1).astype(int).reindex(data["bairro"]).fillna(0).astype(int)

# Divisão de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predição e relatório
y_pred = model.predict(X_test)
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
