# -*- coding: utf-8 -*-

from odoo import models, fields


class Recibo(models.Model):
    _name = 'realty.recibo'
    _description = 'Recibo de un alquiler registrado en el sistema'

    alquiler = fields.Many2one('realty.alquiler', 'Alquiler')
    fecha = fields.Date()
    descuento = fields.Float()
    descuento_texto = fields.Text()
    intereses = fields.Float()
    intereses_texto = fields.Text()
    extras = fields.Float()
    extras_texto = fields.Text()
    valor = fields.Float()

