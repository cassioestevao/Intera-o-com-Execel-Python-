#Inicialização do Projetos
import pandas as pd # as pd significa que eu estou dando uma abreviação aquele modulo.

#abrir os 6 arquivos em execel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'] #listados conforme.

#função de repetição, esse mes acaba se tornando uma variavel 
for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #tab para incluir na função (For x in).
    print(tabela_vendas)


'''Verificar na coluna de vendas se algum vendendor bateu a meta(55.00)'''


'''Se for maior que 55 mil, enviar mensagem!nome, mes e vendas do vendedor'''

