import unicodedata
import re
def sanitizar(texto):
    texto = texto.lower()  #Convierte el texto a minúsculas
    texto = unicodedata.normalize("NFD", texto) #Quita tildes
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn') #Quita caracteres diacríticos
    texto = re.sub(r'[^a-z0-9\s]', '', texto) #Elimina carecteres especiales
    texto = re.sub(r'\s+', ' ', texto).strip() #Elimina espacios redundantes
    return texto