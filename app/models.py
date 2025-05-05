from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação")

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    periodo = models.IntegerField()

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
