"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd 


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    
    lines = lines[4:]

    registros = []
    cluster = None
    cantidad = None
    porcentaje = None
    palabras = ""

    for line in lines:

        if line.startswith("----") or line.strip() == "":
            continue

       
        if line[:7].strip().isdigit():

            
            if cluster is not None:
                registros.append([cluster, cantidad, porcentaje, palabras.strip()])
                palabras = ""

           
            cluster = int(line[0:7].strip())
            cantidad = int(line[7:17].strip())
            porcentaje = float(line[17:32].strip().replace("%", "").replace(",", "."))
            palabras = line[32:].strip()

        else:
            
            palabras += " " + line[32:].strip()

    
    registros.append([cluster, cantidad, porcentaje, palabras.strip()])

    
    df = pd.DataFrame(
        registros,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ]
    )

    
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r",\s*", ", ", regex=True)
        .str.strip(". ")
    )

    return df