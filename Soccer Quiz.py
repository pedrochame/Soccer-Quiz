import csv, random, re, os, sys
from colorama import Fore, Style
from deep_translator import GoogleTranslator
from datetime import date,datetime
from tabulate import tabulate
from babel.dates import format_date, Locale

#Função que limpa o terminal
def limpar_terminal():
    #Para Unix/Linux/MacOS
    if os.name == 'posix':
        os.system('clear')
    #Para Windows
    elif os.name == 'nt':
        os.system('cls')

#Função que recebe um texto e um idioma, e retorna o texto traduzido para o idioma especificado
def traduzir(texto,destino="pt"):
    return GoogleTranslator(source="pt", target=destino).translate(texto)

#Função que recebe o caminho para o arquivo com as questões do jogo e retorna uma lista embaralhada de dicionários, em que cada
#dicionário é uma questão, contendo as chaves da pergunta em si, resposta e 3 alternativas incorretas
def configurar_questoes(arquivo):
    lista = []
    with open(arquivo, encoding = 'utf-8') as file:
        for row in csv.DictReader(file):
            lista.append({"question": row["question"], "ans": row["ans"], "alt1": row["alt1"], "alt2": row["alt2"], "alt3": row["alt3"], "translate_alt": row["translate_alt"]})
    random.shuffle(lista)
    return lista

#Função que recebe o caminho para o arquivo com as informações de jogos que aconteceram e retorna uma lista de dicionários, em que cada
#dicionário é o registro de um jogo, contendo as chaves de nome do jogador, pontuação e data. A lista retorna os 10 primeiros jogos
#de forma ordenada por pontuação e data de maneira decrescente
def configurar_ranking(arquivo, idioma):
    lista = []
    with open(arquivo) as file:
        for row in csv.DictReader(file):
            lista.append({traduzir("Jogador",idioma): row["player"], traduzir("Pontuação",idioma): int(row["score"]), traduzir("Data",idioma): datetime.strptime(row["date"],"%d/%m/%Y")})

    lista = sorted(lista, key=lambda x: (x[traduzir("Pontuação",idioma)], x[traduzir("Data",idioma)]), reverse=True)[:10]

    #Colocando as datas dos registros no formato de acordo com o idioma
    for item in lista:
        item[traduzir("Data",idioma)] = format_date(item[traduzir("Data",idioma)], format='full', locale=Locale.parse(idioma))

    return lista

#Função que recebe um idioma e pede o nome do jogador no idioma especificado, a função se repete até que seja inserido um nome
#contendo somente letras e espaços
def get_name(idioma):
    while True:
        limpar_terminal()
        player = input(traduzir("Qual o seu nome?", idioma) + " ").strip().title()
        if (matches := re.fullmatch(r"([a-z]+ ?)+",player,re.IGNORECASE)):
            return player

#Função que recebe um idioma e pede a resposta do jogador no idioma especificado, a função se repete até que seja inserida uma resposta
#A/a, B/b, C/c ou D/d
def get_resp(idioma):
    while True:
        resp = input("\n" + traduzir("Resposta", idioma) + ": ").strip()
        if (matches := re.fullmatch(r"[a-d]",resp,re.IGNORECASE)):
            return resp

#Função que pede um idioma ao jogador, este podendo ser Inglês(EN/en), Espanhol(ES/es) ou Português(PT/pt).
#A função se repete até que seja inserido um dos idiomas possíveis
def get_idioma():
    while True:
        limpar_terminal()
        idioma = input(traduzir("Escolha o idioma","en") + "/" + traduzir("Escolha o idioma","es") + "/Escolha o idioma" + " [EN | ES | PT]: ").strip()
        if (matches := re.fullmatch(r"es|pt|en",idioma,re.IGNORECASE)):
            return idioma.lower()

#Classe Player, contém variáveis para armazenar a lista de questões a ser utilizada na jogada, a pontuação do jogador, o nome do jogador
#e o idioma escolhido por ele
class Player:
    def __init__(self, name, idioma, questions):
        self._name = name
        self._idioma = idioma
        self._score = 0
        self._questions = questions

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def add_score(self):
        self._score += 1

    @property
    def idioma(self):
        return self._idioma

    @idioma.setter
    def idioma(self, idioma):
        self._idioma = idioma

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, questions):
        self._questions = questions

