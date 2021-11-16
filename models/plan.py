# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Plan(models.Model):
     _name = 'realty.plan'
     _description = 'Plan de suscripción de las inmobiliarias'

     codigo = fields.Char()
     nombre = fields.Char()
     descripcion = fields.Text()
     precio = fields.Float()

