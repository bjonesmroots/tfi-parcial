# -*- coding: utf-8 -*-

from odoo import models, fields


class Recibo(models.Model):
    _name = 'realty.recibo'
    _description = 'Recibo de un alquiler registrado en el sistema'

    alquiler_id = fields.Many2one('realty.alquiler', 'Alquiler')
    fecha = fields.Date()
    valor = fields.Float()

