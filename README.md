# 🏀 NBA Player Props Analyzer

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-orange)
![API](https://img.shields.io/badge/API-nba_api-red)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Ferramenta de **Sports Analytics com Python** que analisa estatísticas de jogadores da NBA usando dados oficiais da API da liga para gerar **insights automatizados para Player Props**.

Projeto construído seguindo um pipeline completo de Data Science:

API → limpeza → transformação → análise → insights


---

## 📊 Exemplo de saída do sistema

📊 Tendência recente:
```bash
📊 Últimos jogos analisados:

12/04/2026 | vs SAS → 1 ASSISTENCIAS
08/04/2026 | vs MEM → 10 ASSISTENCIAS
06/04/2026 | vs POR → 13 ASSISTENCIAS
04/04/2026 | vs SAS → 13 ASSISTENCIAS
01/04/2026 | vs UTA → 12 ASSISTENCIAS
29/03/2026 | vs GSW → 8 ASSISTENCIAS
27/03/2026 | vs UTA → 12 ASSISTENCIAS
25/03/2026 | vs DAL → 19 ASSISTENCIAS
24/03/2026 | vs PHX → 17 ASSISTENCIAS
22/03/2026 | vs POR → 14 ASSISTENCIAS

Resumo:
7/10 jogos (70.0%) com 11.0+ em ASSISTENCIAS nos últimos 10 jogos
```

🏀 Tendência vs adversário:
```bash
🏀 Jogos contra MIN:

01/03/2026 → 9 ASSISTENCIAS
25/12/2025 → 15 ASSISTENCIAS
15/11/2025 → 11 ASSISTENCIAS
27/10/2025 → 10 ASSISTENCIAS

Resumo:
2/4 jogos (50.0%) com 11.0+ em ASSISTENCIAS
```


---

## 🚀 Objetivo do projeto

Criar uma ferramenta automatizada capaz de responder perguntas como:

> O jogador está batendo essa linha recentemente?

> Ele performa melhor contra esse adversário?

> Existe tendência estatística confiável?


---

## 🧠 Tecnologias utilizadas

Python  
Pandas  
nba_api  
Requests  
VSCode  
Virtual Environment (venv)

Conceitos aplicados:

- Data Cleaning
- Feature Engineering
- API Integration
- Exploratory Data Analysis
- Sports Analytics
- Trend Detection


---

## 📂 Estrutura do projeto

```bash
AnaliseEsportivaNBA/

├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── tendencia_recente.py
│   └── tendencia_vs_time.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
├── .gitignore
└── README.md
```


---

## ⚙️ INSTALAÇÃO


Clone o projeto:
```bash
git clone <url-do-repositorio>
```

Crie ambiente virtual:

```bash
python -m venv venv
```

Ative ambiente virtual:
Windows:

```bash
venv\Scripts\activate
```
Linux / Mac:
```bash
source venv/bin/activate
```

Instale dependências:
```bash
pip install -r requirements.txt
```


---

## 📦 DEPENDÊNCIAS


Principais bibliotecas:
```bash
nba_api
pandas
```

Caso necessário instalar manualmente:
```bash
pip install nba_api pandas
```

---

## ▶️ EXECUTAR PROJETO


Rodar:
```bash
python src/main.py
```

Exemplo de input:
```bash
Nome do jogador: Nikola Jokic
Estatística: PONTOS
Linha: 25
Adversário: MIN
Últimos jogos: 10
```


---



---

## 📈 Funcionalidades atuais

✔ coleta automática da temporada mais recente  
✔ análise últimos X jogos  
✔ análise vs adversário  
✔ taxa de acerto vs linha da aposta  
✔ listagem detalhada dos jogos  
✔ formatação automática de datas  
✔ cálculo de aproveitamento estatístico  


---

## 🔬 Roadmap do projeto

Próximas melhorias planejadas:

- filtro por minutos jogados
- média da temporada
- média últimos jogos
- média vs adversário
- exportação CSV automática
- exportação Excel automática
- dashboard interativo
- interface web com Streamlit


---

## 📊 Pipeline de Data Science aplicado

Este projeto segue o fluxo clássico:
```bash
Data Collection → Data Cleaning → Feature Engineering → Analysis → Insight Generation
```

Utilizando dados reais da NBA API.


---

## 🎯 Aplicações reais

Este projeto pode ser aplicado em diferentes cenários de **Sports Analytics** e **Data Science prática**:

-  **Sports Analytics** — análise estatística de desempenho de jogadores
-  **Player Props Analysis** — identificação de tendências para linhas de apostas
-  **Performance Tracking** — acompanhamento de evolução recente por jogador
-  **Trend Detection** — detecção automática de padrões estatísticos
-  **Estudos de Data Science** — projeto aplicado com dados reais
-  **Portfolio profissional** — demonstração prática de pipeline com API + análise




---

##  👨‍💻 Autor

Bernardo Silva Sant Ana de Oliveira

Projeto desenvolvido como prática aplicada de:
 - Python para Data Science  
 - APIs esportivas  
 - Análise estatística  
 - Automação de insights NBA  


---

## ⭐ Próximos passos (versão avançada)

Evoluções planejadas para transformar o projeto em uma ferramenta completa de análise:

- Transformar em **CLI Tool profissional**
- Criar **Dashboard interativo com Streamlit**
- Desenvolver uma **API própria de análise de props**
- Adicionar médias automáticas (últimos jogos / temporada / vs adversário)
- Filtro por minutos jogados
- Exportação automática para CSV e Excel