# Generated by Django 2.1.4 on 2019-01-14 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id_curso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=95)),
                ('nivel', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='datos_cuenta',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=85)),
                ('password', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='datos_personales',
            fields=[
                ('id_datos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=85)),
                ('a_paterno', models.CharField(max_length=85)),
                ('a_materno', models.CharField(max_length=85)),
                ('edad', models.IntegerField()),
                ('datos_cuenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.datos_cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='distractores_pregunta',
            fields=[
                ('id_distractor', models.IntegerField(primary_key=True, serialize=False)),
                ('distractor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ejercicios',
            fields=[
                ('id_ejercicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_ejercicio', models.CharField(max_length=85)),
                ('puntaje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inteligencias',
            fields=[
                ('id_inteligencias', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_de_inteligencia', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='preguntas_test_inteligencia',
            fields=[
                ('id_pregunta_test', models.IntegerField(primary_key=True, serialize=False)),
                ('num_pregunta', models.IntegerField()),
                ('pregunta', models.TextField()),
                ('inteligencias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.inteligencias')),
            ],
        ),
        migrations.CreateModel(
            name='resultados',
            fields=[
                ('id_resultados', models.IntegerField(primary_key=True, serialize=False)),
                ('resultados_correctas', models.IntegerField()),
                ('resultados_incorrectas', models.IntegerField()),
                ('datos_cuenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.datos_cuenta')),
                ('ejercicios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.ejercicios')),
            ],
        ),
        migrations.CreateModel(
            name='resultados_ejercicios',
            fields=[
                ('id_resultado_ejercicio', models.IntegerField(primary_key=True, serialize=False)),
                ('acierto', models.BooleanField()),
                ('datos_cuenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.datos_cuenta')),
                ('ejercicios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.ejercicios')),
            ],
        ),
        migrations.CreateModel(
            name='resultados_test_inteligencia',
            fields=[
                ('valor', models.IntegerField(primary_key=True, serialize=False)),
                ('datos_cuenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.datos_cuenta')),
                ('preguntas_test_inteligencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.preguntas_test_inteligencia')),
            ],
        ),
        migrations.CreateModel(
            name='retroalimetacion_preguntas',
            fields=[
                ('id_retroalimetacion', models.IntegerField(primary_key=True, serialize=False)),
                ('ejercicios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.ejercicios')),
            ],
        ),
        migrations.CreateModel(
            name='temas_curso',
            fields=[
                ('id_temas', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_temas', models.CharField(max_length=45)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.curso')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_usuario',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tipo_usuario', models.CharField(max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='retroalimetacion_preguntas',
            name='temas_curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.temas_curso'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='temas_curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.temas_curso'),
        ),
        migrations.AddField(
            model_name='distractores_pregunta',
            name='id_ejercicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.ejercicios'),
        ),
        migrations.AddField(
            model_name='datos_personales',
            name='tipo_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.tipo_usuario'),
        ),
    ]
