alunos = {}

alunos['nome'] = input('nome: ')
alunos['media'] = float(input('média: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado(a)!'
else:
    alunos['situação'] = 'Reprovado(a)!'

print(f'O aluno(a) {alunos["nome"]}, obteve média {alunos["media"]} e esta {alunos["situação"]}')
