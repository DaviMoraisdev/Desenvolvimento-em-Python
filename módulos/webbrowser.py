import webbrowser

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Aprender python")
    print("2. Aprender sobre módulos")
    print("3. Aprender, Python, Fullstack JS, Inglês e No Code")
    print("4. Sair")

    choice = input(">")

    if choice == "1":
        webbrowser.open_new_tab('http://www.python.org/')
    elif choice == "2":
        webbrowser.open_new_tab('https://docs.python.org/3/py-modindex.html/')
    elif choice == "3":
        webbrowser.open_new_tab('https://pages.onebitcode.com/')
    elif choice == "4":
        done = True 
    else:
        print("Opção Inválida")