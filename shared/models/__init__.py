"""
Shared data models for the AI DungeonMaster system.

These models are used by both the Discord bot and application server
to ensure consistent data structures across the system.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class Player(BaseModel):
    """Represents a player in a D&D campaign."""
    user_id: str
    name: str
    character_class: Optional[str] = None
    level: int = 1
    stats: Dict[str, Any] = {}
    joined_at: datetime


class GameSession(BaseModel):
    """Represents a D&D game session."""
    game_id: str
    title: str
    dm_user_id: Optional[str] = None
    players: List[Player] = []
    history: List[str] = []
    current_turn: int = 0
    status: str = "active"  # active, paused, ended
    created_at: datetime
    last_active: datetime
    settings: Dict[str, Any] = {}


class PlayerAction(BaseModel):
    """Represents an action taken by a player."""
    game_id: str
    user_id: str
    action_type: str  # say, roll, join, leave
    content: str
    timestamp: datetime
    metadata: Dict[str, Any] = {}


class DMResponse(BaseModel):
    """Represents a response from the AI Dungeon Master."""
    game_id: str
    content: str
    action_results: List[Dict[str, Any]] = []
    next_prompts: List[str] = []
    timestamp: datetime
    metadata: Dict[str, Any] = {}


class DiceRoll(BaseModel):
    """Represents a dice roll result."""
    dice_expression: str  # e.g., "d20+5"
    result: int
    breakdown: str  # e.g., "(15) + 5 = 20"
    timestamp: datetime
    user_id: str
