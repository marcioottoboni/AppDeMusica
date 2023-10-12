import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Substitua as seguintes informações pelas suas credenciais do Spotify

class BaixadorMusicas:
    def __init__(self,cantores,estilos, id_cliente = '7ed12207f09d4b9883876da72dcc1892', senha_cliente = '05fcd8636b764ee99bcac6d0adb8648c'):
        self.cantores = cantores    
        self.estilos = estilos
        self.id_cliente = id_cliente
        self.senha_cliente = senha_cliente
        
    def Top_10_Musicas(self):
        #Inicializa o cliente
        client_credentials_manager = SpotifyClientCredentials(client_id=self.id_cliente, client_secret=self.senha_cliente)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Pesquisa o cantor
        resultado = sp.search(q=self.cantores, type='artist')
        items = resultado['artists']['items']

        # Retorna none
        if not items:
            print("Artista não encontrado.")
        return []
        id_artista = items[0]['id']
        # Buscar informações do artista e seus gêneros
        related_artists = sp.artist_related_artists(id_artista)
        print(f'{type(related_artists)}')

    def Todas_Discografia(self):
        print(f'Chamou a discografia')
        print(f'Os cantores digitados sao->{self.cantores}')
        print(f'Os estilos digitados sao->{self.estilos}')
        print(f'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')        
    def Top_10_Parecidos(self):
        print(f'Chamouos parecidos')
        print(f'Os cantores digitados sao->{self.cantores}')
        print(f'Os estilos digitados sao->{self.estilos}')
        print(f'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
