"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    with open("clusters_report.txt", "r") as archivo:
        diccionario = {"cluster": [],
                       "cantidad_de_palabras_clave": [],
                       "porcentaje_de_palabras_clave": [],
                       "principales_palabras_clave" : ""}

        lineas_organizadas = []

        for linea in (archivo.readlines()[4:]):
            linea = linea.replace("\n","")
            datos = list(filter(lambda x: x != "",linea.split(" ")))


            if "%" in datos:
                    lineas_organizadas.append([elemento for elemento in datos[:4]])
                    lineas_organizadas[-1].append(" ".join(datos[4:]))

            elif datos:
                    lineas_organizadas[-1][-1] = lineas_organizadas[-1][-1] + " ".join(datos)
            lineas_organizadas[-1][-1] += " "


        diccionario["cluster"] =  ([int(lista[0]) for lista in lineas_organizadas])
        diccionario["cantidad_de_palabras_clave"] = ([int(lista[1]) for lista in lineas_organizadas])
        diccionario["porcentaje_de_palabras_clave"] = ([float(lista[2].replace(",",".")) for lista in lineas_organizadas])
        diccionario["principales_palabras_clave"] = ([lista[-1].strip().replace(".","") for lista in lineas_organizadas])

        return pd.DataFrame(diccionario)








