import readchar
print(f"!!estas dentro de el juego, preciona la tecla '↑' para salir!!")


while True:
    key = readchar.readkey()    

    if key == readchar.key.UP:
        print("Tecla '↑' presionada. saliendo del juego")
        break
    else:
        print(f"tecla '{key}' precionada.") 