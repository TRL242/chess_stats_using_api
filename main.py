
from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()
USERNAME = 'PolinaKarelina'

ISO = 'BS'

def print_leaderboards():
	data = requests.get('https://api.chess.com/pub/leaderboards').json()
	categories = data.keys()

	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')

print_leaderboards()

def country_info(iso):
	data = requests.get(f'https://api.chess.com/pub/country/{iso}').json()
	print(data)

country_info(ISO)

def print_players_by_country(iso):
	data = requests.get(f'https://api.chess.com/pub/country/{iso}/players').json()
	players = data.items()
	print(players)

print_players_by_country(ISO)


def get_player_rating(username):
	data = requests.get(f'https://api.chess.com/pub/player/{username}/stats').json()
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
	for category in categories:
		print('Category:', category)
		print(f'Current: {data[category]["last"]["rating"]}')
		print(f'Best: {data[category]["best"]["rating"]}')
		print(f'Best: {data[category]["record"]}')

get_player_rating(USERNAME)

def get_most_recent_game(username):
	data = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives').json()
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	printer.pprint(game)

get_most_recent_game(USERNAME)