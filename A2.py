import string
password= input("Введите ваш пароль:")
x=0
if len (password)<8: #Проверка длинны пароля 
    print("Пароль должен быть больше 8  символов")
    x+=1
if password.lower() == password:
    print("В пароле нет заглавных букв")
    x+=1
if password.upper()==password:
    print("В пароле нет строчных букв")
    x+=1
if not any (symbol.isdigit() for symbol in password):
    print("В пароле нет цифр")
    x+=1
allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    print("В пароле нет специальных символов") #для всех доступных символов
    x+=1
speshsym='*_#'
if not any (symbol in speshsym for symbol in password):
    print("В пароле нет специальных символов")
    x+=1
if x==0:
    print ("Пароль надёжен")



