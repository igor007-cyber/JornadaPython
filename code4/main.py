import flet as ft

# funçaõ principal
def main(pagina):
    
    # A FUNÇÃO PARA PODER CRIAR O TUNNEL DE COMUNICAÇÃO
    def tunnel(Mensagem):
        texto_chat = ft.Text(Mensagem)
        chat.controls.append(texto_chat)
        pagina.update()
    
    pagina.pubsub.subscribe(tunnel) # Criar o tunnel de comunicação
    
    
    titulo = ft.Text('ChatSimple')
    
    titulo_janela = ft.Text('Bem vindo ao ChatSimple')
    campo_user = ft.TextField(label='Escreva seu nome no chat')
    
    chat = ft.Column()
    
    def enviar_mensagem(evento):
        mensagem = campo_mensagem.value
        nome = campo_user.value
        Mensagem = f'{nome}: {mensagem}'
        pagina.pubsub.send_all(Mensagem) # enviando todas as mensagens
        campo_mensagem.value = ''
        pagina.update()
        
    campo_mensagem = ft.TextField(label='Digite suma mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_mensagem) 
    
    linha_mensagem =ft.Row([campo_mensagem,botao_enviar])
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        
        pagina.add(chat)
        pagina.add(linha_mensagem)
        Mensagem = f'{campo_user.value} entrou no chat'
        pagina.pubsub.send_all(Mensagem) 
        pagina.update()
    
    
    botao_janela = ft.ElevatedButton('entrar no chat', on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_user, actions=[botao_janela])
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    


# roda a aplicação
ft.app(main, view=ft.WEB_BROWSER) # aqui tu escolhe se vai rodar no site ou nao 