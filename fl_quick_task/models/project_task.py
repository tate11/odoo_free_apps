# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    date_deadline = fields.Date(string='Deadline', default=lambda self: fields.Date.today())
