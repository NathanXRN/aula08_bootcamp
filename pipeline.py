from etl import pipeline

pasta_argumento: str = 'data'
formato_de_saida: list = ["csv", "parquet"]

pipeline(pasta_argumento, formato_de_saida)