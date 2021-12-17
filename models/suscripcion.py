# -*- coding: utf-8 -*-

from odoo import models, fields


class Suscripcion(models.Model):
    _name = 'realty.suscripcion'
    _description = 'Suscripciones al sistema'

    plan_id = fields.Many2one('realty.plan', 'Plan de la suscripcion')
    codigo_plan = fields.Char(related='plan_id.codigo')
    inmobiliaria_id = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    nombre_inmobiliaria = fields.Char(related='inmobiliaria_id.nombre')
    fecha_ultimo_cobro = fields.Datetime()
    id_mercadopago = fields.Char()
