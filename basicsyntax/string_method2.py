a = "1abc2abc3abc4abc"
print(a.replace('abc','ABC'))
print(a.replace('abc','ABC', 1))

# Sub-Strings
# starting index is inclusive
# ending index is exclusive
sub = a[1]
sub1 = a[1:-6]
c = "NylonSuit"
sub2 = c[1:-4]
step = a[1:6:2]
print(sub)
print(sub1)
print(sub2)
print(step)

b = a
print (a is b)



string="How are you? How is your name?"
print("Original string value is: ")
print(string)
#Split the string variable with "space" as a delimiter to convert into a list
string2=string.split(" ")
print("This is a list stored in 'string2' variable derived from 'string' variable: ")
print(string2)
#Counter variable to store how many occurrences of the word "How" exists
counter=0
#indexval is the variable to collect the index number in the string2 list, where last cccurrence of "How" is
indexval=""
#loop to navigate through each content of the list contained in string2 variable to calculate how many occurrences of "How" exists in the list
for i in range(0,len(string2)):
    if string2[i]=="How":
        counter+=1
        indexval=i
print("Number of occurrences: ",counter)
#Replacing the last occurrence of "How" with "What" in the string2 list
string2[indexval]="What"
#joining each list content (words) separated by space in the original variable 'string'
string=" ".join(string2)
print(string)