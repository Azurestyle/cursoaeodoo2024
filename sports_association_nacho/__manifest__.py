# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Nacho Serra>, Domatix",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web", "portal"
    ],
    
    "data": [
             "wizards/sport_create_match.xml",
             "data/sport_license_data.xml",
             "data/sport_issue_tag_data.xml",
             "data/ir_cron.xml",
             "security/groups.xml",
             "security/ir.model.access.csv",
             "views/sport_issue_views.xml",
             "views/sport_issue_tag_views.xml",
             "views/sport_clinic_views.xml",
             "views/sport_player_views.xml",
             "views/sport_sport_views.xml",
             "views/sport_team_views.xml",
             "views/sport_license_views.xml",
             "views/sport_league_views.xml",
             "views/sport_match_views.xml",
             "views/sport_ticket_views.xml",
             "views/sport_menuitems.xml",
             "wizards/sport_create_issue.xml",
             "wizards/sport_issue_state.xml",
             "report/sport_issue_report.xml",
             "report/sport_league_report.xml",
             "report/sport_match_report.xml",

             ],
}