def is_palindrome(palabra):
    palabra=palabra.lower().replace(" ","")
    
    palindromo = palabra[::-1]
    palabra_limpia = ""
    for char in palabra:
        if char.isalnum():
            palabra_limpia += char
    
    palindromo = palabra_limpia[::-1]
    