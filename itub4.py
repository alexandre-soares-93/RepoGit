import yfinance as yf
import pandas as pd

# Define o ticker da ação ITUB4
ticker = "ITUB4.SA"  # ".SA" é usado para ações da B3 no Yahoo Finance

# Baixa os dados de 2025
dados = yf.download(ticker, start="2025-01-01", end="2025-03-28")

# Verifica se os dados foram baixados
if dados.empty:
    print("Nenhum dado encontrado para o período especificado.")
else:
    # Exibe os primeiros dados para análise
    print("Dados de preço da ação ITUB4 em 2025:")
    print(dados.head())

    # Exemplo de análise: cálculo da média de fechamento
    media_fechamento = dados['Close'].mean()
    print(f"Média de preço de fechamento em 2025: R$ {media_fechamento:.2f}")

    # Exemplo de análise: maior e menor preço de fechamento
    maior_preco = dados['Close'].max()
    menor_preco = dados['Close'].min()
    print(f"Maior preço de fechamento em 2025: R$ {maior_preco:.2f}")
    print(f"Menor preço de fechamento em 2025: R$ {menor_preco:.2f}")