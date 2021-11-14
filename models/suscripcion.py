# -*- coding: utf-8 -*-

from odoo import models, fields


class Suscripcion(models.Model):
     _name = 'realty.suscripcion'
     _description = 'Suscripciones al sistema'

     ml_id = fields.Text()
     plan_id = fields.Many2one('realty.plan', 'Plan de la suscripcion')
     inmobiliaria_id = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
