Terminais				# A secao de simbolos terminais eh a primeira do arquivo.
[ runs ]				# Tudo o que estiver apos o sustenido (#) sera considerado comentario
[ barks ]				# Os simbolos terminais sao qualquer sequencia de caracteres (nao reservados) entre colchetes.
[ eats ]				# A secao de simbolos terminais inicia com a palavra-chave "Terminais"
[ dog ]					# Eh altamente recomendavel que simbolos terminais iniciem por caracteres minusculos
[ cat ]					# Simbolos nao podem conter os caracteres "[", "]", "#" ou ">", por serem caracteres reservados
[ meat ]				# Apesar disso, eles podem conter outros caracteres especiais e espacos tambem.
[ the ]					# Normalmente sera necessario apenas um caractere minusculo para definir um simbolo terminal.
[ a ]					# O uso dos espacos eh fundamental. Os colchetes devem ser separados do simbolo por espacos.
Variaveis				# A secao de variaveis inicia pela palavra reservada "Variaveis", e eh a segunda do arquivo
[ N ]					# Eh muito importante respeitar a ordem das secoes
[ V ]					# Note que a sintaxe eh case-sensitive, isto eh, maiusculas e minusculas sao diferenciadas
[ NP ]					# Simbolos variaveis sao qualquer conjunto de caracteres nao reservados entre colchetes.
[ DT ]					# Sugere-se evitar o uso de acentos para que o uso em outras plataformas nao corrompa o arquivo.
[ VP ]
[ S ]
Inicial					# O simbolo inicial possui uma secao propria, iniciada pela palavra "Inicial"
[ S ]					# Essa secao possui apenas uma linha com o simbolo inicial entre colchetes.
Regras					# A ultima secao vem encabecada pela palavra-chave "Regras"
[ S ] > [ NP ] [ VP ] ;1	# Nas regras de producao, coloca-se o simbolo da esquerda entre colchetes antes
[ NP ] > [ N ] ;0.7		# do simbolo de ">", que representa a derivacao.
[ N ] > [ dog ] ;0.3			# Os simbolos da direita devem estar cada um entre colchetes e separados por espacos,
[ N ] > [ cat ] ;0.3			# a fim de definir-se a fronteira entre dois simbolos.
[ N ] > [ meat ] ;0.4		# As regras de producao devem seguir as restricoes de uma GLC.
[ VP ] > [ V ] [ NP ] ;0.8	# Linhas em branco entre as secoes e entre os itens nao serao toleradas.
[ NP ] > [ DT ] [ N ] ;0.3
[ VP ] > [ V ] ;0.2
[ V ] > [ runs ] ;0.25
[ V ] > [ barks ] ;0.5
[ V ] > [ eats ] ;0.25
[ DT ] > [ a ] ;0.45
[ DT ] > [ the ] ;0.55

