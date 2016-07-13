"""This is the entry point of the program."""
# -*- coding: utf-8 -*-
from languages import LANGUAGES



def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    textList = text.split()
    returnName = ''
    highestCount = 0
    
    for lang in languages:
        langName = lang['name']
        langWords = lang['common_words']
        
        count = 0  
        for i in textList:
            if i in langWords:
                count += 1
                
        if count > highestCount:
            highestCount = count
            returnName = langName
    # 
    return returnName
    

       

#text = """Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
#               conocido como Leo Messi, es un futbolista argentino11 que juega
#                como delantero en el Fútbol Club Barcelona y en la selección
#                argentina, de la que es capitán. Considerado con frecuencia el
#                mejor jugador del mundo y calificado en el ámbito deportivo como el
#                más grande de todos los tiempos, Messi es el único futbolista en la
#                historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
#                ellos en forma consecutiva– y el primero en
#                recibir tres Botas de Oro."""
                
#print(detect_language(text, languages=LANGUAGES))