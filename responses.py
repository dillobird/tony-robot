from random import choice
from yahoo_api import get_weekly_summary
import json


def get_response(user_message):
    lowered: str = user_message.lower()

    if lowered.startswith('!summary'):
        print('Responding with weekly summary.')
        data = get_weekly_summary()

        if data is None:
            return "Weekly summary response is empty."

        # Parse the JSON data and format the response
        summary = "Weekly Fantasy Football Summary:\n"
        matchups = data.get('fantasy_content').get('league').get('scoreboard').get('matchups').get('matchup')
        for matchup in matchups:
            print(f'Matchup: {matchup}')
            team1 = matchup.get('teams').get('team')[0].get('name')
            team2 = matchup.get('teams').get('team')[1].get('name')
            score1 = matchup.get('teams').get('team')[0].get('team_points').get('total')
            score2 = matchup.get('teams').get('team')[1].get('team_points').get('total')
            summary += f"{team1} vs {team2}: {score1} - {score2}\n"

        return summary

    else:
        if lowered == '':
            return 'Yes?'
        elif 'hello' in lowered:
            return 'Howdy!'
        else:
            return choice(['Huh?',
                           'What??',
                           'I don\'t understand...',
                           'What did you call me???'])