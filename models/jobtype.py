from . import models, fields, api

class job_type(models.Model):
    _name='job.type'
    name=fields.Char('Type of work')
    parent_id=fields.Many2one('job.type',
                              string='Typ of Job',
                              ondelet='restrict',
                              index=True)
    chiled_ids=fields.One2many('job.type','parent_id',
                               string='task type')
class resgov(models.Model):

    gov_dep_id=fields.one2many('todo.task','gov_dep_id',string='Gov. Department')