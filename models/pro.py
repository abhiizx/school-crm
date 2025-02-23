from odoo import models, fields


class SalesItems(models.Model):
    _name = 'sales.items'
    _description = 'Sales'

    item = fields.Char(string='Items')
    quantity = fields.Char('Quantity')
    price = fields.Char('Price')

# class AddItems(models.Model):
#     _name = 'prototype.item'
#     _inherit = 'sales.items'
#
#     item = fields.Char(string='Item')
