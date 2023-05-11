import aiohttp
import asyncio

async def main():
# Primeiramente definimos uma sessão de cliente com aiohttp?
    async with aiohttp.ClientSession() as session:
        #Em seguida, com nossa sessão, executamos uma resposta get em uma única URL:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            #Em terceiro lugar, observe como usamos a palavra-chave await na frente de response.text() assim:
            # response.text retorna o conteudo da resposta em unicode. Basicamente, refere-se ao conteudo da resposta binaria.
            #As solicitações do Python geralmente são usadas para buscar o conteúdo de uma URI de recurso especifico.
            #Sempre que fazemos uma solicitação para um URI especificado por meio do Python, ele retorna um objeto de resposta.
            #Agora, esse objeto de resposta seria usado para acessar determinados recursos, como conteúdo, cabeçalhos, etc
            html = await response.text()
#await: A segunda significa que a corrotina será paralisada naquele ponto aguardando um resultado futuro. Em outras palavras,
#o controle de execução será dado á outra corroutina e só sera retomado quando o resultado ficar pronto.
            print("Body:", html[:15], "...")
#Por fim ele mostra o tipo de conteudo e especificamente a linha numero 15, posso colocar para ele mostrar a linha 5:15 e ignorar os 5 primeiros digitos

#Por fim, executamos asyncio.run(main()), isso cria um loop de eventos e executa todas as tarefas que forem concluídas, o loop de eventos será destruído automaticamente
asyncio.run(main())
