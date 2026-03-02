class Data:

    user_data = {
        'id': "012345",
        'avatar': ("images/tiki.png"),
        'email': "tiki@meow.net",
        'friends': (""),
        'realname': "tiki",
        'username': "tikigirl",
        'alias': "tikigirl",
        'last_login': "1/1/2020",
        'cookie': "asdf123",
        'current_skins': '001',
        'session': ""
    }

    whatsnew_data = [
        {
            "id": "1",
            "date": "11/07/2025",
            "headline": "PATTERN STACK DEMO NOW AVAILABLE",
            "image": "images/itch.png",
            "text": "The Pattern Stack demo is now available on the web! It will first be available on itch.io, with releases for Steam and Epic stores planned in the near future. There are 3 of 10 playable rounds available. The plan for the full release is to include statisics, inventory, achievements and store pages that will be based on a user profile system. There will also be additional bonus rounds to unlock.",
            "time": "6:00pm"
        },
        {
            "id": "2",
            "date": "10/28/2025",
            "headline": "GAME PREVIEW - PATTERN STACK (ANDROID, IOS, STEAM, WEB)",
            "image": "images/game_logo.png",
            "text": "Pattern Stack is a puzzle game where the goal is to match patterns by building stacks of shapes. Shapes are collected by catching them as they move randomly on the screen. Obstacles are mixed in with shapes, and when hit can force the player to start over. Difficulty and game speed increases as the game progresses. Powerups can be gathered along the way to help progress toward a high score and unlock hidden levels.\n\nPlayers are given the option to make a user profile. This will include a username, email address and avatar. If this option is chosen, statistics are logged for each game, and can be viewed at any time. Badges are awarded based on certain achievements and the Stack Store can be used to buy powerups to use later on. Players with profiles will also be rewarded with special gifts each week for their participation.",
            "time": "4:55pm"
        },
        {
            "id": "3",
            "date": "10/24/2025",
            "headline": "INTRODUCING: NEXT ENTITY, AN INDEPENDENT GAME DEVELOPMENT PROJECT",
            "image": "images/nelogo.png",
            "text": "You've just found a new project dedicated to making original games with innovative gameplay. Next Entity games are made with the idea that playability matters most. The goal is to use in-depth algorithms to implement innovative ideas which stem from years of gaming experience.\n\nOvercomplication isn't the objective here... creating exciting and interesting games is. It's mostly for fun anyway, right? The philosophy of Next Entity is to make games people want to enjoy and can keep coming back to. Hopefully what is created within the project will stay fresh and provide something fun to do -- whether the case may be.",
            "time": "8:00am"
        },
    ]

    statistics_data = {
        'id': id,
        'erasers_collected': (0),
        'erasers_used': (0),
        'games_played': (0),
        'games_won': (0),
        'shields_collected': (0),
        'shields_used': (0),
        'slows_collected': (0),
        'slows_used': (0),
        'stops_collected': (0),
        'stops_used': (0),
        'time_played': (0),
        'top_1': (0),
        'top_3': (0),
        'top_5': (0),
        'top_10': (0),
        'total_points': (0),
        'words_spelled': (0),
        'bomb_mines': (0),
        'grow_mines': (0),
        'freeze_mines': (0),
        'blind_mines': (0),
        'shrink_mines': (0)
    }

    inventory_data = {
        'id': id,
        "backgrounds": (0),
        "coins": (10000),
        "music": (0),
        "paid_version": (False),
        "shield": (0),
        "shrink": (0),
        "skins": (0),
        "slow": (0),
        "stop": (0),
        "strike": (0)
    }

    achievements_data = {
        "collect_100_gold": True,
        "collect_1000_gold": False,
        "collect_10000_gold": False,
        "collect_500_gold": False,
        "collect_5000_gold": False,
        "frozen_stack": True,
        "less_than_10_minutes": False,
        "no_powerups": False,
        "win_1_game": False,
        "win_10_games": False,
        "win_100_games": False,
        "win_25_games": False,
        "win_5_games": False,
        "win_50_games": False,
        "with_1_strike": True
    }

    store_data = {
        '100_coins': "$0.99",
        '1000_coins': "$3.99",
        '500_coins': "$7.99",
        '5000_coins': "$29.99",
        'backgrounds': "40",
        'music': "25",
        'paid_version': "300",
        'powerups_pack': "10",
        'shield_pack': "10",
        'shrink_pack': "10",
        'skins': "40",
        'slow_pack': "10",
        'stop_pack': "10",
        'strike_pack': "10"
    }


def __init__(self, **kwargs):
    super(Data, self).__init__(**kwargs)
    

def get_user_data(self):
    return self.user_data
