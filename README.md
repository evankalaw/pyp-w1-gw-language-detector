# [pyp-w1] Language Detector

This is a program that is able to detect the language of certain piece of text given by the user. Provided with the program is compatibility for Spanish, German, and English. This is what the interface looks like:

```python
>>> from .languages import LANGUAGES

>>> user_text = """
Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987), conocido como
Leo Messi, es un futbolista argentino11 que juega como delantero en el Fútbol
Club Barcelona y en la selección argentina, de la que es capitán. Considerado
con frecuencia el mejor jugador del mundo y calificado en el ámbito deportivo
como el más grande de todos los tiempos, Messi es el único futbolista en la
historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de ellos en
forma consecutiva– y el primero en recibir tres Botas de Oro.
Con el Barcelona ha ganado siete títulos de La Liga y cuatro de la Liga de
Campeones de la UEFA, así como tres títulos de la Copa del Rey. Goleador
prolífico, ostenta los récords por más goles en la historia de La Liga (308),
en una temporada de La Liga (50), en un año calendario (91), en un partido de
la Liga de Campeones (cinco) y en más temporadas de la Liga de Campeones (cinco).
"""

>>> detect_language(user_text, LANGUAGES)
'Spanish'
```

The most common words in every language are counted in order to find the return value, which is the determined language. If given text contains words of different languages, the detector returns the language that contain most words in given text.

- Split function used in order to make user's input into a working list. 
- List then compared to the various lists in the dictionary of languages. The current language name and list of words are      accessed with every iteration
- A for loop checks for any intersections between the two lists, language by language.
- Checks for the highest amount of words - max is set initially to the count of the the first language. 
- When a new max is found, the global variable that holds the new highest language is modified.
- The language with the highest count of words is returned.
