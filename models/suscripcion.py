# -*- coding: utf-8 -*-

from odoo import models, fields


class Suscripcion(models.Model):
    _name = 'realty.suscripcion'
    _description = 'Suscripciones al sistema'

    plan = fields.Many2one('realty.plan', 'Plan de la suscripcion')
    codigo_plan = fields.Char(related='plan.codigo')
    inmobiliaria = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    fecha_ultimo_cobro = fields.Datetime()
    id_mercadopago = fields.Char()
