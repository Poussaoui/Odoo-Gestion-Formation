# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Formateur(models.Model):
    _name = 'formateur.formateur'
    _description = 'Formateur description'
    _sql_constraints = [
        ('matricule_unique', 'unique(matricule)', 'matricule existe  deja!')
    ]

    name = fields.Char()
    matricule = fields.Integer()
    diplome = fields.Char()
    session = fields.Many2many('session')
