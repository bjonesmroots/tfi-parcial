# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import date


class Alquiler(models.Model):
    _name = 'realty.alquiler'
    _description = 'Alquiler de un contrato registrado en el sistema'

    contrato = fields.Many2one('realty.contrato', 'Contrato')
    fecha = fields.Date()
    fecha_vencimiento = fields.Date()
    valor = fields.Float()
    recibos = fields.One2many('realty.recibo', 'alquiler', string='Recibos', )
    total_pagado = fields.Float(string='Pagado', compute='_compute_total_pagado')
    estado = fields.Char(string='Estado', compute='_compute_estado')

    def _compute_total_pagado(self):
        for record in self:
            totalpagado = 0
            for recibo in record.recibos:
                totalpagado += recibo.cancelado_alquiler
            record.total_pagado = totalpagado

    def _compute_estado(self):
        for record in self:
            if record.total_pagado >= record.valor:
                record.estado = 'Pagado'
            else:
                if date.today() > record.fecha_vencimiento:
                    record.estado = 'Vencido'
                elif record.fecha < date.today() < record.fecha_vencimiento:
                    record.estado = 'Vigente'
                elif date.today() < record.fecha:
                    record.estado = 'Futuro'
                else:
                    record.estado = 'Futuro'

    def cobrarClickEvent(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/realty/cobrar?id=' + str(self.id),
            'target': 'new',
        }
