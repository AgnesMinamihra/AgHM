def computador_escolhe_jogada (n, m):
	computadorJoga = 1
	while computadorJoga != m: 
		if ((n - computadorJoga) % (m + 1) == 0):
			return computadorJoga
		else:
			computadorJoga += 1
	return computadorJoga

def usuario_escolhe_jogada(n, m):
	jogadaValida = False
	while not jogadaValida:
		joga = int(input("Informe a jogada: "))
		if joga > m or joga < 1:
			print ("Jogada inválida! Tente novamente")
		else:
			jogadaValida = True 
	return joga

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Número máximo de peças por jogada: "))
	vezDoComputador = False
	if (n % (m + 1) == 0):
		print ("Você começa!")
	else: 
		print ("Computador começa")
		vezDoComputador = True
	while n > 0:
		if vezDoComputador:
			computadorJoga = computador_escolhe_jogada (n, m)
			n = n - computadorJoga
			if n == 0:
				print ("Fim de jogo! O computador ganhou!")
			else:
				print ("O computador tirou", computadorJoga, "peça(s).")
				print("Restam", n, "peça(s).")
			vezDoComputador = False
		else:
			if vezDoComputador == False:
				jogada = usuario_escolhe_jogada (n, m)
				n = n - jogada
				if n == 0:
					print ("Você venceu!")
				else:
					print("Você tirou", jogada, "peça(s).")
					print("Restam", n, "peça(s).")
				vezDoComputador = True

def campeonato():
	rodada = 1 
	pontos_usuario = 0
	pontos_computador = 0
	while rodada <= 3: 
		print ("**** Rodada", rodada)
		rodada += 1
		vencedor = partida()
		if vencedor == 1: 
			pontos_usuario += 1
		else: 
			pontos_computador += 1
	print("Final do campeonato!")
	print("Placar: Usuário", pontos_usuario, "x", pontos_computador, "Computador")

inicio = print ("Bem-vindo ao Jogo Nim! ")
opcao1 =print ("1 - Jogar partida")
opcao2 = print ("2 - Jogar campeonato")

Escolha = int(input("Digite o número de uma das opções: "))

if Escolha == 1:
	print("Você escolheu partida.") 
	partida()
else:
	if Escolha == 2:
		print("Você escolheu campeonato.") 
		campeonato()