# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Contrato(models.Model):
    _name = 'realty.contrato'
    _description = 'Contratos de propiedades'

    propiedad = fields.Many2one('realty.propiedad', 'Propiedad')
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    dia_vencimiento = fields.Integer()
    incremento = fields.Float()
    incremento_meses = fields.Integer()
    valor_inicial = fields.Float()
    interes_diario = fields.Float()
    inquilinos = fields.One2many('realty.inquilino', 'contrato', string='Inquilinos', )
    garantes = fields.One2many('realty.garante', 'contrato', string='Garantes', )
    alquileres = fields.One2many('realty.alquiler', 'contrato', string='Alquileres', )

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.propiedad.direccion + "(" + record.fecha_inicio.strftime('%d/%m/%Y') + "-" + record.fecha_fin.strftime('%d/%m/%Y') + ")"))
        return result

    @api.model
    def create(self, vals):
        res = super(Contrato, self).create(vals)
        res.generar_alquileres()
        return res

    def generar_alquileres(self):
        meses = self.diff_month()
        valor_alquiler = self.valor_inicial
        for x in range(1, meses):
            fecha_alquiler = self.fecha_inicio + relativedelta(months=(x - 1))
            if x % self.incremento_meses == 0:
                valor_alquiler = self.valor_inicial * (1 + (self.incremento * (x / self.incremento_meses)) / 100)
            self.env['realty.alquiler'].create({
                'contrato': self.id,
                'valor': valor_alquiler,
                'fecha': fecha_alquiler,
                'fecha_vencimiento': fecha_alquiler + relativedelta(days=(self.dia_vencimiento - 1)),
            })

    def diff_month(self):
        return (self.fecha_fin.year - self.fecha_inicio.year) * 12 + self.fecha_fin.month - self.fecha_inicio.month
