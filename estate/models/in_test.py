
from odoo import models ,fields,api
from odoo.exceptions import UserError,ValidationError

class MyTest(models.Model):
	_name = 'my.test'
	_description = 'My test'


	name = fields.Char()
	address = fields.Text()
	email = fields.Char()
	pincode = fields.Integer()

class M1(models.Model):
	_inherit = 'my.test'

	country = fields.Char()
	state = fields.Char()
	city = fields.Char()


class M2(models.Model):
	_name = 'm2'
	_inherit = 'my.test'

	pancard = fields.Char()
	adahar = fields.Char()

class M3(models.Model):
	_name = 'm3'
	_inherits = {'my.test':'test_id'}

	test_id = fields.Many2one('')

