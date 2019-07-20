# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Candidat(models.Model):
    _name = 'candidat.candidat'
    _description = 'Candidat description'
    _sql_constraints = [
        ('num_ins_unique', 'unique(num_ins)', 'numero d\' inscription existe  deja!')
    ]

    name = fields.Char()
    num_ins = fields.Integer()
    session = fields.Many2many('session')
