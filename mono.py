# Versao 1.0

#Autor Mono

import json
import os
import sys


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"


with open("perguntas.json", "r", encoding="utf-8") as arquivo:

	questions = json.load(arquivo)

question_key = 0

Acertou = 0

Errou = 0

def logo_quiz():
	print(f"{BLUE}         .d88b.  db    db d888888b d88888D ")
	print("	.8P  Y8. 88    88   `88'   YP  d8' ")
	print("	88    88 88    88    88       d8'  ")
	print("	88    88 88    88    88      d8'   ")
	print("	`8P  d8' 88b  d88   .88.    d8' db ")
	print(f"	 `Y88'Y8 ~Y8888P' Y888888P d88888D {RESET}")
	print("           By: Mono    Versão 1.0\n")


def quiz_act():

	os.system("clear")

	logo_quiz()

	global question_key
	global Acertou
	global Errou

	print(f"{RESET}✓:Acertou", Acertou, " ✗:Errou", Errou,"\n")

	print(f"{YELLOW}",questions["perguntas"][question_key]["Pergunta"],"\n")

	print("[a].", questions["perguntas"][question_key]["Opcoes"][0])
	print("[b].", questions["perguntas"][question_key]["Opcoes"][1])
	print("[c].", questions["perguntas"][question_key]["Opcoes"][2])
	print("[d].", questions["perguntas"][question_key]["Opcoes"][3])
	print("\n[x]. Sair")


	resposta = input("\nQual sua resposta?:").lower()

	if resposta in ["a", "b", "c", "d"]:
		if resposta == questions["perguntas"][question_key]["Resposta"]:
			print(f"{GREEN}Resposta correta! ^^{YELLOW}\n")

			input("Continuar(Enter)")

			question_key += 1

			Acertou += 1

			os.system("clear")

			quiz_act()

		else:
			print(f"{RED}Resposta errada :({YELLOW}\n")

			input("Continuar(Enter)")

			Errou += 1

			quiz_act()

	elif resposta == "x":
		os.system("clear")
		sys.exit()

	else:
		print("Resposta invalída")

		quiz_act()
quiz_act()
