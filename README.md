# AI DungeonMaster Bot

A Discord bot system that enables collaborative Dungeons & Dragons gameplay powered by AI.

## 🏗️ Project Structure

```
dndbot/
├── discord-bot/          # Discord bot application
│   ├── src/
│   │   ├── commands/     # Slash command implementations
│   │   ├── handlers/     # Event and interaction handlers
│   │   ├── utils/        # Bot utility functions
│   │   └── config/       # Bot configuration
│   └── requirements/     # Bot dependencies
├── app-server/           # Game logic server
│   ├── src/
│   │   ├── api/          # REST API endpoints
│   │   ├── game/         # Game logic and state management
│   │   ├── llm/          # LLM integration and prompting
│   │   ├── database/     # Database models and operations
│   │   ├── config/       # Server configuration
│   │   └── utils/        # Server utility functions
│   └── requirements/     # Server dependencies
├── shared/               # Shared components between bot and server
│   ├── models/           # Data models and schemas
│   ├── constants/        # Shared constants
│   └── validators/       # Input validation
├── tests/                # Test suites
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   ├── e2e/              # End-to-end tests
│   └── fixtures/         # Test data
├── docs/                 # Documentation
├── scripts/              # Deployment and utility scripts
└── .github/              # GitHub workflows and templates
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Discord Bot Token
- OpenAI API Key (or local LLM setup)

### Quick Start
1. Clone this repository
2. Set up the Discord bot (see `discord-bot/README.md`)
3. Set up the application server (see `app-server/README.md`)
4. Configure environment variables
5. Run both applications

## 📚 Documentation

See the `docs/` folder for detailed documentation:
- [🔧 Setup Guide](docs/SETUP.md) - **START HERE** - Environment setup and API key configuration
- [🗺️ Development Roadmap](docs/ROADMAP.md) - Project phases and team collaboration strategy
- [📋 Requirements](docs/AI_DungeonMaster_Requirements.md) - Original project requirements
- [🔐 API Key Sharing Template](docs/API_KEYS_TEMPLATE.md) - Template for secure credential sharing

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test types
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest tests/e2e/
```

## 🏗️ Architecture

The system consists of two main components:

1. **Discord Bot**: Handles user interactions through Discord slash commands
2. **Application Server**: Manages game logic, state, and LLM communication

Both components communicate through a secure REST API.

## 📄 License

[Your License Here]
