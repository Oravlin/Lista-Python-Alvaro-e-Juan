qtdAlunos = 0
alunosTotal = []
reprovados = 0
aprovados = 0
recuperacao = 0
notaMaior = 0
notaMenor = 10
alunoMaior = ''
alunoMenor = ''

def classificarAluno(nota):
    resultado = ''
    if nota >= 7:
        resultado = "Aprovado"
    elif nota >= 5 and nota < 7:
        resultado = "Recuperação"
    elif nota < 5:
        resultado = "Reprovado"
    return resultado

def mediaSala():
    totalNotas = 0
    media = 0
    for aluno in alunosTotal:
        nota = (aluno['nota'])
        totalNotas = totalNotas + int(nota)
    media = totalNotas / len(alunosTotal)
    return media

# loop para entrada de dados
while qtdAlunos < 40:
    try:
        nomeAluno = input("Digite seu nome (digite 0 para cancelar): ")
        if nomeAluno == '0':
           break
        idadeAluno = int(input("Digite sua idade: "))
        while(idadeAluno <= 0):
            print("Valor inválido! Digite um número maior que 0")
            idadeAluno = int(input("Digite sua idade: "))
        notaAluno = int(input("Digite sua nota: "))
        while(notaAluno < 0 or notaAluno > 10):
            print("Valor inválido! Digite uma nota entre 0 e 10")
            notaAluno = int(input("Digite sua nota: "))
    except ValueError:
        print("Digite uma idade válida!")
    except ValueError:
        print("Digite uma nota válida!")
    except TypeError:
        print("Digite valores númericos!")
        
    if(notaAluno > notaMaior):
        alunoMaior = nomeAluno
        notaMaior = notaAluno
    elif(notaAluno < notaMenor):
        alunoMenor = nomeAluno
        notaMenor = notaAluno
    if (notaAluno == notaMaior and not nomeAluno == alunoMaior):
        alunoMaior = f"{alunoMaior}, {nomeAluno}"
    elif(notaAluno == notaMenor and not nomeAluno == alunoMenor):
        alunoMenor = f"{alunoMenor}, {nomeAluno}"
        
    qtdAlunos += 1
    aluno = {"nome": nomeAluno,
            "idade": idadeAluno,
            "nota": notaAluno,
            "classificacao": classificarAluno(notaAluno)
    }
    alunosTotal.append(aluno)

#loop para mostrar os alunos
print(f"Quantidade de alunos: {len(alunosTotal)}")
for pessoa in alunosTotal:
    situacaoEstudante = pessoa['classificacao']
    if (situacaoEstudante == 'Aprovado'):
        aprovados += 1
    elif (situacaoEstudante == 'Reprovado'):
        reprovados += 1
    else:
        recuperacao += 1
    print(f"Nome: {pessoa["nome"]}\nSituação: {situacaoEstudante}\n")

print(f"Aprovados: {aprovados}\nReprovados: {reprovados}\nEm recuperação: {recuperacao}")
print(f"media da sala:{mediaSala():.2f}")
print(f"Aluno(s) com maior(es) nota(s): {alunoMaior}\nSua(s) nota(s): {notaMaior}\nAluno(s) com menor(es) nota(s): {alunoMenor}\nSua(s) nota(s): {notaMenor}")