# 🧠 PucTech – Desafio Técnico 2025

Este repositório reúne as soluções desenvolvidas para os desafios do processo seletivo da **PucTech 2025**, abordando temas como análise de dados, construção de sistemas interativos e uso de machine learning.

---

## 📁 Desafio 1 – Análise de Dados Reais

**Arquivo:** `desafio_1_analise_dados.py`

Neste desafio, foi realizada uma análise exploratória dos dados coletados em um formulário respondido por alunos da universidade. O objetivo é extrair e representar visualmente informações úteis sobre as preferências de aprendizado.

### ✅ Etapas realizadas

- Carregamento do arquivo CSV com os dados dos alunos
- Seleção de colunas relevantes
- Tratamento de valores ausentes
- Geração de insights:
  - Total de respostas por linguagem de programação
  - Preferências por horário de estudo
  - Formatos de conteúdo (principal e secundário)
- Visualizações com gráficos:
  - Gráficos de barras e gráfico de pizza

📊 **Ferramentas utilizadas**:
- `pandas`, `matplotlib`

---

## 🧪 Desafio 2 – Sistema de Estoque para Farmácia

**Arquivo:** `sistema_estoque_farmacia.py`

Desenvolvimento de um sistema de terminal para controle de estoque de medicamentos em uma farmácia. O sistema permite cadastrar, atualizar, listar, remover medicamentos e processar pedidos.

### ✅ Funcionalidades

- Adicionar e atualizar medicamentos
- Listar estoque com status visual (🔴 crítico, 🟡 baixo, 🟢 ok)
- Remover medicamentos
- Processar pedidos automáticos
- Exibir resumo do estoque

📟 **Interface**: Menu interativo em terminal  
🔧 **Dependências**: Nenhuma (puro Python)

---

## 🚨 Desafio 3 – Mini Detector de Fraudes

**Arquivo:** `detector_fraudes.py` + `creditcard.csv`

Este script utiliza aprendizado de máquina (Random Forest) para detectar transações bancárias fraudulentas com base em dados reais.

### ✅ Etapas realizadas

- Carregamento do dataset `creditcard.csv`
- Separação entre features e rótulos
- Divisão dos dados em treino e teste (80/20)
- Treinamento de modelo `RandomForestClassifier`
- Avaliação com métricas (precision, recall, f1-score)

📈 **Bibliotecas utilizadas**:
- `pandas`, `scikit-learn`

---