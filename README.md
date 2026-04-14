# 🚀 Data Collection & Storage Pipeline (Lakehouse Transacional)

Este projeto implementa um pipeline de dados ponta a ponta (**End-to-End**) focado em **Ingestão, Processamento (Streaming e Batch)** e armazenamento em arquitetura **Lakehouse**.

O sistema simula transações de e-commerce em tempo real, gerencia o fluxo via mensageria e organiza os dados utilizando a **Medallion Architecture (Raw, Bronze, Silver)**, com suporte a **operações ACID** através do Apache Iceberg.

---

# 🎯 Objetivo

Construir um pipeline capaz de:

* Ingerir dados transacionais em tempo real
* Processar e tratar dados em múltiplas camadas
* Persistir dados em formato Open Table Format (Iceberg)
* Garantir propriedades **ACID (Atomicidade, Consistência, Isolamento, Durabilidade)**
* Demonstrar operações de **UPSERT, DELETE e Time Travel**
* Comparar performance entre **Iceberg vs Parquet**

---

# 🏗️ Arquitetura do Sistema

Fluxo completo de dados:

```text
Simulador → FastAPI → Kafka → Consumer → PostgreSQL (RAW) → Spark → Iceberg (Bronze → Silver)
```

<img width="700" height="200" alt="image" src="https://github.com/user-attachments/assets/aff844d8-8ba1-4d83-849e-1ef634b74de0" />


## 🔄 Componentes

* **Simulador:** Gera transações aleatórias (incluindo falhas de dados)
* **FastAPI (Producer):** Normaliza e publica eventos no Kafka
* **Apache Kafka:** Buffer de streaming garantindo resiliência
* **Consumer:** Consome eventos e persiste na camada RAW
* **PostgreSQL (Staging):** Armazena dados brutos em JSONB
* **PySpark + Iceberg:** Processamento distribuído e armazenamento transacional

---

# 🗂️ Arquitetura Medallion

| Camada | Tecnologia | Descrição                             |
| ------ | ---------- | ------------------------------------- |
| Raw    | PostgreSQL | Dados crus em JSONB                   |
| Bronze | Iceberg    | Dados estruturados e tipados          |
| Silver | Iceberg    | Dados tratados, limpos e enriquecidos |

---

# 🧹 Processamento de Dados (Silver)

Transformações aplicadas:

* **Casting:** Conversão de tipos (ex: valor → double)
* **Data Cleaning:** Remoção de registros inválidos
* **Imputação:** Substituição de valores nulos (valor → 0)
* **Deduplicação:** Remoção de duplicatas por ID
* **Enriquecimento:** Criação de colunas derivadas (ex: preço unitário)

---

# 🔥 Operações ACID com Iceberg

## ✔️ UPSERT (MERGE INTO)

Atualiza registros existentes e insere novos:

* Garante **atomicidade**
* Evita duplicação de dados

## ✔️ DELETE

Remoção de registros com garantia transacional:

* Exemplo: exclusão de registros inválidos (`valor = 0`)
* Validação realizada via contagem antes/depois

## ✔️ Time Travel

Permite consultar versões anteriores da tabela:

* Baseado em snapshots do Iceberg
* Suporte a auditoria e recuperação de dados

---

# ⚡ Benchmark de Performance

Comparação entre:

* **Parquet (arquivo tradicional)**
* **Apache Iceberg (tabela transacional)**

## Métricas avaliadas:

* Tempo de leitura (`count`)
* Tempo de consulta com filtro
* Eficiência em operações analíticas

---

# 📊 Propriedades ACID

| Propriedade  | Implementação                             |
| ------------ | ----------------------------------------- |
| Atomicidade  | MERGE INTO e DELETE                       |
| Consistência | Validação e tratamento de dados           |
| Isolamento   | Controle transacional do Iceberg          |
| Durabilidade | Persistência em storage com versionamento |

---

# 🛠️ Tecnologias Utilizadas

| Componente    | Tecnologia               |
| ------------- | ------------------------ |
| Linguagem     | Python                   |
| API           | FastAPI                  |
| Streaming     | Apache Kafka + Zookeeper |
| Banco         | PostgreSQL 15            |
| Processamento | PySpark (Spark 3.5.1)    |
| Table Format  | Apache Iceberg           |
| Orquestração  | Docker & Docker Compose  |
| Ambiente      | Jupyter Lab              |

---

# 📂 Estrutura do Projeto

```text
├── api/                # FastAPI (Producer)
├── simulator/         # Geração de dados
├── consumer/          # Consumo Kafka → Postgres
├── docker/
│   └── init/          # Scripts SQL
├── notebooks/         # ETL (Bronze / Silver)
├── Dockerfile.jupyter # Ambiente Spark
└── docker-compose.yml # Orquestração
```

---

# 🚀 Como Executar

## 1. Subir a infraestrutura

```bash
docker-compose up -d --build
```

## 2. Monitorar ingestão

```
http://localhost:8000/monitor
```

## 3. Executar processamento

* Rodar notebooks no Jupyter
* Executar transformações Bronze → Silver

---

# 📊 Resultados

| Operação | Parquet | Iceberg |
| -------- | ------- | ------- |
| Leitura  | Xs      | Ys      |
| Filtro   | Xs      | Ys      |

---

# 📌 Conclusão

O uso do Apache Iceberg permitiu:

* Implementação de operações ACID
* Versionamento de dados (Time Travel)
* Melhor governança e rastreabilidade
* Estrutura escalável para análise de dados

---

# 👩‍💻 Autora

Projeto desenvolvido como trabalho final de MBA em Engenharia de Dados.


Aline Ribeiro Ferreira
Arthur Girotti
Lais Hatsumi Sato
