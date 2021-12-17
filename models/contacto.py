# -*- coding: utf-8 -*-

from odoo import models, fields


class Contacto(models.Model):
    _name = 'realty.contacto'
    _description = 'Contacto de una inmobiliaria registrada en el sistema'

    inmobiliaria_id = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    nombre = fields.Char()
    direccion = fields.Text()
    dni = fields.Char()
    fecha_nacimiento = fields.Date()
    nombre_inmobiliaria = fields.Char(related='inmobiliaria_id.nombre', string='Inmobiliaria', )
