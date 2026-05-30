# 🏦 Banking Bot

A professional banking assistant powered by Mistral Large AI and Streamlit.

## Features

✅ **AI-Powered Banking Assistant** - Powered by Mistral Large language model
✅ **Real-time Chat Interface** - Interactive Streamlit-based UI
✅ **Banking Expertise** - Handles account inquiries, transactions, loans, and more
✅ **Conversation History** - Maintains chat context throughout the session
✅ **Professional Guidance** - Provides general banking advice and support

## Prerequisites

- Python 3.8+
- Virtual Environment

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/prashantbhaskar1612-pixel/Bank2.git
cd Bank2
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # Linux/Mac
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file in the root directory:
```
MISTRAL_API_KEY=your_api_key_here
```

Get your API key from [Mistral AI](https://console.mistral.ai/)

## Usage

Run the Streamlit app:
```bash
streamlit run banking_bot.py
```

The app will open at `http://localhost:8501`

## What You Can Ask

- Account information and balance inquiries
- Transaction history and details
- Loan and credit information
- Card services and payments
- General banking questions
- Financial advice (general guidance)

## Project Structure

```
Bank2/
├── banking_bot.py          # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Technologies Used

- **Streamlit** - UI Framework
- **Mistral AI** - Language Model API
- **Python** - Backend Language
- **python-dotenv** - Environment management

## Security

⚠️ **Important:**
- Never commit `.env` file to GitHub
- Keep your API key confidential
- Do not share your API key publicly
- For sensitive transactions, always verify with your bank directly

## Notes

This is a general-purpose banking assistant AI. For actual banking transactions or sensitive account changes, always contact your bank directly through official channels.

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.

---

**Created with ❤️ using Streamlit and Mistral AI**
