def busca_cotacao():
    import requests
    from datetime import datetime
    try:
        response = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

        dados = response.json()

        data = datetime.strptime(dados['USD']['create_date'], '%Y-%m-%d %H:%M:%S')
        data_convertida = data.strftime('%d/%m/%Y %H:%M:%S')

        return 'Cotação do ' + dados['USD']['name'] + ' é R$ '+ dados['USD']['bid'] + ' Atualizado em: ' + data_convertida
    except Exception as e:
        return 'Erro ao consultar a cotação: ' + str(e)