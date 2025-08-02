# 🔧 Project Setup Guide

## 🔐 Secure API Key Management

### For Team Members

**⚠️ NEVER commit API keys to the repository!**

#### Option 1: Environment Variables (Recommended)
1. Create a `.env` file in both `discord-bot/` and `app-server/` directories
2. Copy from the respective `.env.example` files
3. Share API keys through secure channels (see below)

#### Option 2: Secure Key Sharing Methods

**🔒 Recommended Secure Sharing Options:**
- **1Password/Bitwarden** - Share via secure password manager
- **Azure Key Vault** - Enterprise-grade secret management
- **GitHub Secrets** - For CI/CD (team access via repository settings)
- **Encrypted messaging** - Signal, WhatsApp, or similar for one-time sharing

**❌ DO NOT use:**
- Email
- Slack/Discord (unencrypted)
- Text messages
- Shared documents

### Setting Up Your Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JahsFactory/dnd-bot.git
   cd dnd-bot
   ```

2. **Set up Discord Bot:**
   ```bash
   cd discord-bot
   cp .env.example .env
   # Edit .env with your values (see sections below)
   ```

3. **Set up Application Server:**
   ```bash
   cd ../app-server
   cp .env.example .env
   # Edit .env with your values
   ```

## 🤖 Discord Bot Setup

### Getting a Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a New Application
3. Go to "Bot" section
4. Create a bot and copy the token
5. Add to `discord-bot/.env`:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

### Bot Permissions Required
- Send Messages
- Use Slash Commands
- Embed Links
- Read Message History

### Inviting Bot to Server
Use this URL format (replace CLIENT_ID with your app's Client ID):
```
https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=2147483648&scope=bot%20applications.commands
```

## 🔑 OpenAI API Setup

### Getting OpenAI API Key
1. Visit [OpenAI API Platform](https://platform.openai.com/)
2. Sign in/create account
3. Go to API Keys section
4. Create new secret key
5. Add to `app-server/.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### API Usage Notes
- Monitor usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)
- Set usage limits to avoid unexpected charges
- Consider using `gpt-3.5-turbo` for development to reduce costs

## 🗄️ Database Setup

### Development (SQLite - Default)
No additional setup required. Database file will be created automatically.

### Production (PostgreSQL - Optional)
1. Install PostgreSQL or use cloud provider
2. Create database: `createdb dndbot`
3. Update `app-server/.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dndbot
   ```

## 🚀 Running the Application

### Discord Bot
```bash
cd discord-bot
pip install -r requirements/requirements.txt
python src/main.py
```

### Application Server
```bash
cd app-server
pip install -r requirements/requirements.txt
python src/main.py
```

## 🧪 Testing Setup

```bash
cd tests
pip install -r requirements.txt
pytest
```

## 🔍 Verification Checklist

- [ ] Discord bot comes online in your server
- [ ] Bot responds to `/ping` (if implemented)
- [ ] Application server starts without errors
- [ ] Can access API docs at `http://localhost:8000/docs`
- [ ] Database connection successful
- [ ] OpenAI API key valid (check server logs)

## 🆘 Troubleshooting

### Common Issues
- **Bot not responding**: Check bot token and permissions
- **Server won't start**: Verify database connection and API keys
- **Import errors**: Ensure virtual environment is activated
- **Permission denied**: Check file permissions and bot server permissions

### Getting Help
1. Check the logs in the respective log files
2. Verify all environment variables are set
3. Ensure all dependencies are installed
4. Check Discord developer console for bot issues
