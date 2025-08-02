# 🧾 Requirements Document  
**Project Name:** AI DungeonMaster (working title)  
**Purpose:** Allow groups of users to collaboratively play a Dungeons & Dragons-style campaign via Discord, with an AI-powered DM running the adventure through LLM-generated output.

---

## 🧩 1. System Overview

The system enables players to engage in a DnD campaign through Discord using:
- A **Discord Bot**, which facilitates user interaction.
- An **Application Server**, which handles game logic, user inputs, and communication with the LLM (AI Dungeon Master).

The campaign state is tied to a **game ID**, which maps to a long-running adventure and context.

---

## 🛠 2. System Architecture

```
[Discord Users] ⇄ [Discord Bot] ⇄ [Application Server] ⇄ [LLM Backend]
                                                ⇅
                                         [Game State DB]
```

---

## 🧠 3. Key Features

### ✅ MVP Features

#### 3.1 Discord Bot (Client Interface)

- `/startgame [title]` – Initializes a new game and assigns a game ID.
- `/join [game_id]` – Allows users to join a campaign.
- `/say [text]` – Sends player action/input to the DM.
- `/roll [dice]` – Allows rolling dice (e.g., `/roll d20+5`).
- `/endgame` – Ends the session (admin/owner only).
- Display messages from the AI DM as embedded rich messages.
- Session/channel mapping for each game ID.
- Command throttling/anti-spam.

#### 3.2 Application Server (Game Brain)

- Receives input from Discord bot, tagged with game ID and player metadata.
- Stores and maintains game context (history, characters, decisions).
- Batches player input per turn (e.g., once all players have responded or after timeout).
- Sends input to LLM with prompt context (world, players, history).
- Receives LLM output (narrative, consequences) and sends it back to the bot.
- Stores game progression and allows retrieval of logs/history.
- Handles game creation, joining, and persistent context.
- Integrates basic rule logic for rolls if necessary.

---

## 🧰 4. Technical Requirements

### 4.1 Discord Bot

| Requirement             | Details |
|-------------------------|---------|
| Language                | Python (discord.py or pycord), Node.js, or similar |
| Authentication          | Bot token with server invite + slash commands |
| Command Handling        | Slash commands for UX clarity |
| State Management        | Light state per session (game ID ↔ channel) |
| Error Handling          | Informative bot replies for user errors |

### 4.2 Application Server

| Requirement             | Details |
|-------------------------|---------|
| Language                | Python (FastAPI), Node.js (Express), or similar |
| API                     | RESTful endpoints for bot-to-server communication |
| Game State Persistence  | In-memory for MVP, or Redis/PostgreSQL for persistence |
| LLM Integration         | OpenAI API / Local LLM w/ retrieval for history |
| Security                | Auth token or secret key between bot and app server |
| Rate Limiting           | To avoid repeated spam to LLM backend |

### 4.3 LLM Backend

| Requirement             | Details |
|-------------------------|---------|
| Context Window Support  | Long context input for campaign history |
| Fine-tuning             | Optional: Pre-trained with DnD-specific datasets |
| Prompt Format           | Structured: narrative + history + player input |
| Output Constraints      | Return JSON or structured string with narrative, rolls, next options |

---

## 🗃 5. Data Model (Simplified)

### Game Session

```json
{
  "game_id": "abc123",
  "title": "Curse of the Lich Lord",
  "players": [
    {"user_id": "123", "name": "Thorin", "class": "Fighter"},
    {"user_id": "456", "name": "Elara", "class": "Cleric"}
  ],
  "history": ["intro text", "player actions", "DM responses"],
  "current_turn": 5,
  "last_active": "2025-08-01T10:00Z"
}
```

---

## ⏱ 6. Interaction Flow

1. **User** types `/startgame` on Discord.  
2. **Bot** creates a new game ID and informs players to join.  
3. Players join and use `/say` to take actions.  
4. **Bot** batches input and sends it to **App Server**.  
5. **App Server** sends game context + inputs to **LLM**.  
6. **LLM** generates a DM-style response.  
7. **App Server** relays response to **Bot**, which posts it to Discord.  

---

## 🚀 7. Future Features (TODO)

| Feature                       | Description |
|-------------------------------|-------------|
| Character Sheet Integration   | Track stats, skills, equipment |
| Dice Roll Resolution          | Automatic dice parsing and logic |
| Turn Timer / Voting           | Automate turns based on time or majority |
| Voice Channel Integration     | Optional speech-to-text + narration |
| Image Generation              | Scenes/maps/characters via AI image tools |
| Game Save/Resume              | Pause and resume games from DB |
| Dungeon Map Mode              | Collaborative map sharing and movement |
| Player Stats Dashboard        | Track user performance across campaigns |
| Campaign Scripting API        | Allow creators to define worldbuilding triggers and custom events |

---

## 📦 Deployment

| Component     | Target        |
|---------------|---------------|
| Discord Bot   | Azure Container Instance / AWS Lambda / Render |
| App Server    | Azure App Service / EC2 / Fly.io |
| LLM Backend   | OpenAI API (gpt-4-turbo), Local LLM (optional fallback) |
| Database      | Redis (temp state), PostgreSQL (persistent games) |

---

## 🔐 Security Considerations

- Secure token exchange between bot and server.  
- Throttle/queue user inputs to prevent spam.  
- Avoid prompting LLMs with malicious content (sanitize inputs).  
- Use role-based permissions (only GM can `/endgame`, etc.).