class NotasTurma:
    def __init__(self, nAlunos=30, nCreditos=3):
        self._nAlunos = nAlunos
        self._nCreditos = nCreditos
        self._notas = [[0] * nCreditos for _ in range(nAlunos)]

    def leNotas(self):
        for i in range(self._nAlunos):
            for j in range(self._nCreditos):
                nota = float(input(f"Informe a nota do aluno {i + 1} na avaliação {j + 1}: "))
                self._notas[i][j] = nota

    def mediaTurma(self):
        total = sum(sum(avaliacao) for avaliacao in self._notas)
        return total / (self._nAlunos * self._nCreditos)

    def mediaAluno(self, index=0):
        return sum(self._notas[index]) / self._nCreditos

    def mediaAvaliacao(self, index=0):
        return sum(avaliacao[index] for avaliacao in self._notas) / self._nAlunos

    def quantAprovados(self):
        return sum(1 for media_aluno in map(lambda i: self.mediaAluno(i), range(self._nAlunos)) if media_aluno >= 6)

    def quantReprovados(self):
        return sum(1 for media_aluno in map(lambda i: self.mediaAluno(i), range(self._nAlunos)) if media_aluno < 6)

    def menorNota(self):
        notas_flat = [nota for avaliacao in self._notas for nota in avaliacao]
        return min(notas_flat)

    def maiorNota(self):
        notas_flat = [nota for avaliacao in self._notas for nota in avaliacao]
        return max(notas_flat)

    def __str__(self):
        return f"Notas da turma:\n{self._notas}"


turma = NotasTurma()
turma.leNotas()
print("Média da turma:", turma.mediaTurma())
print("Média do Aluno:", turma.mediaAluno())
print("Média da avaliação:", turma.mediaAvaliacao())
print("Quantidade de alunos aprovados:", turma.quantAprovados())
print("Quantidade de alunos reprovados:", turma.quantReprovados())
print("Menor nota da turma:", turma.menorNota())
print("Maior nota da turma: ", turma.maiorNota())
print(turma)