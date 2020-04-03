# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chatter(models.Model):
     _name = 'account.journal'
     _inherit = ['account.journal', 'mail.thread', 'mail.activity.mixin']
