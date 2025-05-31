# 🚨 Mini Detector de Fraudes

Este projeto utiliza aprendizado de máquina para detectar transações bancárias fraudulentas com base em um dataset real de cartões de crédito.

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
- `creditcard.csv`: base de dados (não incluída no repositório)

---

## 📥 Download do Dataset

O arquivo `creditcard.csv` não está incluído neste repositório devido ao seu tamanho (>100MB).

Você pode baixá-lo manualmente pelo link abaixo:

🔗 [Download via Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

Após o download, coloque o arquivo na mesma pasta que o script `detector_fraudes.py`.

---

## ▶️ Como Executar

1. Instale as bibliotecas necessárias:

```bash
pip install pandas scikit-learn
```

2. Execute o script:

```bash
python detector_fraudes.py
```

---

## 👨‍💻 Autor

Desenvolvido por **vitormingas**  
Para o Processo Seletivo da **PucTech 2025**
