from odoo import models, fields, api

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(related='partner_id.name', inherited=True, readonly=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    team_id = fields.Many2one('sport.team', string='Team')
    birthdate = fields.Date('Birthdate', copy=False)
    age = fields.Integer('Age', compute='_compute_age', store=True)
    starter = fields.Boolean('Starter', default=True, copy=False) 
    position = fields.Char('Position', copy=False)
    sport_name = fields.Char('Sport', related='team_id.sport_id.name', store=True)
    active = fields.Boolean('Active', default=True)

    def action_make_starter(self):
        self.starter = True
    
    def action_make_substitute(self):
        self.starter = False
    
    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days / 365
            else:
                record.age = 0