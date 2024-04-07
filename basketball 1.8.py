import random
import json
import os
import sys
from datetime import datetime, date, timedelta  # Add timedelta to the imports

team_attributes = {
    "Silverpine University": [2, 4, 2, "North", "North Conference"],
    "Redwood Technical Institute": [2, 3, 1, "North", "North Conference"],
    "Northridge Academy of Arts": [2, 3, 1, "North", "North Conference"],
    "Crestview Polytechnic": [2, 2, 2, "North", "North Conference"],
    "Starlight International University": [2, 1, 4, "North", "North Conference"],
    "Blue Harbor College": [2, 2, 2, "South", "North Conference"],
    "Summit Valley University": [1, 1, 2, "South", "North Conference"],
    "Eclipse Science and Technology Institute": [3, 1, 4, "South", "North Conference"],
    "Horizon Community College": [1, 4, 1, "East", "North Conference"],
    "Arcadian Liberal Arts College": [1, 1, 2, "East", "North Conference"],
    "Twilight Vocational School": [3, 2, 4, "East", "North Conference"],
    "Greenwood Agricultural College": [4, 1, 4, "West", "North Conference"],
    "Ironforge Engineering Institute": [3, 4, 4, "West", "North Conference"],
    "Sapphire Coast University": [1, 2, 3, "West", "North Conference"],
    "Misty Mountain College": [1, 2, 4, "West", "North Conference"],
    "Sunlight Business Academy": [1, 3, 4, "West", "North Conference"],
    "Crystal Lake Medical University": [2, 2, 2, "North 2", "North Conference"],
    "Shadow Valley Law School": [3, 1, 3, "North 2", "North Conference"],
    "Marble Cliff Culinary Institute": [4, 1, 2, "North 2", "North Conference"],
    "Golden Plains Conservatory": [3, 2, 4, "North 2", "North Conference"],
    "Phoenix Flight Aviation Academy": [1, 4, 4, "North 2", "North Conference"],
    "Frostpeak Research University": [2, 3, 1, "South 2", "South Conference"],
    "Thunder River Community College": [1, 4, 3, "South 2", "South Conference"],
    "Whisperwind Fine Arts College": [2, 3, 1, "South 2", "South Conference"],
    "Amberfield Music Conservatory": [2, 4, 3, "East 2", "South Conference"],
    "Brightwood Health Sciences Institute": [1, 2, 4, "East 2", "South Conference"],
    "Ravenhill Sports Management College": [3, 3, 3, "East 2", "South Conference"],
    "Moonlight Film and Theater Academy": [2, 4, 4, "East 2", "South Conference"],
    "Skyview Environmental Studies Center": [1, 1, 2, "West 2", "South Conference"],
    "Starfall Language Institute": [2, 1, 2, "West 2", "South Conference"],
    "Evergreen Hospitality College": [4, 2, 4, "West 2", "South Conference"],
    "Wildrose Veterinary School": [3, 3, 1, "West 2", "South Conference"]
}

