import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "teclado", "internet", "javascript"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_digitadas = []
    tentativas = 6
    letras_corretas = []

    while tentativas > 0:
        palavra_secreta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_secreta += letra + " "
            else:
                palavra_secreta += "_ "

        print(f"Palavra: {palavra_secreta}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras digitadas: {letras_digitadas}")

        if palavra_secreta.replace(" ", "") == palavra:
            print("Parabéns! Você ganhou!")
            break

        letra_digitada = input("Digite uma letra: ").lower()

        if letra_digitada in letras_digitadas:
            print("Você já digitou essa letra. Tente outra.")
            continue

        letras_digitadas.append(letra_digitada)

        if letra_digitada in palavra:
            letras_corretas.append(letra_digitada)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta. Tente novamente.")

    if tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")

def main():
    print("Bem-vindo ao Jogo da Forca!")
    jogar_forca()
    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()