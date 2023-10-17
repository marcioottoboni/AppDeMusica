import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Substitua as seguintes informações pelas suas credenciais do Spotify

class Spotify:
    def __init__(self,cantor,estilos, id_cliente = '7ed12207f09d4b9883876da72dcc1892', senha_cliente = '05fcd8636b764ee99bcac6d0adb8648c'):
        self.cantor = cantor    
        self.estilos = estilos
        self.id_cliente = id_cliente
        self.senha_cliente = senha_cliente
    def Top_10_Musicas(self):
        dic_top10_musicas = {}
        list_top10_musicas = []
        client_credentials_manager = SpotifyClientCredentials(client_id=self.id_cliente, client_secret=self.senha_cliente)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        resultados = sp.search(q=f'artist:{self.cantor}', type='artist', limit=1)
    
        if resultados['artists']['items']:
            id_artista = resultados['artists']['items'][0]['id']
            top_musicas = sp.artist_top_tracks(id_artista)
            dic_top10_musicas[self.cantor] = []
        
            print(f'As 10 principais músicas de {self.cantor}:')
            for i, musica in enumerate(top_musicas['tracks'][:10], start=1):
                print(f'{i}. {musica["name"]}')
                list_top10_musicas.append(musica["name"])
            dic_top10_musicas[self.cantor] =  list_top10_musicas
        return dic_top10_musicas
    def Todas_Discografia(self):
        dic_discografia= {} 
        dic_disco = {}
        client_credentials_manager = SpotifyClientCredentials(client_id=self.id_cliente, client_secret=self.senha_cliente)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        resultado = sp.search(q=f'artist:{self.cantor}', type='artist', limit=1)
        if resultado['artists']['items']:
            id_artista = resultado['artists']['items'][0]['id']
            discografia = sp.artist_albums(id_artista, album_type='album')
            print(f'Discografia de {self.cantor}:')
            
            for album in discografia['items']:
                faixas = sp.album_tracks(album['id'])
                dic_disco[album["name"]] = []
                print(f'Disco ->{album["name"]}({album["release_date"]})') 
                musicas_disco = []                
                for faixa in faixas['items']:
                    print(f'- {faixa["track_number"]}. {faixa["name"]}')
                    musicas_disco.append(faixa["name"])
                dic_disco[album["name"]] = musicas_disco
            dic_discografia[self.cantor] =  dic_disco
            return dic_discografia
    def Top_20_Parecidos(self):
        lista_parecidos = []
        print(f'Chamouos parecidos')
        #Inicializa o cliente
        client_credentials_manager = SpotifyClientCredentials(client_id=self.id_cliente, client_secret=self.senha_cliente)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Pesquisa o cantor
        resultado = sp.search(q=self.cantores, type='artist')
        items = resultado['artists']['items']

        # Retorna none
        if resultado['artists']['items']:
            id_artista = resultado['artists']['items'][0]['id']
            artistas_similares = sp.artist_related_artists(id_artista)
            return []
        
        print('20 Principais Artistas Semelhantes:')
        for artista in artistas_similares['artists'][:20]:
            lista_parecidos.append(artista["name"])            
        return lista_parecidos
