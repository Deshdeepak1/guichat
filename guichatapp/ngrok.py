from pyngrok import ngrok


def Ngrok(port,authtoken):
    if authtoken:
        ngrok.set_auth_token(authtoken)

    link=ngrok.connect(port,'tcp')
        
    return link
