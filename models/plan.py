# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RealtyPlan(models.Model):
     _name = 'realty.plan'
     _description = 'Plan de suscripción de las inmobiliarias'

     codigo = fields.Char()
     descripcion = fields.Text()
