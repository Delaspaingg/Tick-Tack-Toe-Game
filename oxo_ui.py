import oxo_logic

menu = ["Nueva partida",
		"Cargar partida", 
		"Ayuda",
		"Salir"]

def getMenuChoice(aMenu):
	if not aMenu:
		raise ValueError('Sin contenido del menu')

	while True:
		print("\n\n")
		for index, item in enumerate(aMenu, start=1):
			print(index, '\t', item)

		try:
			choice = int(input("\nEscoje una opcion del menu: "))
			if 1 <= choice <= len(aMenu):
				return choice
			else:
				print("Escoje un numero entre 1 y", len(aMenu))
		except ValueError:
			print("Escoje el numero de la funcion del menu")

def startGame():
	return oxo_logic.newGame()

def resumeGame():
	return oxo_logic.restoreGame()

def displayHelp():
	print('''
		Nueva partida: Empieza una nueva partida de tick tack toe
		Cargar partida: Sige donde lo dejaste la ultima vez
		Ayuda: Muestra esta paguina
		Salir: Sales del juego
		''')
def quit():
	print('Adios...')
	raise SystemExit

def executeChoice(choice):
	dispatch = [startGame, resumeGame, displayHelp, quit]
	game = dispatch[choice -1]()
	if game:
		playGame(startGame())

def printGame(game):
	display = '''
	1 | 2 | 3		{} | {} | {}
	---------		------------
	4 | 5 | 6		{} | {} | {}
	---------		------------
	7 | 8 | 9		{} | {} | {} '''
	print(display.format(*game))

def playGame(game):
	result = ""
	while not result:
		printGame(game)
		choice = input("Celda[1-9 o q para quitar]: ")
		if choice.lower()[0] == 'q':
			saves = input("Guardar partida antes de abandonar??[S/N] ")
			if save.lower()[0] == 'S':
				oxo_logic.saveGame(game)
			quit()
		else:
			try:
				cell = int(choice) -1
				if not (0 <= cell <=8):
					raise ValueError
			except ValueError:
				print("Escoje un numero entre 1 o 9 'q' para quitar ")
				continue

			try:
				result = oxo_logic.userMove(game,cell)
			except ValueError:
				print("Elige una celda vacia")
				continue

			if not result:
				result = oxo_logic.computerMove(game)
			if not result:
				continue
			elif result == 'D':
				printGame(game)
				print("Es un empate")
			else:
				printGame(game)
				print("El ganador es", result, '\n')


def main():
	while True:
		choice = getMenuChoice(menu)
		executeChoice(choice)

if __name__ == '__main__':
	main()

