# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chatterAccountBankStatement(models.Model):
     _name = 'account.bank.statement'
     _inherit = ['account.bank.statement', 'mail.thread', 'mail.activity.mixin']