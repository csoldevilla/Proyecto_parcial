import os
import warnings 
 
warnings.filterwarnings("ignore")

### Carpeta Dataset ####
location =  'C:/Users/Christhian/Documents/Cursos/DATA_ANALYTICS_CERTUS/3_20241763DATAOPSMA/proyecto_parcial/python/dataset'
print(location)

### validar si existe carpeta ###
if  not os.path.exists(location) : ### si la carpeta no existe
    ### creo la carpeta
    os.mkdir(location)
else: ### si la carpeta existe
    ### borrar contenido carpeta
    for root, dirs , files in  os.walk(location,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ### eliminar archivos de la carpeta
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ### eliminar la carpeta despues de estar vacio

### imprtar libreria api kaggle ###
from  kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

### Listar dataset disponibles ###
#print(api.dataset_list(search=''))

### Descargar Dataset ###

dataset_name = 'rahulvyasm/netflix-movies-and-tv-shows'
file_name    = 'netflix_titles.csv'
path_name    = location

api.dataset_download_file(dataset_name,file_name,path = path_name)
#api.dataset_download_file(dataset_name,file_name,path = path_name,force=True,quiet=False)
#api.dataset_download_file(dataset_name,file_name,path = location ,force=True,quiet=False)

api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=path_name,force=True,quiet=False,unzip=True)


