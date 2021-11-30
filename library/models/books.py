
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class Author(models.Model):
    _name = 'author'
    _description = 'Author'

    name = fields.Char()
    address = fields.Text()


class BookCategory(models.Model):
    _name = 'books.category'
    _description = 'Book Category'

    name = fields.Char()


class BookDepartment(models.Model):
    _name = 'books.department'
    _description = 'Book Department'

    name = fields.Char()

class BookPublisher(models.Model):
    _name = 'books.publisher'
    _description = 'Book Publisher'

    name = fields.Char()


class Shelf(models.Model):
    _name = 'shelf'
    _description = 'Shelf'

    name = fields.Char()
    rack_id = fields.Many2one('rack')


class Rack(models.Model):
	_name = 'rack'
	_description = 'Rack'

	name = fields.Char()
	shelf_ids = fields.One2many('shelf', 'rack_id')

class LibraryDemo(models.Model):
    _name = 'books'
    _description = 'Library data'
    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]
    _order = 'price desc'

    name = fields.Char(string="Book Name", default="Book", required=True)
    book_description = fields.Text()
    price = fields.Float()
    # author_ids = fields.One2many('author', 'book_id')
    author_ids = fields.Many2many('author')
    isbn = fields.Integer()
    category_id = fields.Many2one('books.category')
    department_id = fields.Many2one('books.department')
    barcode = fields.Char()
    publisher_id = fields.Many2one('books.publisher')
    edition = fields.Char()  # Many 2 one
    date = fields.Date()
    shelf_id = fields.Many2one('shelf')
    state = fields.Selection([('new', 'New'), ('issued', 'Issued'), ('cancel', 'Cancel')], default='new')

    def action_issued(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Book is cancel")
            record.state = 'issued'

    def action_cancel(self):
        for record in self:
            if record.state == 'issued':
                raise UserError("Book is issued")
            record.state = 'cancel'


class BookIssue(models.Model):
    _name = 'book.issue'
    _description = 'Book issued'

    name = fields.Char(default="User", required=True)
    email = fields.Char()
    address = fields.Text()
    issue_date = fields.Date()   
    ret_date=fields.Date()
    dept_ids = fields.Many2one('books.department','department_id')
    cat_ids = fields.Many2one('books.category','category_id')
    image = fields.Image()  
    rem_days=fields.Char(string="Count Days",readonly=True)
    penlaty=fields.Char(string="Penlaty",readonly=True)
    
  
    @api.onchange('ret_date')
    def _onchange_ret_date(self):
        for record in self:
            if record.ret_date:
                date_format = "%Y-%m-%d"
                book_issued_date = datetime.strptime(str(record.issue_date), date_format)
                book_return_date = datetime.strptime(str(record.ret_date), date_format)
                cntdays = book_return_date - book_issued_date           
                x=str(cntdays).split(",")[0]
                print(x.split("days")[0])
                y=x.split("days")[0]
                c=int(y)*10
                record.rem_days = int(y) 
                record.penlaty=c
                
            else:
                pass
                #record.rem_days = 0
               
