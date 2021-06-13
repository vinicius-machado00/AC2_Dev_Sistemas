#pip install totalvoice
from totalvoice.cliente import Cliente

# Utilizando API do TotalVoice para disparo de SMS
#
# INTEGRANTES:
#
# 1800982 - Clarissa Leme
# 1801036 - Higor Casemiro
# 1800984 - João Vitor Paiva
# 1701912 - Vinicius Machado



#region Conexão com API

#Insira aqui o Token de Acesso

token_pessoal = Cliente('3055e3edd8119f41aa4ceb537c85c36c', 'api.totalvoice.com.br')
token_facul = Cliente('4c6453c71ee092395f0da557c309ae5b', 'api.totalvoice.com.br')
# coding=utf-8
def Token(cod_api): 
    token = Cliente(str(cod_api),'api.totalvoice.com.br')
    return token

#endregion
#Insira a mensagem a ser enviada com até 160 caracteres. 
Mensagem = '''Vlw por hj rapaziada !!!! 
            Ass: Vinícius Machado :)'''

#Basta instanciar a classe Cliente e passar os parametros necessários. 

vinicius= token_pessoal.sms.enviar('11977207283',Mensagem,None,None,None)
higor = token_pessoal.sms.enviar('11949957248',Mensagem,None,None,None)
clarissa = token_facul.sms.enviar('11987198301',Mensagem,None,None,None)
paiva = token_facul.sms.enviar('11965959525',Mensagem,None,None,None)

print('clarissa: ',clarissa)
print('vinicius' , vinicius)
print('higor :',higor)
print('paiva :',paiva)
