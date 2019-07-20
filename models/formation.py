# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Formation(models.Model):
    _name = 'formation.formation'
    _description = 'Formation description'

    name = fields.Char()
    prix = fields.Float()
    sessionId = fields.One2many('session' , 'formationId' , "refernece des session")
