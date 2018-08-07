# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def send_birthday_wish(self):
        today_date = datetime.today().date()
        for employee in self.env['hr.employee'].search([]):
            if employee.birthday:
                emp_birthdate = datetime.strptime(employee.birthday, '%Y-%m-%d').date()
                if str(today_date) == str(emp_birthdate):
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_employee_template')
                    template_id.send_mail(employee.id, force_send=True)
        for partner in self.env['res.partner'].search([]):
            if partner.birthday:
                cust_birthdate = datetime.strptime(partner.birthday, '%Y-%m-%d').date()
                if str(today_date) == str(cust_birthdate):
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_partner_template')
                    template_id.send_mail(partner.id, force_send=True)