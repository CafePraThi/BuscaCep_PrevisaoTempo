import requests

def busca_cep():
    print("===========  PESQUISA POR CEP  ===========")
    cep = input('Digite o CEP que deseja encontrar: ')
    link = f'https://viacep.com.br/ws/03624020/json/'

    req = requests.get(link)

    if req.status_code == 200:
        req_dic = req.json()
        localidade = req_dic['localidade']

        print("CEP: {}".format(req_dic['cep']))
        print("Longadouro: {}".format(req_dic['logradouro']))
        print("Complemento: {}".format(req_dic['complemento']))
        print("Bairro: {}".format(req_dic['bairro']))
        print("Cidade: {}".format(req_dic['localidade']))
        print("Estado: {}".format(req_dic['uf']))
        clima(localidade)
    else:
        print('ERRO NA CONSULTA, VERIFIQUE OS DADOS E TENTE NOVAMENTE!')
        
def pesquisar_cep():
    print("===========  PESQUISA POR ENDEREÇO  ===========")

    uf = input("Informe a sigla do Estado: ")
    localidade = input("Informe a Cidade: ")
    longadouro = input("Informe o Longadouro/Rua: ")
    link = f'https://viacep.com.br/ws/{uf}/{localidade}/{longadouro}/json/'

    req = requests.get(link)

    if req.status_code == 200:
        req_dic = req.json()
        print("Segue os dados do Endereço informado: \n")
        
        for endereco in req_dic:
            print("CEP: {}".format(endereco['cep']))
            print("Longadouro: {}".format(endereco['logradouro']))
            print("Complemento: {}".format(endereco['complemento']))
            print("Bairro: {}".format(endereco['bairro']))
            print("Cidade: {}".format(endereco['localidade']))
            print("Estado: {}".format(endereco['uf']))

        localidade = endereco['localidade']
        clima(localidade)
    else:
        print('ERRO NA CONSULTA, VERIFIQUE OS DADOS E TENTE NOVAMENTE!')

def clima(localidade):
    api_key= 'd52dc5031b71c4f4534ae895e5b94fd8'
    link = f'http://api.openweathermap.org/data/2.5/weather?q={localidade}&appid={api_key}&units=metric&lang=pt_br'

    req_clima = requests.get(link)

    print("===========  PREVISÃO DO TEMPO  ===========")

    if req_clima.status_code == 200:
        req_clima_dic = req_clima.json()
        description = req_clima_dic['weather'][0]['description']
        temp = req_clima_dic['main']['temp']
        max_temp = req_clima_dic['main']['temp_min']
        min_temp = req_clima_dic['main']['temp_max']

        print("A previsão de tempo para {} é: ".format(localidade))
        print("Tempretatura atual: {}ºC".format(temp))
        print("Descrição: {}".format(description))
        print("Temperatura Maxima de: {} ºC".format(max_temp))
        print("Temperatura Minima de: {} ºC".format(min_temp))
    else:
        print('ERRO NA CONSULTA, TENTE NOVAMENTE!')

choice = int(input('Selecione: \n 1 -Buscar por CEP \n 2 -Buscar por Endereço \n'))

if choice == 1:
    busca_cep()
elif choice == 2:
    pesquisar_cep()
else:
    print('Selecione uma opção Valida!!')