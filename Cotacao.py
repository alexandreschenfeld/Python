API_URL = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
import requests
def obter_cotacao(moeda_origem, moeda_destino):
    """
    Obtém a cotação atual entre duas moedas.
    
    Args:
        moeda_origem (str): Código da moeda de origem (ex: USD, EUR, BTC)
        moeda_destino (str): Código da moeda de destino (ex: BRL)
    
    Returns:
        float: Valor da cotação
        
    Raises:
        RequestException: Se houver erro na requisição
        KeyError: Se o par de moedas não for encontrado
    """
    try:
        resposta = requests.get(API_URL)
        resposta.raise_for_status()
        dados = resposta.json()
        par_moedas = f"{moeda_origem}{moeda_destino}"
        return float(dados[par_moedas]["bid"])
    except requests.RequestException as erro:
        raise Exception(f"Erro ao obter cotação: {erro}")
    except KeyError:
        raise Exception(f"Par de moedas {par_moedas} não encontrado")
    except Exception as erro:
        raise Exception(f"Erro desconhecido: {erro}")
    else:
        return float(dados[par_moedas]["bid"])
    finally:
        print("Finalizando...")

print(obter_cotacao("USD", "BRL"))
