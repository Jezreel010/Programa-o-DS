class Alunos:
    def __init__ (self, nome, matricula, idade, sexo,):
        self.nome = nome
        self.matricula = matricula
        self.idade  = idade
        self.sexo = sexo

if __name__ == "__main__":
    aluno1 = Alunos ("pedro", "157244", "17", "Masculino")
    aluno2 = Alunos ("Bianca", "250787", "17", "Feminina")
    print("nome:", aluno1.nome, "Matricula:", aluno1.matricula, "Idade:", aluno1.idade, "Sexo:", aluno1.sexo)
    print("nome:", aluno2.nome, "Matricula:", aluno2.matricula, "Idade:", aluno2.idade, "Sexo:", aluno2.sexo)
    
    