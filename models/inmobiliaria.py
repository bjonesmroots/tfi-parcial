# -*- coding: utf-8 -*-

from odoo import models, fields


class Inmobiliaria(models.Model):
    _name = 'realty.inmobiliaria'
    _description = 'Inmobiliaria registrada en el sistema'

    nombre = fields.Char()
    direccion = fields.Text()
    telefono = fields.Text()
    suscripciones = fields.One2many('realty.suscripcion', 'inmobiliaria', string='Suscripciones', )
    propiedades = fields.One2many('realty.propiedad', 'inmobiliaria', string='Propiedades', )

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nombre))
        return result
