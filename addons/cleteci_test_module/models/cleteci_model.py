from odoo import models, fields

class CleteciModel(models.Model):
    _name = 'cleteci.model'
    _description = 'Cleteci Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')