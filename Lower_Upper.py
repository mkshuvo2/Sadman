
def main():
    print("Enter any letter:")
    inp = input()
    uni_code = ord(inp)
    # Determine Upper or lower case
    if ((uni_code >= 65) and (uni_code <= 95)):
        print("Entered letter is Upper Case")
        print("Coverted Lower case", end=' ')
        print('{:c}'.format(toLower(uni_code)))
        
    elif ((uni_code >= 97) and (uni_code <= 122)):
        print("Entered letter is Lower Case")
        print("Coverted upper case", end=' ')
        print('{:c}'.format(toUpper(uni_code)))
    else:
        print("Hey! Enter a letter")

def toUpper(a):
    ''' Coverts lower case letter to upper case'''
    return a - 32
def toLower(a):
    ''' Coverts lower case letter to upper case'''
    return a + 32

if __name__ == '__main__':main()