def generate_schedule(teams):
    print("Entering generate_schedule")
    start_date = date(2024, 11, 9)  # Season's start date
    current_date = start_date
    season_end_date = date(2025, 3, 31)  # Season's end date
    division_games = 8
    conference_games = 12
    out_of_conference_games = 9
    games_per_team = division_games + conference_games + out_of_conference_games
    games_per_week = 2  # Teams can play 1 or 2 games per week

    # Organize teams by division and conference
    divisions = {}  # {division_name: [team1, team2, ...]}
    conferences = {}  # {conference_name: [team1, team2, ...]}
    for team in teams:
        divisions.setdefault(team.division, []).append(team)
        conferences.setdefault(team.conference, []).append(team)

    # Initialize each team's schedule and games count
    for team in teams:
        team.schedule = []  # Clear existing schedules
        team.games_scheduled = 0  # Track the number of games scheduled for each team

    # Main loop to schedule games until the season end date
    while current_date <= season_end_date and not all(team.games_scheduled >= games_per_team for team in teams):
        print(f"Current Date: {current_date}, Season End Date: {season_end_date}")
        weekly_games_scheduled = 0

        print("Finished scheduling games.")

        # Shuffle teams to vary matchups
        random.shuffle(teams)

        for team in teams:
            if team.games_scheduled >= games_per_team:
                continue  # Skip if team has already scheduled all games

    # Schedule games ensuring 1 to 2 games per week
    while not all(team.games_scheduled >= games_per_team for team in teams):
        for team in teams:
            if team.games_scheduled < games_per_team:
                # Schedule Division Games
                if team.games_scheduled < division_games:
                    division_opponents = [t for t in divisions[team.division] if t != team and {'opponent': t.name, 'type': 'division'} not in team.schedule]
                    if division_opponents:
                        opponent = random.choice(division_opponents)
                        team.schedule.append({'date': current_date, 'opponent': opponent.name, 'type': 'division', 'result': None})
                        opponent.schedule.append({'date': current_date, 'opponent': team.name, 'type': 'division', 'result': None})
                        team.games_scheduled += 1
                        opponent.games_scheduled += 1

                # Schedule Conference Games
                elif team.games_scheduled < division_games + conference_games:
                    conference_opponents = [t for t in conferences[team.conference] if t != team and t.division != team.division and {'opponent': t.name, 'type': 'conference'} not in team.schedule]
                    if conference_opponents:
                        opponent = random.choice(conference_opponents)
                        team.schedule.append({'date': current_date, 'opponent': opponent.name, 'type': 'conference', 'result': None})
                        opponent.schedule.append({'date': current_date, 'opponent': team.name, 'type': 'conference', 'result': None})
                        team.games_scheduled += 1
                        opponent.games_scheduled += 1

                # Schedule Out-of-Conference Games
                else:
                    out_of_conference_opponents = [t for conf in conferences if conf != team.conference for t in conferences[conf] if {'opponent': t.name, 'type': 'out-of-conference'} not in team.schedule]
                    if out_of_conference_opponents:
                        opponent = random.choice(out_of_conference_opponents)
                        team.schedule.append({'date': current_date, 'opponent': opponent.name, 'type': 'out-of-conference', 'result': None})
                        opponent.schedule.append({'date': current_date, 'opponent': team.name, 'type': 'out-of-conference', 'result': None})
                        team.games_scheduled += 1
                        opponent.games_scheduled += 1

                # Example placeholder for simplification - to be replaced with actual scheduling logic
                if weekly_games_scheduled < len(teams):
                    # Placeholder opponent selection; replace with actual selection logic
                    opponent = random.choice([t for t in teams if t != team])
                    team.schedule.append({'date': current_date, 'opponent': opponent.name, 'type': 'placeholder', 'result': None})
                    opponent.schedule.append({'date': current_date, 'opponent': team.name, 'type': 'placeholder', 'result': None})
                    team.games_scheduled += 1
                    opponent.games_scheduled += 1
                    weekly_games_scheduled += 2  # Increment by 2 to account for both teams scheduling a game

                # Increment the current_date cautiously
                if any(team.games_scheduled for team in teams):
                    current_date += timedelta(weeks=1)  # Move to the next week after some games are scheduled
                    
                # Increment the current_date cautiously
                if any(team.games_scheduled for team in teams):
                    current_date += timedelta(days=7)  # Ensure only a week passes between scheduling blocks
                    
        # Clean up the temporary 'games_scheduled' attribute
        for team in teams:
            del team.games_scheduled

def simulate_week_by_week(teams):
    current_week = 1
    season_length = 29  # Assuming each team plays 29 games
    
    # Calculate the number of weeks in the season based on the games and assuming two games per week
    total_weeks = (season_length + 1) // 2
    
    for week in range(current_week, total_weeks + 1):
        print(f"\n--- Week {week} ---")
        for team in teams:
            for game in team.schedule:
                if not game['result']:  # If the game hasn't been played
                    simulate_game(game)
        
        input("Press Enter to continue to the next week...")  # Pause for user input to proceed
    
    print("Season ended. Proceeding to playoffs...")

def simulate_game(game, teams):
    # Find teams involved in the game
    team1 = next((t for t in teams if t.name == game['team1_name']), None)
    team2 = next((t for t in teams if t.name == game['team2_name']), None)

    if not team1 or not team2:
        print("Error finding teams for the game.")
        return

    # Simulate the game based on a simplified skill comparison
    result = simulate_based_on_skills(team1, team2)

    # Update the game result
    game['result'] = result
    print(f"Simulated game: {team1.name} vs {team2.name} - {result}")

