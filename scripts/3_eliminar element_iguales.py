
def array_diff(a, b):
    nueva_lista=[]
    for elemento in a[:]: #hacemos una copia de la lista para evitar problemas al eliminar elementos mientras iteramos
        if elemento in b:
            a.remove(elemento)
    nueva_lista=a
            
    return nueva_lista
print (array_diff([1,2,3], [1, 2]))

#Implement a function that computes the difference
#  between two lists. The function should remove all 
# occurrences of elements from the first list (a)
#  that are present in the second list (b). 
# The order of elements in the first list should 
# be preserved in the result.
#  If a = [1, 2, 2, 2, 3] and b = [2], 
# the result should be [1, 3].