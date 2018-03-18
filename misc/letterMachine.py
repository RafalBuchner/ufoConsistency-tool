# -*- coding: utf-8 -*-
from fontTools.agl import UV2AGL


ASCII = '''a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z @ [ \ ] ^ _ ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? { | } ~ '''
Hamburgefontsiv = '''H a m b u r g e f o n t s i v'''


ASCIInaming = list(set(ASCII.split(" ")) - set(['[', ']', '(', ')', '{', '}', '<', '>', '/', '%']))
def lettersToNames(txt):
    txt = txt.decode("utf-8")

    output = ""
    for char in txt:
        uni = ord(char)
        if UV2AGL.get(uni) == "space":
        	pass
        elif UV2AGL.get(uni) == "None":
        	print("None!!!",char)
        else:
    	    output += UV2AGL.get(uni) + " "
    return output
