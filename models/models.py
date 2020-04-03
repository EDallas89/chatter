# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chatter(models.Model):
     _name = 'account.bank.statement'
     _inherit = ['account.bank.statement', 'mail.thread', 'mail.activity.mixin']
