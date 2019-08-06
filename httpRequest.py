import requests

#Variáveis Globais
token = ''
url  = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=%s'%token
#acesso a Api
def getApi():
    
    request = requests.get(url)

    jsonFile = open('fileApi.json','w')

    jsonFile.write(request.text)

    jsonFile.close()
    return None

def postApi():
    file = {'answer':open('answer.json','r')}

    post = requests.post(url, data=file)

    post.response()

    
