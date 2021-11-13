# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RealtyInmobiliaria(models.Model):
     _name = 'realty.inmobiliaria'
     _description = 'Inmobiliaria registrada en el sistema'

     nombre = fields.Char()
     direccion = fields.Text()
     plan_id = fields.Many2one('plan', 'Plan de Suscripcion', index=True, ondelete='cascade')
