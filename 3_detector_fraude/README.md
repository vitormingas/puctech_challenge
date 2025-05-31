# 🚨 Mini Detector de Fraudes

Este projeto utiliza machine learning para detectar transações bancárias fraudulentas com base em um dataset de cartões de crédito.

---

## 🧪 Funcionalidades

- Leitura do dataset `creditcard.csv`
- Separação entre variáveis preditoras (X) e rótulo (y)
- Divisão dos dados em treino e teste
- Treinamento de modelo `RandomForestClassifier`
- Geração de relatório de classificação (precision, recall, f1-score)

---

## 🗂️ Arquivos

- `detector_fraudes.py`: script principal
- `creditcard.csv`: base de dados

---

## ▶️ Como Executar

1. Instale as bibliotecas necessárias:

```bash
pip install pandas scikit-learn
```

2. Coloque o arquivo `creditcard.csv` na mesma pasta do script.

3. Execute o script:

```bash
python detector_fraudes.py
```

---

## 👨‍💻 Autor

Desenvolvido por **vitormingas**  
Para o Processo Seletivo da **PucTech 2025**
