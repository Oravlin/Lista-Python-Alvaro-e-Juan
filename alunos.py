qtdAlunos = 0
alunosTotal = []
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
    media = 0.0
    for aluno in alunosTotal:
        print()
        for nota in aluno['nota']:
            totalNotas + totalNotas + nota
    media = totalNotas / len(alunosTotal)
    return media

# loop principal
while qtdAlunos < 40:


    try:
        nomeAluno = input("Digite seu nome: ")
        if nomeAluno == 'parar':
           break
        idadeAluno = int(input("Digite sua idade: "))
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
    print(f"media da sala:{mediaSala()}")

    

