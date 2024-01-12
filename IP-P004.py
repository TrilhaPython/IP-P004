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

from abc import ABC, abstractmethod
import numpy as np

class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, dtype):
        pass

    @abstractmethod
    def entradaDeDados(self, dado):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(np.float64)
        self.__lista = np.array([])

    def entradaDeDados(self, salario):
        self.__lista = np.append(self.__lista, salario)

    def mostraMediana(self):
        mediana = np.median(self.__lista)
        print("Mediana:", mediana)

    def mostraMenor(self):
        menor = np.min(self.__lista)
        print("Menor:", menor)

    def mostraMaior(self):
        maior = np.max(self.__lista)
        print("Maior:", maior)

    def listarEmOrdem(self):
        print("Lista de Salários em Ordem:")
        for salario in np.sort(self.__lista):
            print(salario)

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return str(self.__lista)
