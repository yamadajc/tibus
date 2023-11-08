import pandas as pd
import numpy as np
import re




def daytime (x, pattern):
    """ funcion que devuelve el periodo del dia en el que se produjo el ataque

    Args:
        x (str): string que contiene la fecha del ataque 
        pattern (_type_): patron de busqueda

    Returns:
        np.nan: devuelve un nan en el caso de que no se encuentre el patron
        str : devuelve el estado de la fecha del ataque (Morning, Afternoon, Evening, Night)
    """
    res = re.findall(pattern, x)
    res="".join(res)
    if res in ["06","07","08","09","10","11", "Morning"]:
        return "Morning"
    elif res in ["12","13","14","15","16","17", "Afternoon"]:
        return "Afternoon"
    elif res in ["18","19","20","21","22","23", "Evening"]:
        return "Evening"
    elif res in ["24","01","02","03","04","05", "Night"]:
        return "Night"
    else:
        return np.nan

def regeshark (x, pattern):
    """ funcion que devuelve el tipo de tiburon que ha atacado usando regex y el patron de busqueda

    Args:
        x (str): string que contiene el tipo de tiburon
        pattern (str): patron de busqueda

    Returns:
        np.nan: en caso en el que no se encuentre el patron devuelve un nan
        str: devuelve el tipo de tiburon
    """
    res = re.findall(pattern, x)
    res="".join(res)
    res=res.replace("]", "")
    if "shark" in res:
        return res
    else:
        return np.nan
    
def age (x, pattern):
    res = re.findall(pattern, x)
    if len(res)>=1:
        return int(res[0])
    else:
        return x

def monthattack (x, pattern):
    res = re.findall(pattern, x)
    if len(res)>1:
        if (len(res[-1])==3) and (res[-1] != "War"):
            return res[-1]
        else:
            return "NaN"
    elif len(res)==1:
        if (len(res[0])==3) and (res[-1] != "War"):
            return res[0]
        else:
            return "NaN"
    else:
        return "NaN"



def fatal (x, pattern):
    res = re.findall(pattern, x)
    res="".join(res)
    if len(res)>=1:
        return res
    else:
        return "NaN"




def sex (x, pattern):
    res = re.findall(pattern, x)
    if len(res)>=1:
        return str(res[0])
    else:
        return "NaN"
