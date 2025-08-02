"""
Input validators for the AI DungeonMaster system.
"""

import re
from typing import Optional
from ..constants import VALID_DICE, CHARACTER_CLASSES, MAX_PLAYERS_PER_GAME


def validate_game_id(game_id: str) -> bool:
    """Validate game ID format."""
    if not game_id or len(game_id) < 3 or len(game_id) > 50:
        return False
    return re.match(r'^[a-zA-Z0-9_-]+$', game_id) is not None


def validate_dice_expression(expression: str) -> bool:
    """Validate dice roll expression (e.g., 'd20+5', '2d6')."""
    if not expression:
        return False
    
    # Basic dice expression pattern
    pattern = r'^(\d+)?d(\d+)([+-]\d+)?$'
    return re.match(pattern, expression.lower().replace(' ', '')) is not None


def validate_character_name(name: str) -> bool:
    """Validate character name."""
    if not name or len(name) < 2 or len(name) > 30:
        return False
    return re.match(r'^[a-zA-Z0-9\s\-_\']+$', name) is not None


def validate_character_class(character_class: Optional[str]) -> bool:
    """Validate character class."""
    if character_class is None:
        return True
    return character_class in CHARACTER_CLASSES


def validate_game_title(title: str) -> bool:
    """Validate game title."""
    if not title or len(title) < 3 or len(title) > 100:
        return False
    return True


def validate_player_action(content: str) -> bool:
    """Validate player action content."""
    if not content or len(content) > 2000:  # Discord message limit
        return False
    return True


def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    if not text:
        return ""
    
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '&', '"', "'", '\\', '/', '`']
    sanitized = text
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, '')
    
    return sanitized.strip()
