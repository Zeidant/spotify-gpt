import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


#Credenciales
load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

#Autenticar con Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


playlist_link_file = "./playlist_link.txt"

#Leer enlace de archivo
with open(playlist_link_file) as file:
    playlist_link = file.readline().strip()
    

#Obtener canciones desde Spotify
results = sp.playlist_tracks(playlist_link)

#Guardar canciones
canciones_info = []

#Agregar canciones
for idx, item in enumerate(results['items']):
    track = item['track']
    nombre_cancion = track['name']
    artista_info = track['artists'][0]
    artista_nombre = artista_info['name']
    artista_id = artista_info['id']
    
    artista_data = sp.artist(artista_id)
    generos_artista = artista_data['genres']
    genero = ", " .join(generos_artista[:3]) if generos_artista else "Desconocido"
    
    #Agregar info
    cancion_info = {
    "Cancion": nombre_cancion,
    "Artista": artista_nombre,
    "Generos": genero
    }
    canciones_info.append(cancion_info)
    

#Guardar canciones en json
with open('canciones.json', 'w', encoding='utf-8') as json_file:
    json.dump(canciones_info, json_file, ensure_ascii=False, indent=2)


print("lista completa")
