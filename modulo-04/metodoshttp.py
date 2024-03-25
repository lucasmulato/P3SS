# Importar a biblioteca requests
import requests
# Passar uma variavel com o host
host = "http://testphp.vulnweb.com/"
# Passar os métodos existentes
metodos = ['OPTIONS', 'GET', 'POST', 'DELETE', 'TRACE', 'CONECT']
# Criar um for loop para ele testar cada metoo
for metodo in metodos:
    # Validação de cada metodo existente para ver se funciona no host
    resposta = requests.requests(metodo, host)
    print(metodo, "->", resposta.reason)
    