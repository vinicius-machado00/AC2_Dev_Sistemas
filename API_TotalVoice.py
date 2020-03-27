# Marmifit -> Utilizando API do TotalVoice para disparo de SMS
#
# INTEGRANTES:
#
# 1800982 - Clarissa Leme
# 1801036 - Higor Casemiro
# 1800984 - João Vitor Paiva
# 1701912 - Vinicius Machado

from totalvoice.cliente import Cliente
import json

def Acesso_TotalVoice():
    api_token = 'Chave_de_acesso_AQUI'
    token = Cliente(api_token,'api.totalvoice.com.br')
    return token

#Função SMS
#Parametros:
#   telefone_user -> string ->  DDD + Telefone
#   Mensagem -> string -> Até 160 caracteres

def SMS(telefone_user, mensagem):
    Login = Acesso_TotalVoice()
    retorno = Login.sms.enviar(str(telefone_user),mensagem,None,None,None)
    #Retorna bytes então há uma conversão p/ JSON
    retorno_tratado = json.loads(retorno.decode())
    if(retorno_tratado['status'] == 200):
        return "Mensagem enviada com sucesso"
    else:
        return "Erro no envio"
    return retorno_tratado

#Print apenas para demonstração da função.
print(SMS('Insira DDD + Telefone','Insira_sua_Mensagem'))






