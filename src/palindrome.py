def is_palindrome(palabra):
    palabra=palabra.lower().replace(" ","")
    
    palindromo = palabra[::-1]
    palabra_limpia = ""
    for char in palabra:
        if char.isalnum():
            palabra_limpia += char
    
    palindromo = palabra_limpia[::-1]
    
    if palindromo==palabra_limpia:
        print(f"la palabra/frase {palabra} es un palindromo")
        return True
    else:
        print(f"la palabra/frase {palabra} es un no palindromo")
        return False

def main():
    palabra=input("ingrese una palabra")
    is_palindrome(palabra)
        

if __name__=="__main__":
    main()