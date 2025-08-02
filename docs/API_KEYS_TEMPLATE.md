# 🔐 Secure API Key Sharing

## For Your Development Partner

Hi! Here are the API keys needed for the DnD Bot project. **Please handle these securely:**

### 🤖 Discord Bot Token
```
DISCORD_TOKEN=your_discord_bot_token_here
```

### 🔑 OpenAI API Key
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 🔒 API Secret Key (for bot-server communication)
```
API_SECRET_KEY=your_generated_secret_key_here
```

## 🛡️ Security Instructions

1. **Copy these values to your `.env` files immediately**
2. **Delete this message after copying** (don't leave it in chat/email)
3. **Never commit these to git** (they're in .gitignore)
4. **Don't share with anyone else**

## 📂 Where to put them:

### Discord Bot (.env file location: `discord-bot/.env`)
```
DISCORD_TOKEN=paste_discord_token_here
APP_SERVER_URL=http://localhost:8000
API_SECRET_KEY=paste_secret_key_here
```

### App Server (.env file location: `app-server/.env`)
```
OPENAI_API_KEY=paste_openai_key_here
API_SECRET_KEY=paste_secret_key_here
HOST=0.0.0.0
PORT=8000
DATABASE_URL=sqlite:///./game_sessions.db
```

## 🔄 If you need to regenerate keys:
- **Discord:** Go to Discord Developer Portal → Your App → Bot → Reset Token
- **OpenAI:** Go to OpenAI Platform → API Keys → Create new secret key
- **API Secret:** Use any secure password generator

## ✅ Verification
After setup, both applications should start without "missing API key" errors.

---
**Remember:** Keep these credentials secure! 🔒
