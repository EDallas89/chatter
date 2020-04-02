# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chatter(models.Model):
      _name = 'account.journal.form'
      _inherit = ['account.journal.form','mail.thread', 'mail.activity.mixin']
