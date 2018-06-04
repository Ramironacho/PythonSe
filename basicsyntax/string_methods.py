"""
Ejemplos de metodos de string
"""

# Accesing characters in a string
# index starts from zero
first = "nyc"[0]
city = "sfo"
print(first)
ft = city[0]
print(ft)
first = "nyc"[1]
print(first)

"""
len()
lower()
upper()
str()
"""

stri = "This Is a MIxed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

""""
Concatenation
"""
print ("Hello "+ "World"+"!!!")
print (first + " " + city)