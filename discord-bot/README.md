# Discord Bot

This is the Discord bot component that handles user interactions for the AI DungeonMaster system.

## Structure

- `src/commands/` - Slash command implementations (`/startgame`, `/join`, `/say`, `/roll`, `/endgame`)
- `src/handlers/` - Event handlers for Discord interactions
- `src/utils/` - Utility functions for bot operations
- `src/config/` - Configuration management
- `requirements/` - Python dependencies

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements/requirements.txt
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Discord bot token and app server URL
   ```

3. Run the bot:
   ```bash
   python src/main.py
   ```

## Commands

- `/startgame [title]` - Initialize a new D&D campaign
- `/join [game_id]` - Join an existing campaign
- `/say [text]` - Perform an action or speak in character
- `/roll [dice]` - Roll dice (e.g., `d20+5`)
- `/endgame` - End the current session (admin only)

## Configuration

See `src/config/` for configuration options including:
- Discord bot token
- Application server URL
- Command cooldowns
- Error handling settings
