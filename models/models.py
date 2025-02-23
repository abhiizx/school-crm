from odoo import models, fields

class School(models.Model):
    _name = 'school.teacher'
    _description = 'School Teachers'

    name = fields.Char(string='Name', required=True)
    subject = fields.Char(string='Subject', required=True)
    age = fields.Char(string='Age')

class STeacher(models.Model):
    _inherit = 'school.teacher'

    cls = fields.Char(string='Class')
    place = fields.Char(string='Place')

class Principal(models.Model):
    _name = 'school.principal'
    _inherits = {'res.partner':'partner'}
    _description = 'principal delegation inherits'

    partner = fields.Many2one('res.partner', string='partner')