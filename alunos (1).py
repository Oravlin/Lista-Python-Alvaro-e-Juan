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
    nomeEstudante = pessoa['nome']
    situacaoEstudante = pessoa['classificacao']
    if(pessoa['nota'] > notaMaior):
        alunoMaior = pessoa['nome']
        notaMaior = pessoa['nota']
    elif(pessoa['nota'] < notaMenor):
        alunoMenor = pessoa['nome']
        notaMenor = pessoa['nota']
    elif (pessoa['nota'] == notaMaior):
        alunoMaior = f"{alunoMaior}, {pessoa['nome']}"
    elif(pessoa['nota'] == notaMenor):
        alunoMenor = f"{alunoMenor}, {pessoa['nome']}"

    if (situacaoEstudante == 'Aprovado'):
        aprovados += 1
    elif (situacaoEstudante == 'Reprovado'):
        reprovados += 1
    else:
        recuperacao += 1
    print(f"Nome: {nomeEstudante}\nSituação: {situacaoEstudante}\n")


print(f"Aprovados: {aprovados}\nReprovados: {reprovados}\nEm recuperação: {recuperacao}")
print(f"media da sala:{mediaSala():.2f}")
print(f"Aluno(s) com maior nota: {alunoMaior}\nSua(s) nota(s): {notaMaior}\nAluno(s) com menor notas: {alunoMenor}\nSua(s) nota(s): {notaMenor}")
