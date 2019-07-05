#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:08:41 2019

@author: DaveTremblay
"""
def cyrillify():
    import datetime
    import sys
    
    today = datetime.datetime.now()
    
    filename = "faux-cyrillic_output_"+str(today)+".txt"
    f = open(filename, "w", encoding="utf-8")
    
    alphabet = {
            "A" : "Д",
            "a" : "д",
            "B" : "В",
            "b" : "ь",
            "C" : "С",
            "c" : "с",
            "D" : "D",
            "d" : "d",
            "E" : "З",
            "e" : "з",
            "F" : "F",
            "f" : "f",
            "G" : "G",
            "g" : "g",
            "H" : "Н",
            "h" : "н",
            "I" : "I",
            "i" : "i",
            "J" : "J",
            "j" : "j",
            "K" : "К",
            "k" : "к",
            "L" : "L",
            "l" : "l",
            "M" : "М",
            "m" : "м",
            "N" : "И",
            "n" : "и",
            "O" : "Ф",
            "o" : "ф",
            "P" : "Р",
            "p" : "р",
            "Q" : "Q",
            "q" : "q",
            "R" : "Я",
            "r" : "г",
            "S" : "S",
            "s" : "s",
            "T" : "Т",
            "t" : "т",
            "U" : "Ц",
            "u" : "ц",
            "V" : "V",
            "v" : "v",
            "W" : "Ш",
            "w" : "ш",
            "X" : "Ж",
            "x" : "ж",
            "Y" : "Ч",
            "y" : "ч",
            "Z" : "Z",
            "z" : "z"
            }
    
    text_to_convert = str(input("Write text to cyrillify: "))
    
    if text_to_convert == "q" or text_to_convert == "Q":
        raise sys.exit()
    
    for character in text_to_convert:
        try:
            f.write(alphabet[character])
        except:
            f.write(character)
            
    f.close()
    
if True:
    cyrillify()