def simulate_based_on_skills(team1, team2):
    # Placeholder for a simple skill-based simulation
    skill_difference = team1.skill_level - team2.skill_level
    random_factor = random.randint(-10, 10)  # Add some randomness
    net_effect = skill_difference + random_factor

    return 'W' if net_effect >= 0 else 'L'

def simulate_to_end(teams):
    for team in teams:
        for game in team.schedule:
            if not game['result']:  # If the game hasn't been played
                simulate_game(game)  # Use the same game simulation placeholder
    
    print("Season fully simulated. Proceeding to end-of-season activities...")
    
def print_rankings(teams):
    # Sort teams by their wins (descending), losses (ascending)
    sorted_teams = sorted(teams, key=lambda t: (-t.wins, t.losses))
    print("\nTeam Rankings:")
    for team in sorted_teams:
        print(f"{team.name}: {team.wins} Wins, {team.losses} Losses")

def get_sorted_teams(teams):
    # Returns teams sorted by their wins (descending), losses (ascending)
    return sorted(teams, key=lambda t: (-t.wins, t.losses))

def print_news(teams):
    sorted_teams = get_sorted_teams(teams)
    top_team = sorted_teams[0]
    worst_team = sorted_teams[-1]

    # Identifying the top player based on points scored
    top_players = calculate_top_players(teams)
    top_player = top_players[0]  # Assuming the list is sorted by points scored

    # Sample messages based on player performance
    if top_player.points_scored > 500:
        player_performance = "amazing"
        player_news = f"{top_player.name} of {top_player.team_name} has had an amazing season, scoring an impressive {top_player.points_scored} points. A truly remarkable achievement that has fans and critics alike in awe."
    elif 300 < top_player.points_scored <= 500:
        player_performance = "good"
        player_news = f"{top_player.name} of {top_player.team_name} played well this season, contributing significantly with {top_player.points_scored} points. A solid performance that helped the team immensely."
    else:
        player_performance = "bad"
        player_news = f"While {top_player.name} of {top_player.team_name} gave their best, managing only {top_player.points_scored} points this season leaves room for improvement next year."

    # Alternative top team news
    top_alternatives = [
        f"{top_team.name} soared above the competition, finishing with an impressive {top_team.wins}-{top_team.losses} record!",
        f"With a commanding lead, {top_team.name} has set a new league standard, boasting a {top_team.wins}-{top_team.losses} season record.",
        f"{top_team.name}'s unmatched performance this season, ending {top_team.wins}-{top_team.losses}, has fans and critics alike in awe.",
    ]

    # Alternative worst team news
    worst_alternatives = [
        f"{worst_team.name} has faced a tough season, ending with a {worst_team.wins}-{worst_team.losses} record, signaling a time for rebuilding.",
        f"The season proved challenging for {worst_team.name}, which concluded with a disappointing {worst_team.wins}-{worst_team.losses} record.",
        f"Amidst struggles, {worst_team.name} finishes the season at {worst_team.wins}-{worst_team.losses}, looking ahead to a brighter future.",
    ]

    # Generating random news
    random_news = generate_random_news()

    # Select random top and worst news
    top_news = random.choice(top_alternatives)
    worst_news = random.choice(worst_alternatives)

    print("\nEnd of Season News:")
    print(top_news)
    print(worst_news)
    print(player_news)  # Print the player-focused news once
    print("Random News Update:")
    print(random_news)

def print_team_schedule(team):
    print(f"\nSchedule for {team.name}:")
    for game in team.schedule:
        game_date = game['date']
        if isinstance(game_date, str):
            # If the date is a string, parse it back into a date object
            game_date = datetime.strptime(game_date, '%Y-%m-%d').date()
        print(f"{game_date}: vs {game['opponent']} - {'Win' if game['result'] == 'W' else 'Loss'}")

