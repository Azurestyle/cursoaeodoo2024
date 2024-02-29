from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True)
    team_id = fields.Many2one('sport.team', string='Team')
    age = fields.Integer('Age')
    starter = fields.Boolean('Starter')
    position = fields.Char('Position')

    def action_make_starter(self):
        self.starter = True
    
    def action_make_substitute(self):
        self.starter = False