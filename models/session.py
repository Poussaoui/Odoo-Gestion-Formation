# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Session(models.Model):
    _name = 'session.session'
    _description = 'session description'

    name = fields.Char()
    nb_participants = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char(string='Duree', compute='compute_duree')
    state = fields.Selection([])

    formationId = fields.Many2one('formation.formation', ondelete="cascade")
    categorie = fields.Char(string='categorie',compute='_onchange_formation')
    salle_ids = fields.Many2many('formation.salle', 'session_salle', 'session_id', 'salle_id')
    candidat_ids = fields.Many2many('formation.candidat', 'session_candidat', 'session_id', 'candidat_id')
    formateur_ids = fields.Many2many('formation.formateur', 'session_formateur', 'session_id', 'formateur_id')

    @api.one
    @api.depends('date_debut', 'date_fin')
    def compute_duree(self):
        if self.date_debut and self.date_fin:
            date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
            date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
            self.duree = date_fin - date_debut
        else:
            self.duree = False

    @api.one
    @api.constrains('date_debut', 'date_fin')
    def verif(self):
        date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
        date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
        if date_debut > date_fin:
            raise ValidationError("erreur date fin superieur")

    @api.one
    @api.depends('formationId')
    def _onchange_formation(self):
        self.categorie = self.formationId.categorie