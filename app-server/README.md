# Application Server

This is the game logic server that manages D&D campaigns and coordinates with the LLM.

## Structure

- `src/api/` - REST API endpoints for Discord bot communication
- `src/game/` - Game logic, state management, and session handling
- `src/llm/` - LLM integration and prompt management
- `src/database/` - Database models and operations
- `src/config/` - Server configuration
- `src/utils/` - Utility functions
- `requirements/` - Python dependencies

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements/requirements.txt
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key, database settings, etc.
   ```

3. Run the server:
   ```bash
   python src/main.py
   ```

## API Endpoints

- `POST /games` - Create a new game session
- `POST /games/{game_id}/join` - Join a game session
- `POST /games/{game_id}/action` - Submit player action
- `GET /games/{game_id}` - Get game state
- `DELETE /games/{game_id}` - End game session

## Features

- Game state persistence
- Player management
- LLM integration for dungeon master responses
- Turn-based action batching
- Dice roll integration
- Game history tracking

## Configuration

See `src/config/` for configuration options including:
- Database settings
- LLM provider settings
- API authentication
- Rate limiting
