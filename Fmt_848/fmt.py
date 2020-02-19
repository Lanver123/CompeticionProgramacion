import sys

"""
    - Lineas lo mas cercanas a 72 caracteres sin pasarse
    - Las lineas se cortan en los espacios
    - Los espacios en blanco al final de la linea anterior y al principio
        de la nueva linea se borran
    - Un \n se puede borrar a menos que:
        - Esta al final de una linea con solo espacios o sin caracteres
        - Le sigue un espacio o otro \n
    - Las palabras de > 72 caracteres deben aparecer en una linea por si mismas    
"""
if __name__ == "__main__":
    data = "".join([line for line in sys.stdin.readlines()])
    print(data.split(" "))
