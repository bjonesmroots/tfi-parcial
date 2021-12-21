# -*- coding: utf-8 -*-

from odoo import models, fields


class Contacto(models.Model):
    _name = 'realty.contacto'
    _description = 'Contacto de una inmobiliaria registrada en el sistema'

    inmobiliaria = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    nombre = fields.Char()
    direccion = fields.Text()
    dni = fields.Char()
    email = fields.Char()
    telefono = fields.Char()
    fecha_nacimiento = fields.Date()

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nombre))
        return result
