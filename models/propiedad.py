# -*- coding: utf-8 -*-

from odoo import models, fields


class Propiedad(models.Model):
    _name = 'realty.propiedad'
    _description = 'Propiedad de una inmobiliaria registrada en el sistema'

    inmobiliaria = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    nombre = fields.Char()
    nombre_inmobiliaria = fields.Char(related='inmobiliaria.nombre', string='Inmobiliaria', )
    direccion = fields.Text()
    propietarios = fields.One2many('realty.propietario', 'propiedad', string='Propietarios', )
