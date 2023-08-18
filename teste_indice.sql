-- Apagar a tabela de dados caso exista
DROP TABLE IF EXISTS test_index_hc;

-- Criação da tabela para inserção de dados
CREATE TABLE test_index_hc(
  id SERIAL,
  name TEXT
);

-- Inserção de dados
INSERT INTO test_index_hc(name)
SELECT 'higor' FROM generate_series(1, 500000);

INSERT INTO test_index_hc(name)
SELECT 'thais' FROM generate_series(1, 500000);

-- Resultado antes da criação do índice
EXPLAIN ANALYZE SELECT * FROM test_index_hc WHERE ID = 15000;

-- Criação do índice 
CREATE INDEX test_idx_hc ON test_index_hc(id);

--5 check the result after index
EXPLAIN ANALYZE SELECT * FROM test_index_hc WHERE ID = 15000;