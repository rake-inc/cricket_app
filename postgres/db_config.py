"""
Database configuration:
uses : settings.py
"""

ENGINE = 'django.db.backends.postgresql'
DB_NAME = 'cricket'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'crunchbang'
PORT = '5432'

TEAM_MODEL = 'team.Team'
MATCH_MODEL = 'match.Match'
TEAM_A_MODEL = 'team_a_id'
TEAM_B_MODEL = 'team_b_id'
PLAYER_MODEL = 'players.Player'
BATSMAN_MODEL = 'bats_man_id'
BOWLER_MODEL = 'bowler_id'