#Função principal do programa
def main():

    #Definindo número de questões por jogo
    questoes_por_jogo = 10

    #Coletando resposta do jogador para idioma e nome
    player_idioma = get_idioma()
    player_name = get_name(player_idioma)

    #Menu
    while True:

        #Configurando lista embaralhada de questões
        player_questions = configurar_questoes("questions.csv")

        #Criação do objeto Player
        player = Player(player_name, player_idioma, player_questions)

        #Exibindo opções
        limpar_terminal()
        print(traduzir("Seja bem-vindo ao", player.idioma) + " Soccer Quiz" + f", {player.name.split(" ")[0]}.\n" )
        print(traduzir("Escolha uma opção:", player.idioma) + " \n")
        print("[1] " + traduzir("Jogar",player.idioma))
        print("[2] " + traduzir("Ver Classificação Geral",player.idioma))
        print("[3] " + traduzir("Sair",player.idioma) + "\n")

        #Coletando resposta do jogador para o Menu
        match input(traduzir("Resposta",player.idioma) + ": "):
            case "1":
                #Jogo Iniciado
                for n,question in enumerate(player.questions[len(player.questions)-questoes_por_jogo:], start=1):

                    #Imprimindo a questão
                    limpar_terminal()
                    print(f"{n} - {traduzir(question["question"], player.idioma)}\n")

                    #Embaralhando as opções de resposta
                    opcoes = [question["ans"], question["alt1"], question["alt2"], question["alt3"]]
                    random.shuffle(opcoes)

                    #Imprimindo as opções de resposta
                    for n,opcao in enumerate(opcoes, start=65):
                        #Se as opções necessitarem de tradução, são impressas traduzidas
                        if question["translate_alt"] == "1":
                            print(f"[{chr(n)}]",traduzir(opcao,player.idioma))
                        else:
                            print(f"[{chr(n)}]",opcao)
                        #Verificando se a opção é a resposta, se sim, armazenamos a letra correspondente da opção
                        if question["ans"] == opcao:
                            question_resp = chr(n)

                    #Coletando resposta do jogador
                    resp = get_resp(player.idioma)

                    #Verificando se o jogador acertou a resposta
                    if resp.lower() == question_resp.lower():
                        #Mensagem de acerto
                        print(f"\n{Fore.GREEN}{traduzir("Você acertou.", player.idioma)}{Style.RESET_ALL}")
                        #Incrementando a pontuação do jogador
                        player.add_score()
                    else:
                        #Mensagem de erro
                        print(f"\n{Fore.RED}{traduzir("Você errou.", player.idioma)}{Style.RESET_ALL}")

                    #Exibindo pontuação e esperando o usuário pressionar uma tecla para recomeçar o loop, avançando para a próxima pergunta
                    print(traduzir("Sua pontuação",player.idioma) + ": ", player.score)
                    input("\n"+traduzir("Tecle Enter para continuar...",player.idioma))

                #Exibindo mensagem de fim de jogo, com pontuação do jogador e feedback de desempenho
                limpar_terminal()
                print(f"{traduzir("Fim de jogo", player.idioma)}.")
                print(f"{traduzir("Sua pontuação", player.idioma)}: {player.score}")

                if 8 <= player.score <= 10:
                    desempenho = "Bom"
                    cor = Fore.GREEN
                elif 4 <= player.score <= 7:
                    desempenho = "Regular"
                    cor = Fore.YELLOW
                else:
                    desempenho = "Ruim"
                    cor = Fore.RED

                print(f"{traduzir("Seu desempenho", player.idioma)}: {cor}{traduzir(desempenho,player.idioma)}{Style.RESET_ALL}")

                print(f"{traduzir("Obrigado por jogar", player.idioma)}.")
                input("\n"+traduzir("Tecle Enter para continuar...",player.idioma))

                #Gravando no arquivo de ranking os dados do jogo do jogador
                with open("ranking.csv", "a") as file:
                    writer = csv.DictWriter(file, fieldnames=["player", "score", "date"])
                    writer.writerow({"player": player.name, "score": player.score, "date": date.today().strftime("%d/%m/%Y")})

            case "2":
                limpar_terminal()
                print(f"{traduzir('Classificação Geral',player.idioma)}:\n")
                print(tabulate(configurar_ranking("ranking.csv", player.idioma), headers="keys", tablefmt="grid"))
                input("\n"+traduzir("Tecle Enter para continuar...",player.idioma))

            case "3":
                sys.exit("\n" + traduzir("Obrigado por jogar.",player.idioma))


if __name__ == "__main__":
    main()
