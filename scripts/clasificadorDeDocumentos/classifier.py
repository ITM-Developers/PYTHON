import os
import shutil
import filetype 

def organizeByMIME( srcPath, destPath):
    
    #Creamos el directorio a donde vamos a mover los archivos ordenados
    if not( os.path.exists(destPath) ):
        os.mkdir(destPath, 0o777)

    # Itineramos todos los archivos para clasificarlos
    listaDeArchivos = os.listdir(srcPath)

    for nombreDelArchivo in listaDeArchivos:
        fullpath = srcPath + nombreDelArchivo

        #Validamos si es un fichero para determinar su tipo
        if ( os.path.isfile(fullpath) ):

            tipoDeFichero = filetype.guess(fullpath)

            if (tipoDeFichero is None):
                print('File: ', nombreDelArchivo, 'MIME: UNKNOWN')
            else:
                directorioDestino = os.path.join(destPath, tipoDeFichero.extension)
                
                if not( os.path.exists(directorioDestino) ):
                     os.mkdir(directorioDestino, 0o777)
                
                shutil.move(srcPath + nombreDelArchivo, os.path.join(directorioDestino, nombreDelArchivo))
                # print('File: ', nombreDelArchivo, ' EXTNSION: ', tipoDeFichero.extension)