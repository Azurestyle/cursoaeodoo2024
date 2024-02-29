from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True)
    sport_id = fields.Many2one('sport.sport', string='Sport')
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    logo = fields.Image('Logo')

    def action_make_all_starters(self):
        for record in self.player_ids:
            record.action_make_starter()
    
    def action_make_all_substitutes(self):
        for record in self.player_ids:
            record.action_make_substitute()