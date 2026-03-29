-- ========================================
-- TABELA staging (dados crus)
-- ========================================

CREATE TABLE IF NOT EXISTS staging.transacoes_raw (
    id SERIAL PRIMARY KEY,
    payload JSONB,
    data_ingestao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);