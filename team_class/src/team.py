class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, player):
        self.players.append(player)

    def has_player(self, findplayer):
        player_exists = False
        for player in self.players:
            if player == findplayer:
             player_exists = True
        return player_exists

    def play_game(self, result):
        if result == True:
            self.points += 3