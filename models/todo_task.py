from odoo import api, fields, models
from datetime import datetime, timedelta

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char('Description', required=True)
    gov_dep_id = fields.Many2one('res.partner', string='Gov Department')
    company_id = fields.Many2one('res.partner', string='Work For')
    start_date = fields.Date('Start Date')
    deadline_date = fields.Date('Deadline')
    is_done = fields.Boolean('Done?')
    note = fields.Text('Note')
    amount = fields.Float('Cost Amount')
    remaining_days = fields.Integer(
        string="Remaining Days",
        compute='_compute_remaining_days')
    priority = fields.Selection([('1', 'Low'), ('2', 'High'),('3', 'Very High')],'Priority', default='2')


    @api.depends('deadline_date')
    def _compute_remaining_days(self):
        for task in self:
            if task.deadline_date:
                time_delta = task.deadline_date - fields.Date.today()
                task.remaining_days = time_delta.days
                


# from odoo import models, fields
# from odoo import api
# from datetime import datetime,date, timedelta
# from dateutil.relativedelta import relativedelta
#
#
# class todotask(models.Model):
#     _name='todo.task'
#     _description='to manage your job tasks'
#
#     name=fields.Char('Description', required=True)
#     gov_deprt_id=fields.Many2many('res.partner',string='Gov Department')
#     company=fields.Many2one(
#         'res.partner',
#         string='Work For')
#     start_date=fields.Date('Start Date')
#     deadline_date=fields.Date('Deadline')
#     is_done=fields.Boolean('Done?')
#     note=fields.Text('Note')
#     amount=fields.Float('Cost Amount')
#     remaining_days=fields.Integer(string="Remaining Days")
#
#     @api.onchange('start_date', 'deadline_date', 'remaining_days')
#
#     def calculate_date(self):
#
#          while self.start_date and self.deadline_date:
#
#             #d1 = datetime.strptime(str(self.start_date), '%Y-%m-%d')
#             # d1 = datetime.now().date()
#             # today = datetime.now()
#             # today_str= today.strftime("%Y-%m-%d")
#             # d2 = datetime.strptime(str(self.deadline_date), '%Y-%m-%d')
#             today = datetime.now()
#             today_str = today.strftime("%Y-%m-%d")
#             diff = relativedelta(datetime.strptime(today_str, '%Y-%m-%d').date(),
#                                  datetime.strptime(str(self.deadline_date), '%Y-%m-%d').date())
#             self.remaining_days =str(diff.days)


    # def _search_age(self, operator, value):
    #     today = fDate.from_string(fDate.context_today(self))
    #     value_days = timedelta(days=value)
    #     value_date = fDate.to_string(today - value_days)
    #     # convert the operator:
    #     # book with age > value have a date < value_date
    #     operator_map = {
    #         '>': '<',
    #         '>=': '<=',
    #         '<': '>',
    #         '<=': '>=',
    #     }
    #     new_op = operator_map.get(operator, operator)
    #     return [('deadline_date', new_op, value_date)]






