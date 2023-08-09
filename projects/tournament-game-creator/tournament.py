import logging

logging.basicConfig(format='%(message)s',level=logging.DEBUG)
logger = logging.getLogger()

class Tournament():
    def __init__(self):
        self._num_teams = 0
        self._teams = { }
        self._games_played = 0
        self._matches = { }
    
    def get_num_teams(self):
        return self._num_teams
    
    def set_num_teams(self):
        while True:
            num_teams = input("Enter the number of teams in the tournament: ")
            if int(num_teams) >= 2:
                self._num_teams = int(num_teams)
                break
            else:
                logger.info("The minimum number of teams is 2, try again.")
    
    def get_teams(self):
        return self._teams
    
    def set_teams(self):
        for i in range(self.get_num_teams()):
            while True:
                team = input(f"Enter the name for team #{i + 1}: ")
                
                if len(team.strip().split(" ")) <= 2 and len(team) >= 2:
                    self._teams[team] = 0
                    break

                if len(team) < 2:
                    logger.info("Team names must have at least 2 characters, try again.")
                
                if len(team.strip().split(" ")) > 2:
                    logger.info("Team names may have at most 2 words, try again.")
    
    def get_games_played(self):
        return self._games_played

    def set_games_played(self):
        while True:
            games_played = input("Enter the number of games played by each team: ")
            
            if int(games_played) >= self.get_num_teams() - 1:
                self._games_played = int(games_played)
                break

            logger.info("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    
    def add_team_results(self):
        for team in self.get_teams().keys():
            
            while True:
                num_wins = input(f"Enter the number of wins Team {team} had: ")
                
                if int(num_wins) <= self.get_games_played() and int(num_wins) >= 0:
                    self.get_teams()[team] = int(num_wins)
                    break

                if int(num_wins) > self.get_games_played():
                    logger.info(f"The maximum number of wins is {self.get_games_played()}, try again.")
                
                if int(num_wins) < 0:
                    logger.info("The minimum number of wins is 0, try again.")
                                    
    def start(self):
        self.set_num_teams()
        self.set_teams()
        self.set_games_played()
        self.add_team_results()
    
    def get_matches(self):
        return self._matches
    
    def set_matches(self):
        logger.info("Generating the games to be played in the first round of the tournament...")

        teams = self.get_teams()
        teams_ordered_by_wins = sorted(teams, key= lambda team: teams[team])

        for i in range( int(self.get_num_teams() / 2) ):
            self._matches[i + 1] = {
                "Home": teams_ordered_by_wins[i],
                "Away": teams_ordered_by_wins[(len(teams_ordered_by_wins) - 1) - i],
            }
    
    def print_matches(self):
        for match in self.get_matches().values():
            logger.info(f"HOME: {match['Home']} VS AWAY: {match['Away']}")