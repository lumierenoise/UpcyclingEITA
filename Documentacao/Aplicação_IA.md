
# Relatório Final do Projeto EITA Upcycling

## Resultados Atualizados

### Análise de Pontos de Descarte por Tipo de Resíduo
Com base nos dados reais, a distribuição dos pontos de descarte está detalhada abaixo:
- **Resíduos Recicláveis**: 79 pontos (maioria dos pontos suportam esses materiais).
- **Resíduos de Construção Civil**: 8 pontos.
- **Resíduos Orgânicos e Volumosos**: Nenhum ponto identificado no dataset fornecido.

### Análise Geográfica
Os bairros com maior número de pontos de descarte são:
1. **São José**: 5 pontos.
2. **Torre**: 2 pontos.
3. Outros bairros incluem Arruda, Imbiribeira e Ibura com 2 pontos cada.

### Observações
- Há uma concentração de pontos para resíduos recicláveis, mas faltam pontos de descarte para resíduos volumosos e orgânicos.
- Algumas áreas, como **São José**, concentram mais pontos, enquanto outros bairros têm infraestrutura limitada.

### Impacto das Análises
Essas informações podem ser utilizadas para:
1. Identificar lacunas e propor novos pontos de descarte.
2. Melhorar a logística de coleta com base na localização dos pontos.
3. Incentivar práticas de descarte responsável, especialmente para resíduos com pouca infraestrutura.

### Gráficos Gerados
Os seguintes gráficos foram criados para visualização dos dados:
- **Distribuição dos Tipos de Resíduos Aceitos**.
- **Número de Pontos de Descarte por Bairro**.
- **Quantidade Total de Resíduos por Tipo (se aplicável).**

## Próximos Passos
Com base nesses resultados, recomenda-se:
1. Criar mapas interativos para visualização geográfica detalhada.
2. Propor soluções específicas para resíduos orgânicos e volumosos.
3. Expandir a análise para incluir dados de quantidades coletadas (se disponíveis).

---
**Arquivos disponíveis:** Gráficos, dados processados e documentação.

## Aplicação Prática de IA

### Clustering (KMeans)
Os dados geográficos foram agrupados em 3 clusters principais. Esses clusters representam agrupamentos naturais de pontos de descarte.

### Predição (Random Forest)
Utilizando os dados existentes, foi criada uma predição para identificar bairros prioritários para novos pontos de descarte. O modelo Random Forest alcançou os seguintes resultados:

**Relatório de Classificação:**
```
              precision    recall  f1-score   support

           0       0.86      0.95      0.90        20
           1       0.50      0.25      0.33         4

    accuracy                           0.83        24
   macro avg       0.68      0.60      0.62        24
weighted avg       0.80      0.83      0.81        24

```


## Bibliografia
1. **Portal de Dados Abertos da Cidade do Recife**: https://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos
2. **Scikit-learn Documentation**: https://scikit-learn.org/
3. **KMeans Clustering**: Aplicado para agrupar os pontos de descarte.
4. **Random Forest Classifier**: Utilizado para predição de bairros prioritários.

