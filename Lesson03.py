'''LIST'''
# List are mutable
# Elements can be different types
# List and Tuples are iterable
L = [1, 2, 4]
print(dir(L))

# Alias
L_alias = L
#Cloning
L_clone = L[:]

#Problem 
#Write a function that takes in two Lists(L1, L2
# and removes repeated elements from L1 and L2
# returns a List of Unique elements from two lists

L1 = [1, 3, 5, 7]
L2 = [1, 3, 4, 6]

def list_dup(L1,L2):
    for i in L1:
        if i in L2:
            L1.remove(i)
    return L1+L2   

print(L1)            
L_mod = list_dup(L1,L2)
print(L1)

#Scope of Variables

a = 10

def print_some():
    b = 20
    print('a:', a)
    print('b:', b)
    def some():
        print('b: Some', b)
    some()


print_some()
#print('b:Outside FNC', b)


