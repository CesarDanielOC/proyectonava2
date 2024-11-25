from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.CharField(max_length=10, unique=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.TimeField()),
                ('motivo', models.CharField(max_length=255)),
            ],
        ),
    ]
