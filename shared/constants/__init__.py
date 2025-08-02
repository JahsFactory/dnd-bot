"""
Shared constants for the AI DungeonMaster system.
"""

# Game Status Constants
GAME_STATUS_ACTIVE = "active"
GAME_STATUS_PAUSED = "paused"
GAME_STATUS_ENDED = "ended"

# Action Types
ACTION_SAY = "say"
ACTION_ROLL = "roll"
ACTION_JOIN = "join"
ACTION_LEAVE = "leave"
ACTION_START_GAME = "start_game"
ACTION_END_GAME = "end_game"

# Discord Command Names
COMMAND_START_GAME = "startgame"
COMMAND_JOIN = "join"
COMMAND_SAY = "say"
COMMAND_ROLL = "roll"
COMMAND_END_GAME = "endgame"

# API Endpoints
API_CREATE_GAME = "/games"
API_JOIN_GAME = "/games/{game_id}/join"
API_PLAYER_ACTION = "/games/{game_id}/action"
API_GET_GAME = "/games/{game_id}"
API_END_GAME = "/games/{game_id}"

# Default Values
DEFAULT_PLAYER_LEVEL = 1
MAX_GAME_HISTORY = 1000
MAX_PLAYERS_PER_GAME = 8
TURN_TIMEOUT_SECONDS = 300  # 5 minutes

# Character Classes
CHARACTER_CLASSES = [
    "Fighter", "Wizard", "Rogue", "Cleric", "Ranger", "Barbarian",
    "Bard", "Druid", "Monk", "Paladin", "Sorcerer", "Warlock"
]

# Dice Types
VALID_DICE = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
