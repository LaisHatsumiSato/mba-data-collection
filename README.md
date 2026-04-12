# Data Collection & Storage Pipeline 🚀

Este projeto implementa um pipeline de dados ponta a ponta (End-to-End) focado em *Ingestão, **Processamento Streaming e Batch* e armazenamento em arquitetura *Lakehouse. O sistema simula transações ecommerce em tempo real, gerencia o tráfego via mensageria e organiza os dados utilizando a **Medallion Architecture* (Raw, Bronze, Silver).

## 🏗️ Arquitetura do Sistema

O fluxo de dados segue o seguinte caminho:

1.  *Simulador*: Gera transações aleatórias (incluindo simulação de falhas de dados).
2.  *FastAPI (Producer)*: Recebe os dados, normaliza-os e atua como um Producer para o Kafka.
3.  *Apache Kafka*: Atua como o buffer de streaming, garantindo que nenhuma mensagem seja perdida entre a coleta e o armazenamento.
4.  *Consumer*: Consome os dados do Kafka e realiza a ingestão bruta (RAW) no PostgreSQL.
5.  *Staging*: Armazena os dados crus em formato JSONB para persistência inicial.
6.  *PySpark & Apache Iceberg*: Camada de processamento distribuído que transforma os dados brutos em tabelas analíticas otimizadas, seguindo as camadas:
      - Raw: Staging de dados
      - Bronze: Dados estruturados e tipados vindos do Staging.
      - Silver: Dados limpos, sem nulos, deduplicados via MERGE INTO e enriquecidos.

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia |
| :--- | :--- |
| *Linguagem* | Python | SQL |
| *Orquestração* | Docker & Docker Compose |
| *API / Gateway* | FastAPI |
| *Streaming* | Apache Kafka & Zookeeper |
| *Banco de Dados* | PostgreSQL 15 |
| *Processamento* | PySpark (Spark 3.5.1) |
| *Table Format* | Apache Iceberg |
| *IDE / Notebooks* | Jupyter Lab |

## 📂 Estrutura do Projeto

text
├── api/                  # FastAPI para recebimento de transações
├── simulator/            # Script de geração de dados randômicos
├── consumer/             # Consumidor Kafka para ingestão no Postgres
├── docker/
│   └── init/             # Scripts SQL de inicialização das tabelas
├── notebooks/            # Notebooks Jupyter para ETL (RAW/Bronze/Silver)
├── Dockerfile.jupyter    # Configuração do ambiente Spark + Iceberg
└── docker-compose.yml    # Orquestração de todos os containers

# 🚀 Como Executar

1.*Subir a infraestrutura*

Certifique-se de ter o Docker instalado e execute:


docker-compose up -d --build


Isso iniciará o Kafka, PostgreSQL, a API, o Simulador e o ambiente Jupyter.

2. *Monitorar a Ingestão*

Você pode acessar o monitor em tempo real da API em:


   http://localhost:8000/monitor.
   
3. *⚙️ Detalhes de Processamento*

Camada Silver (Tratamento e Qualidade)

O processo de transformação na camada Silver inclui:
  - Casting: Conversão de tipos (ID para Int, Valor para Double).
  - Data Cleaning: Remoção de registros com transacao_id nulo.
  - Imputação: Preenchimento de valores faltantes (ex: valor nulo vira 0).
  - Deduplicação: Uso de dropDuplicates baseado no ID único da transação.
  - Upsert (Merge): Implementação do MERGE INTO do Iceberg para garantir que registros atualizados substituam os antigos sem gerar duplicatas na camada analítica.

# 📊 Detalhes das Camadas de Dados

| Camada | Tecnologia | Descrição | 
| *Staging* | PostgreSQL | Dados crus salvos como JSONB conforme recebidos da API. |
| *Bronze* | Iceberg | Dados tipados e estruturados, mas ainda contendo inconsistências. |
| *Silver* | Iceberg | Dados limpos, sem nulos e com colunas enriquecidas para análise. |
