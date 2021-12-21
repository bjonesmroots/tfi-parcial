# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Plan(models.Model):
    _name = 'realty.plan'
    _description = 'Plan de suscripción de las inmobiliarias'

    codigo = fields.Char()
    nombre = fields.Char()
    descripcion = fields.Text()
    precio = fields.Float()

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nombre))
        return result
