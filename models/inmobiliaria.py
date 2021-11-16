# -*- coding: utf-8 -*-

from odoo import models, fields


class Inmobiliaria(models.Model):
     _name = 'realty.inmobiliaria'
     _description = 'Inmobiliaria registrada en el sistema'

     nombre = fields.Char()
     direccion = fields.Text()
     suscripcion_ids = fields.One2many('realty.suscripcion','inmobiliaria_id', string='Suscripciones',)
