# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date

class autoescuela_autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'Permite definir las características de una autoescuela'

    name = fields.Char(string="Nombre", required=True)
    domicilio = fields.Char(string="Domicilio")
    localidad = fields.Char(string="Localidad")
    provincia = fields.Char(string="Provincia")
    contacto = fields.Char(string="Teléfono de contacto")

    # Relaciones
    examen_ids = fields.Many2many('autoescuela.examen', string="Exámenes")
    profesor_ids = fields.One2many('autoescuela.profesor', 'autoescuela_id', string="Profesores")
    alumno_ids = fields.One2many('autoescuela.alumno', 'autoescuela_id', string="Alumnos")


class autoescuela_profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Permite definir las características de un profesor de autoescuela'

    name = fields.Char(string="Nombre y Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    coche = fields.Char(string="Coche")
    matricula = fields.Char(string="Matrícula")
    incorporacion = fields.Date(string="Fecha de incorporación")
    
    # Campo computado
    antiguedad = fields.Integer(string="Antigüedad", compute="_get_antiguedad")

    # Relaciones
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string="Autoescuela")
    alumno_ids = fields.One2many('autoescuela.alumno', 'profesor_id', string="Alumnos del profesor")

    # Restricciones SQL
    _sql_constraints = [
        ('dni_unique', 'unique(dni)', 'Error: Ya existe un profesor con este DNI.')
    ]

    @api.depends('incorporacion')
    def _get_antiguedad(self):
        for profesor in self:
            if profesor.incorporacion:
                profesor.antiguedad = relativedelta(date.today(), profesor.incorporacion).years
            else:
                profesor.antiguedad = 0


class autoescuela_alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Permite definir las características de un alumno'

    name = fields.Char(string="Nombre y Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    domicilio = fields.Char(string="Domicilio")
    matricula = fields.Char(string="Número de matrícula", required=True)

    # Relaciones
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string="Autoescuela")
    profesor_id = fields.Many2one('autoescuela.profesor', string="Profesor")
    examen_ids = fields.One2many('autoescuela.examen', 'alumno_id', string="Exámenes")

    # Restricciones SQL
    _sql_constraints = [
        ('matricula_unique', 'unique(matricula)', 'Error: El número de matrícula ya existe.')
    ]


class autoescuela_examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Permite definir las características de un examen'

    # Campo autogenerado con secuencia
    name = fields.Char(string="Código del Examen", default=lambda self: ('Autogenerado'), 
                       copy=False, readonly=True, tracking=True)
    
    fecha = fields.Date(string="Fecha del Examen")
    moneda_id = fields.Many2one('res.currency', string="Moneda")
    precio = fields.Monetary(string="Precio del Examen", currency_field='moneda_id')
    clases = fields.Integer(string="Número de clases")
    carnet = fields.Char(string="Tipo de Carnet", required=True, 
                         help="AM = Ciclomotores, A1 = Moto 11kW, A2 = Moto 35kW, A = Motos, B = Automóviles")
    aprobado = fields.Boolean(string="Aprobado")

    # Relaciones
    autoescuela_ids = fields.Many2many('autoescuela.autoescuela', string="Autoescuelas Asociadas")
    alumno_id = fields.Many2one('autoescuela.alumno', string="Alumno", required=True)

    # Funcionalidad para generar la secuencia del código de examen
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', ('Autogenerado')) == ('Autogenerado'):
                vals['name'] = self.env['ir.sequence'].next_by_code('autoescuela.examen')
        return super().create(vals_list)
    
    def _compute_display_name(self):
        for examen in self:
            examen.display_name = f"Código Examen: {examen.name} - Carnet: {examen.carnet}"