def generate_random_news():
    news_list = [
        "A major upset shook the league last night, with the underdog team securing a surprise victory.",
        "Injuries plague several key players across multiple teams, affecting their performance in upcoming games.",
        "Rumors swirl around potential trades as the trade deadline approaches, with several teams looking to shake up their rosters.",
        "The league commissioner announces new rule changes aimed at increasing the pace of the game and enhancing player safety.",
        "A rookie sensation emerges, showcasing incredible talent and leading their team to unexpected victories.",
        "Controversy erupts as a contentious call by the referees decides the outcome of a crucial match.",
        "An iconic veteran player announces their retirement, marking the end of an illustrious career.",
        "An underperforming team undergoes a coaching change in hopes of turning their season around.",
        "A heated rivalry game ends in a brawl between players, resulting in fines and suspensions from the league.",
        "Fan attendance reaches record highs as excitement builds towards the upcoming playoffs.",
        "A record-breaking performance tonight as a player scores the highest points in a single game this season.",
        "Team chemistry is at an all-time high, with several teams showing exceptional coordination and playmaking.",
        "An underdog team defies expectations, making it to the playoffs against all odds.",
        "A top player is on the verge of breaking the season's scoring record, drawing attention from scouts nationwide.",
        "Defensive strategies dominate this season's play, with record-low scores in multiple games.",
        "A legendary coach announces plans to retire after this season, ending a decades-long career.",
        "Newcomers make their mark, with rookies outperforming veterans in several key matches.",
        "A scandal rocks the league, with allegations of unfair play and rule violations.",
        "Unexpected weather conditions lead to the postponement of several key matches, adding to the season's drama.",
        "A heartwarming story of sportsmanship as opposing teams come together to support a charitable cause."
    ]
    return random.choice(news_list)


class Player:
    def __init__(self, name, skill_level, team_name, jersey_number, points_scored=0, rebounds=0, assists=0):
        self.name = name
        self.skill_level = skill_level
        self.team_name = team_name
        self.jersey_number = jersey_number
        self.points_scored = points_scored
        self.rebounds = rebounds
        self.assists = assists

    def to_dict(self):
        return {
            'name': self.name,
            'skill_level': self.skill_level,
            'team_name': self.team_name,
            'jersey_number': self.jersey_number,
            'points_scored': self.points_scored,
            'rebounds': self.rebounds,
            'assists': self.assists,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            skill_level=data['skill_level'],
            team_name=data['team_name'],  # Assuming players know their team's name
            jersey_number=data['jersey_number'],
            # Include other fields as necessary
        )

class Team:
    def __init__(self, name, offense, defense, coaching, division, conference, players):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.coaching = coaching
        self.division = division
        self.conference = conference
        self.players = players  # Store the list of players for this team
        self.wins = 0
        self.losses = 0
        self.schedule = []  # This will hold the team's game schedule

    def all_players(self):
        """Return the list of player objects belonging to the team."""
        return self.players

    def composite_score(self):
        """Calculate and return the team's composite score based on offense, defense, and coaching attributes."""
        return (self.coaching * 0.5) + (self.defense * 0.3) + (self.offense * 0.2)

    def to_dict(self):
        # Convert the team object and its attributes into a dictionary.
        return {
            'name': self.name,
            'offense': self.offense,
            'defense': self.defense,
            'coaching': self.coaching,
            'division': self.division,
            'conference': self.conference,
            'players': [player.to_dict() for player in self.players],  # Assuming Player has a to_dict method
            'wins': self.wins,
            'losses': self.losses,
            'schedule': [{'date': game['date'].isoformat() if isinstance(game['date'], date) else game['date'],
                          'opponent': game['opponent'],
                          'result': game['result']} for game in self.schedule],
        }

    @classmethod
    def from_dict(cls, team_data):
        # First, convert any nested dictionaries for players into Player objects
        players = [Player(**player_data) for player_data in team_data.get('players', [])]
        # Then, create a new Team instance with the data
        team = cls(
            name=team_data['name'],
            offense=team_data['offense'],
            defense=team_data['defense'],
            coaching=team_data['coaching'],
            division=team_data['division'],
            conference=team_data['conference'],
            players=players
        )
        team.wins = team_data.get('wins', 0)
        team.losses = team_data.get('losses', 0)
        # Convert string dates back to date objects in the schedule
        team.schedule = [{'date': datetime.strptime(game['date'], '%Y-%m-%d').date() if isinstance(game['date'], str) else game['date'],
                          'opponent': game['opponent'],
                          'result': game['result']} for game in team_data.get('schedule', [])]
        return team

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play_game(self):
        # Determine the winner based on composite scores or another mechanism
        if random.randint(0, 1) == 0:
            winning_team = self.team1
            losing_team = self.team2
        else:
            winning_team = self.team2
            losing_team = self.team1

        # Increment the win/loss records
        winning_team.wins += 1
        losing_team.losses += 1

        # Randomly update stats for each player
        # These values should be based on how you simulate the game
        for player in winning_team.players:
            player.points_scored += random.randint(10, 30)
            player.rebounds += random.randint(5, 15)
            player.assists += random.randint(3, 10)

        # Less stats for the losing team
        for player in losing_team.players:
            player.points_scored += random.randint(1, 9)
            player.rebounds += random.randint(1, 4)
            player.assists += random.randint(0, 2)

        return f"{winning_team.name} wins"

