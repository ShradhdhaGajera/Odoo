from odoo import models, fields


class Book(models.Model):
    _name="book"

    name = fields.Char(string="Title")
    author = fields.Char()
    category = fields.Selection([('fiction','Fiction'), ('bio', 'Biography')])
    price = fields.Float()
    publication = fields.Char()
    image = fields.Image()