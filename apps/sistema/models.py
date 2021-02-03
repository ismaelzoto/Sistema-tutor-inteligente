from django.db import models
# Create your models here.


class curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=95)
    nivel = models.CharField(max_length=45)
    image = models.ImageField(upload_to='media/images/', default=None)

    def __str__(self):
        return '{}'.format(self.nombre_curso)


class temas_curso(models.Model):
    id_temas = models.IntegerField(primary_key=True)
    nombre_temas = models.CharField(max_length=45)
    curso = models.ForeignKey(curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_temas)


class ejercicios(models.Model):
    id_ejercicio = models.IntegerField(primary_key=True)
    nombre_ejercicio = models.CharField(max_length=85)
    puntaje = models.IntegerField()
    temas_curso = models.ForeignKey(temas_curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_ejercicio)


class distractores_pregunta(models.Model):
    id_distractor = models.IntegerField(primary_key=True)
    distractor = models.CharField(max_length=50)
    id_ejercicio = models.ForeignKey(ejercicios, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.distractor)


class inteligencias(models.Model):
    id_inteligencias = models.IntegerField(primary_key=True)
    tipo_de_inteligencia = models.CharField(max_length=65)

    def __str__(self):
        return '{}'.format(self.tipo_de_inteligencia)


class preguntas_test_inteligencia(models.Model):
    id_pregunta_test = models.IntegerField(primary_key=True)
    num_pregunta = models.IntegerField()
    pregunta = models.TextField()
    inteligencias = models.ForeignKey(inteligencias, null=True, blank=True, on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(self.pregunta)


class datos_cuenta(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=85)
    password = models.CharField(max_length=85)

    def __str__(self):
        return '{}'.format(self.usuario)


class resultados_test_inteligencia(models.Model):
    valor = models.IntegerField(primary_key=True)
    preguntas_test_inteligencia = models.ForeignKey(preguntas_test_inteligencia, null=True, blank=True, on_delete=models.CASCADE)
    datos_cuenta = models.ForeignKey(datos_cuenta, null=True, blank=True, on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(self.valor)


class tipo_usuario(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=75)

    def __str__(self):
        return '{}'.format(self.nombre_tipo_usuario)


class datos_personales(models.Model):
    id_datos = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=85)
    a_paterno = models.CharField(max_length=85)
    a_materno = models.CharField(max_length=85)
    edad = models.IntegerField()
    tipo_usuario = models.ForeignKey(tipo_usuario, null=True, blank=True, on_delete=models.CASCADE)
    datos_cuenta = models.ForeignKey(datos_cuenta, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.edad)


class resultados_ejercicios(models.Model):
    id_resultado_ejercicio = models.IntegerField(primary_key=True)
    acierto = models.BooleanField()
    ejercicios = models.ForeignKey(ejercicios, null=True, blank=True, on_delete=models.CASCADE)
    datos_cuenta = models.ForeignKey(datos_cuenta, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField

    def __str__(self):
        return '{}'.format(self.fecha)


class retroalimetacion_preguntas(models.Model):
    id_retroalimetacion = models.IntegerField(primary_key=True)
    ejercicios = models.ForeignKey(ejercicios, null=True, blank=True, on_delete=models.CASCADE)
    temas_curso = models.ForeignKey(temas_curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id_retroalimetacion)


class resultados(models.Model):
    id_resultados = models.IntegerField(primary_key=True)
    resultados_correctas = models.IntegerField()
    resultados_incorrectas = models.IntegerField()
    ejercicios = models.ForeignKey(ejercicios, null=True, blank=True, on_delete=models.CASCADE)
    datos_cuenta = models.ForeignKey(datos_cuenta, null=True, blank=True, on_delete=models.CASCADE)


class cuestionario(models.Model):
    id_cuestionario = models.IntegerField(primary_key=True)
    id_pregunta_test = models.ForeignKey(preguntas_test_inteligencia, null=True, blank=True, on_delete=models.CASCADE)
    resultado_pregunta_cuestionario = models.IntegerField()