# Function to calculate top players based on their statistics
def calculate_top_players(teams):
    all_players = []
    for team in teams:
        all_players.extend(team.players)

    # Sort players by their statistics (e.g., points scored) in descending order
    top_players = sorted(all_players, key=lambda player: player.points_scored, reverse=True)
    return top_players

def print_top_players(teams):
    print("\nTop Players (Averages per game):")
    total_games = 29  # Each player plays 29 games in the season

    top_players = calculate_top_players(teams)
    for i, player in enumerate(top_players[:10], start=1):
        avg_points = player.points_scored / total_games
        avg_rebounds = player.rebounds / total_games
        avg_assists = player.assists / total_games

        # Corrected print statement
        print(f"{i}. {player.name} ({player.team_name}): Avg Points: {avg_points:.2f}, Avg Rebounds: {avg_rebounds:.2f}, Avg Assists: {avg_assists:.2f}")

def list_all_teams(teams):
    for idx, team in enumerate(teams, start=1):
        print(f"{idx}. {team.name}")

def get_team_by_index(teams, index):
    if 0 <= index < len(teams):
        return teams[index]
    return None

def print_team_roster(team):
    print(f"\nRoster for {team.name}:")
    for player in team.players:
        print(f"Name: {player.name}, Skill Level: {player.skill_level}")

# Sample data for name generation
first_names = ["Adam", "Bob", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Ian", "Jack", "Kevin", "Liam", "Michael", "Nathan", "Oliver"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Anderson", "Martinez", "Davis", "Garcia", "Rodriguez", "Wilson", "Taylor", "Thomas", "Moore", "Jackson"]

def initialize_players(team_name):
    players = []
    jersey_numbers = list(range(1, 100))  # Jersey numbers from 1 to 99
    random.shuffle(jersey_numbers)  # Shuffle them to assign randomly
    used_names = set()  # Keep track of used names to avoid duplicates

    for i in range(10):  # For 10 players per team
        while True:
            first_name = random.choice(first_names)  # Use your existing list of first names
            last_name = random.choice(last_names)    # Use your existing list of last names
            full_name = f"{first_name} {last_name}"
            if full_name not in used_names:
                used_names.add(full_name)
                break

        skill_level = random.randint(1, 10)
        jersey_number = jersey_numbers.pop()  # Assign and remove a jersey number
        players.append(Player(full_name, skill_level, team_name, jersey_number))
    return players

def initialize_teams():
    teams = []
    for name, (offense, defense, coaching, division, conference) in team_attributes.items():
        players = initialize_players(name)  # Make sure to pass 'name' as 'team_name'
        team = Team(name, offense, defense, coaching, division, conference, players)
        teams.append(team)
    return teams

# Revised end-of-season options
def end_of_season_options(teams, my_team):
    def display_main_menu():
        print("\nMain Menu")
        print("---------")
        print("1. View Rankings")
        print("2. View Schedule")
        print("3. View News")
        print("4. View Top Players")
        print("5. View Roster")
        print("6. Save Game")
        print("7. Exit Game")

    def handle_option(option):
        if option == "1":
            print_rankings(teams)
        elif option == "2":
            print_team_schedule(my_team)
        elif option == "3":
            print_news(teams)
        elif option == "4":
            print_top_players(teams)
        elif option == "5":
            handle_roster_option(teams, my_team)
        elif option == "6":
            save_game()
        elif option == "7":
            exit_game()
        else:
            print("Invalid option. Please try again.")

     
    while True:
        display_main_menu()
        choice = input("\nEnter your option: ")
        handle_option(choice)
        if choice == "7":
            break

def setup_new_game():
    print("Initializing a new game...")
    teams = initialize_teams()  # This initializes all teams
    print("Teams initialized.")
    generate_schedule(teams)  # Generates the schedule for all teams
    return teams, my_teams

