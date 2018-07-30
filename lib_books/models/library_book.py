# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )
    times_borrowed = fields.Integer('Borrowed', default=0, required=True)

    available_copies = fields.Integer('Available', default=5, required=True)

    @api.multi
    def borrowBook(self):
        if self.available_copies > 0:
            self.times_borrowed += 1
            self.available_copies -= 1

    @api.multi
    def returnBook(self):
        if self.available_copies < 5 and self.times_borrowed > 0:
            self.available_copies += 1
            self.times_borrowed -= 1