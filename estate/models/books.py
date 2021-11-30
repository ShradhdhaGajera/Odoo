from odoo import models,fields

class Author(models.Model):
	_name = 'author'
	_description = 'Author'

	name = fields.Char()
	address = fields.Text()
	# books_id = fields.Many2one('books')

class BookCategory(models.Model):
	_name = 'book.category'
	_description = 'Books category'

	name = fields.Char() 

class BookDepartment(models.Model):
	_name = 'book.department'
	_description = 'Book Department'

	name = fields.Char()


class Rack(models.Model):

	_name = 'rack'
	_description = 'Rack'


	name = fields.Char()
	shelf_ids = fields.One2many('rack','rack_id')


class Shelf(models.Model):
	_name = 'shelf'
	_description = 'Shelf'


	name = fields.Char()
	rack_id = fields.Many2one('rack')




class Bools(models.Model):
	_name = 'books'
	_description = 'Books'
	_sql_constarints = [('isbn_unique','unique(isbn)','Dublicate isbn not allowed')]


	name = fields.Char()

	price = fields.Float()

	#author_id  = fields.One2many('author','books_id')

	author_ids = fields.Many2many('author')

	isbn = fields.Integer()

	category_id = fields.Many2one('book.category')

	department_id = fields.Many2one('book.department')

	edition = fields.Char()

	date = fields.Date()

	shelf_id = fields.Many2one('shelf')


