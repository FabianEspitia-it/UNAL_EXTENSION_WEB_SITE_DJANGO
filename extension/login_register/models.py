# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from typing import Any
from django.db import models
from django.contrib.auth import authenticate


class CursarEstudianteCursos(models.Model):
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    id_cursos_diplomados = models.ForeignKey('CursosDiplomados', db_column='id_cursos_diplomados', on_delete=models.CASCADE, blank=True, null=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursar_estudiante_cursos'


class CursarEstudianteServicio(models.Model):
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    id_servicio_extension = models.ForeignKey('ServicioExtension', models.DO_NOTHING, db_column='id_servicio_extension', blank=True, null=True)
    id_facultad = models.ForeignKey('Facultad', models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursar_estudiante_servicio'


class CursosDiplomados(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    duracion = models.CharField(max_length=60, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)
    id_modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='id_modalidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos_diplomados'

    def __str__(self):
        try:
            return f"{self.nombre} // {self.fecha} // {self.id_modalidad} // {self.id_profesor.nombre} // ID: {self.id}"
        except:
            return f"{self.nombre} // {self.fecha} // {self.id_modalidad} // {None} // ID: {self.id}"



class Decano(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decano'

    def __str__(self):
        return f"{self.nombre} // {self.correo} // ID: {self.id}"


class Direccion(models.Model):
    carrera = models.CharField(max_length=60, blank=True, null=True)
    calle = models.CharField(max_length=60, blank=True, null=True)
    codigo_postal = models.IntegerField(blank=True, null=True)
    id_sede = models.OneToOneField('Sede', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Entidad(models.Model):
    tipo = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad'


class EquipoTrabajo(models.Model):
    cargo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo_trabajo'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    rol = models.CharField(max_length=60, blank=True, null=True)
    estado_practica = models.IntegerField(blank=True, null=True)
    id_practica = models.ForeignKey('PracticasPasantia', models.DO_NOTHING, db_column='id_practica', blank=True, null=True)
    contraseña = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


    def __str__(self):
        return f"{self.nombre} /// {self.correo} /// {self.rol} /// ID: {self.id}"


class Facultad(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    id_decano = models.ForeignKey(Decano, models.DO_NOTHING, db_column='id_decano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultad'
    
    def __str__(self):
        return f"{self.nombre}"


class IntegranteEquipoTrabajo(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    cargo = models.CharField(max_length=60, blank=True, null=True)
    id_equipo = models.ForeignKey(EquipoTrabajo, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integrante_equipo_trabajo'


class Modalidad(models.Model):
    tipo_modalidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'
    def __str__(self):
        return f"{self.tipo_modalidad}"


class PertenecerSedeFacultad(models.Model):
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pertenecer_sede_facultad'


class PracticasPasantia(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_empresa = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='tipo_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'practicas_pasantia'


class Profesor(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'
    def __str__(self):
        return f"{self.nombre} /// {self.correo} /// {self.id_facultad} /// ID: {self.id}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    id_equipo_trabajo = models.ForeignKey(EquipoTrabajo, models.DO_NOTHING, db_column='id_equipo_trabajo', blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'
        
    def __str__(self):
        return f"{self.nombre} // {self.fecha} // {self.id_sede}"


class Sede(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    id_equipo_trabajo = models.ForeignKey(EquipoTrabajo, models.DO_NOTHING, db_column='id_equipo_trabajo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sede'
    def __str__(self):
        return f"{self.nombre}"


class ServicioCiudadania(models.Model):
    correo = models.CharField(max_length=60, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    id_servicio_extension = models.ForeignKey('ServicioExtension', models.DO_NOTHING, db_column='id_servicio_extension', blank=True, null=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_ciudadania'


class ServicioDetalleCiudadania(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_servicio_ciudadania = models.ForeignKey(ServicioCiudadania, models.DO_NOTHING, db_column='id_servicio_ciudadania', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_detalle_ciudadania'


class ServicioDetalleEmpresa(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_servicio_empresa = models.ForeignKey('ServicioEmpresa', models.DO_NOTHING, db_column='id_servicio_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_detalle_empresa'


class ServicioDetalleEstado(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_servicio_estado = models.ForeignKey('ServicioEstado', models.DO_NOTHING, db_column='id_servicio_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_detalle_estado'

    def __str__(self):
        return f"{self.nombre}"


class ServicioEmpresa(models.Model):
    correo = models.CharField(max_length=60, blank=True, null=True)
    telefono = models.CharField(max_length=60, blank=True, null=True)
    id_servicio_extension = models.ForeignKey('ServicioExtension', models.DO_NOTHING, db_column='id_servicio_extension', blank=True, null=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_empresa'


class ServicioEstado(models.Model):
    correo = models.CharField(max_length=60, blank=True, null=True)
    telefono = models.CharField(max_length=60, blank=True, null=True)
    id_servicio_extension = models.ForeignKey('ServicioExtension', models.DO_NOTHING, db_column='id_servicio_extension', blank=True, null=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_estado'


class ServicioExtension(models.Model):
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_extension'


class TenerProfesorEstudiante(models.Model):
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, blank=True, null=True)
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tener_profesor_estudiante'
