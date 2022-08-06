import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

def download_pubmed (keyword):
    """
    Funcion que pide como input la palabra de busqueda en tipo str del pubmed y como output guarda un documento con extensión
    txt que contiene los datos de la busqueda
    """ 
    Entrez.email = "nicole.torres@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term=keyword+"[Title]",
                        usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text", 
                       retstart=0,
                       retmax=543, 
                       webenv=webenv,
                       query_key=query_key)

    out_handle = open("data/"+keyword, "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list 

import re 
import matplotlib.pyplot as plt
from collections import Counter

def science_plots(data):
    """
    Funcion que pide como entrada la data de busqueda anterior y como resultado muestra un grafico tipo pastel que indica 
    a los cinco paises de origen de autores que presentaron mayor frecuencia. 
    """ 
    with open("data/"+data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    unique_countries = list(set(countries_1))
    conteo=Counter(countries_1)
    resultado={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ordenar = (sorted(resultado.values()))
    ordenar.sort(reverse=True)
    import operator
    pais = []
    contador = []
    
    reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        pais.append(name[1][0])
        contador.append(resultado[name[1][0]])
    five_p = pais[0:5] 
    five_c = contador [0:5]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(five_c, labels = five_p)
    (plt.savefig("img/"+data, dpi=300, bbox_inches='tight'))
    plt.show()