def main():
    global team_attributes
    game_loaded = False
    teams = None
    my_team = None
    
    choice = input("Do you want to load a saved game or start a new game? (load/new): ").lower()
    if choice == 'load':
        slot = input("Choose a save slot (1-3): ")
        teams, my_team, game_loaded = attempt_load_game(slot)
    elif choice == 'new':
        print("User chose to start a new game.")
        teams = setup_new_game()  # Setup new game returns only teams without selecting my_team yet
        my_team = select_team(teams)  # Now select my_team from the list of teams
        print("New game setup completed.")
        game_loaded = True  # Treat as if game is "loaded" so it proceeds to simulation

    if game_loaded:
        # Proceed to simulation and end of season options directly after team selection
        print(f"Your team is {my_team.name}.")
        start_season_simulation(teams, my_team)
        end_of_season_options(teams, my_team)
    else:
        print("Failed to load or start a new game. Exiting...")

    # Start the season simulation
    start_season_simulation(teams, my_team)

    # After completing the season simulation, proceed to end-of-season options.
    end_of_season_options(teams, my_team)

def attempt_load_game(slot):
    try:
        with open(f'save_slot_{slot}.json', 'r') as file:
            saved_data = json.load(file)
        print("Game loaded successfully.")
    except Exception as e:
        print(f"Error loading game: {e}")

        # Process the saved data to restore game state
        teams = [Team.from_dict(team_data) for team_data in saved_data['teams']]
        my_team = Team.from_dict(saved_data['my_team'])
        print("Game loaded successfully.")
        return teams, my_team, True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Failed to load game: {e}")
        return None, None, False
    else:
        print("No saved games found.")
    return False

def initialize_new_game():
    print("Initializing a new game...")
    teams = initialize_teams()  # Initialize teams for a new game
    generate_schedule(teams)
    my_team = select_team(teams)  # Let the user select a team
    print(f"Your team is {my_team.name}.")
    return teams, my_team

def process_saved_data(saved_data):
    # Assuming saved_data is a dictionary with 'teams' and 'my_team' keys
    # and your Team class has a from_dict class method for instantiation
    teams_data = saved_data.get('teams', [])
    my_team_data = saved_data.get('my_team', None)

    teams = [Team.from_dict(team_dict) for team_dict in teams_data]

    # Find 'my_team' in the loaded teams by matching a unique identifier, such as the team's name.
    my_team = next((team for team in teams if team.name == my_team_data['name']), None)

    return teams, my_team

def select_team(teams):
    print("Entering select_team")
    print("Here are the available teams:")
    for i, team in enumerate(teams, start=1):
        print(f"{i}. {team.name}")
    choice = input("Pick your team or have one randomly assigned (pick/random): ").lower()
    if choice == 'pick':
        team_number = int(input("Enter the number of your team: ")) - 1
        my_team = teams[team_number]
    else:
        my_team = random.choice(teams)
    print(f"Your team is {my_team.name}.")
    return my_team

def start_season_simulation(teams, my_team):
    start_choice = input("Start at Week 1 and simulate every week ('week') or simulate straight to the end ('end')? ").lower()
    if start_choice == "week":
        simulate_week_by_week(teams)
    elif start_choice == "end":
        simulate_to_end(teams)
    else:
        print("Invalid option. Starting week-by-week simulation.")
        simulate_week_by_week(teams)

    # Re-integrating the roster option functionality
    while True:
        option = input("\nWould you like to view rosters or exit? (roster/exit): ").lower()
        if option == 'roster':
            handle_roster_option(teams, my_team)
        elif option == 'exit':
            print("Exiting the game. Thank you for playing!")
            break
        else:
            print("Invalid option, please try again.")

def handle_roster_option(teams, my_team):
    roster_choice = input("Type 'own' to view your team's roster or 'other' to view another team's roster: ").lower()
    if roster_choice == 'own':
        print_team_roster(my_team)
    elif roster_choice == 'other':
        list_all_teams(teams)
        team_number = int(input("Enter the number of the team you wish to see the roster for: ")) - 1
        selected_team = get_team_by_index(teams, team_number)
        if selected_team:
            print_team_roster(selected_team)
        else:
            print("Invalid team selection.")
    else:
        print("Invalid option. Please type 'own' or 'other'.")

# Add this function definition to your script
def exit_game():
    print("Exiting the game. Thank you for playing!")
    sys.exit(0)

if __name__ == "__main__":
    main()
