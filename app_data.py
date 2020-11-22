# O arquivo main.py importa private.app_data
# Tal módulo contém dados privados como senhas e tokens do bot
# Portanto a pasta foi adicionada ao .gitignore de modo a manter tais informações privadas
# Este arquivo é um arquivo base contendo as funções sem os dados (são gets comuns)

def get_client_id():
    return "yours client id"

def get_client_secret():
    return "yours client secret"

def get_public_key():
    return "your app's public key"

def get_oauth2_url():
    return "your app's url"



