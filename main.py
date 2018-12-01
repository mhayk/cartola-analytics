import json
import requests
from lxml import html

pageContent=requests.get(
     'https://globoesporte.globo.com/futebol/brasileirao-serie-a/'
)
tree = html.fromstring(pageContent.content)
elements = tree.xpath('//*[@id="scriptReact"]')
# print(elements[0].text.split('\n')[8])
classificacao = elements[0].text.split('\n')[8]
# print(classificacao)
classificacao = classificacao[26:-1]
# print(classificacao)
output = json.loads(classificacao)
print(output['classificacao'])