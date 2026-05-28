qtdAlunos = 0
alunosTotal = []
reprovados = 0
aprovados = 0
recuperacao = 0
notaMaior = 0
notaMenor = 10
alunoMaior = ""
alunoMenor = ""
continuar = "s"

def classificarAluno(nota):
    resultado = ""
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
        nota = aluno["nota"]
        totalNotas = totalNotas + int(nota)
    media = totalNotas / len(alunosTotal)
    return media

# entrada de dados
while continuar == "s":
    nomeAluno = input("\nDigite seu nome: ")
    while True:
        try:
            idadeAluno = int(input("\nDigite sua idade: "))
            if idadeAluno <= 0:
                print("Valor inválido! Digite um número maior que zero!")
                continue
            break
        except ValueError:
            print("Erro! Digite valores inteiros para a idade")
    while True:
        try:
            notaAluno = float(input("\nDigite a nota do aluno: "))
            if notaAluno < 0 or notaAluno > 10:
                print("Valor inválido! Digite um valor entre 0 e 10!")
                continue
            break
        except ValueError:
            print("Erro! Digite um número inteiro ou decimal!")
    if notaAluno > notaMaior:
        alunoMaior = nomeAluno
        notaMaior = notaAluno
    elif notaAluno < notaMenor:
        alunoMenor = nomeAluno
        notaMenor = notaAluno
    if notaAluno == notaMaior and not nomeAluno == alunoMaior:
        alunoMaior = f"{alunoMaior}, {nomeAluno}"
    elif notaAluno == notaMenor and not nomeAluno == alunoMenor:
        alunoMenor = f"{alunoMenor}, {nomeAluno}"

    qtdAlunos += 1
    aluno = {
                "nome": nomeAluno,
                "idade": idadeAluno,
                "nota": notaAluno,
                "classificacao": classificarAluno(notaAluno),
            }
    alunosTotal.append(aluno)
    while True:
            continuar = input("\nDeseja continuar? (s/n): ").lower()
            if continuar == "s" or continuar == "n":
                break
            else:
                print("Digite 's' ou 'n' apenas! \n") 
                continue
# loop para mostrar os alunos
print(f"Quantidade de alunos: {len(alunosTotal)}")
for pessoa in alunosTotal:
    situacaoEstudante = pessoa["classificacao"]
    if situacaoEstudante == "Aprovado":
        aprovados += 1
    elif situacaoEstudante == "Reprovado":
        reprovados += 1
    else:
        recuperacao += 1
    print(f"Nome: {pessoa["nome"]}\nSituação: {situacaoEstudante}\n")

print(
    f"Aprovados: {aprovados}\nReprovados: {reprovados}\nEm recuperação: {recuperacao}"
)
print(f"media da sala:{mediaSala():.2f}")
print(
    f"Aluno(s) com maior(es) nota(s): {alunoMaior}\nSua(s) nota(s): {notaMaior}\nAluno(s) com menor(es) nota(s): {alunoMenor}\nSua(s) nota(s): {notaMenor}"
)
