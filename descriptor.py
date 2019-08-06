import json, hashlib

# Função que retorna o índice da letra cifrada.
def geraIndex(ind,numb):
    return (ind + numb-1) %26

#Função que retorna o alfabeto cifrado   
def alfaCif(numb,alfa):
    alfa_cif = ""
    for i in alfa:
        alfa_cif += alfa[geraIndex(alfa.index(i),int(numb)-1)]

    return alfa_cif

# Função que descripta a string, fazendo a referência entre
# do indice da letra no alfabeto cifrado e passando para o alfabeto normal
def descriptor(numb,cifra):    
    alfa = "abcdefghijklmnopqrstuvwxyz"
    alfa_cif = alfaCif(numb,alfa)
    new_string = ''
    for i in cifra:
        if i in alfa:
            decif = alfa_cif[alfa.index(i)]
        else:
            decif = i

        new_string += decif 

    return new_string

# Retorna um texto encriptado
def encrypt(numb,cifra):    
    alfa = "abcdefghijklmnopqrstuvwxyz"
    alfa_cif = alfaCif(numb,alfa)
    new_string = ''
    for i in cifra:
        if i in alfa:
            decif = alfa[alfa_cif.index(i)]
        else:
            decif = i

        new_string += decif 

    return new_string

#Retorna o resumo do texto feito com SHA1
def resumoSha1(string):
    """Com o uso da biblioteca hashlib usando o método sha1 passo a 
    a string codificada em utf-8 e tenho como retorno um objeto sha1 do tipo 
    hash, enseguida converto e retorno esse objeto em uma string hexadecimal """
    resumo = hashlib.sha1(string.encode('utf-8'))
    return  resumo.hexdigest()  

#Abertura e Chamda dos Dados do arquivo.
file = open("fileApi.json")
obJson = json.load(file)
file.close()

#recebe o texto descriptado e o resumo 
descripted = descriptor(obJson.get('numero_casas',0),obJson.get('cifrado',0).lower())
resumo = resumoSha1(descripted)

#Setando o texto decifrado e o resumo no objeto json
obJson['decifrado'] = descripted
obJson['resumo_criptografico'] = resumo

#Escrevendo no arquivo de respostas
answer = open("answer.json","w")
answer.write(json.dumps(obJson))
answer.close()
