# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Salle(models.Model):
    _name = 'salle.salle'
    _description = 'salle description'
    
    name = fields.Char()
    nb_place = fields.Integer(default=20)
    libre = fields.Boolean()

    session = fields.Many2many('session')