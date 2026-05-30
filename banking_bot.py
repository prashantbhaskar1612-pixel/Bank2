import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Banking Bot",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Banking Assistant Bot")
st.markdown("---")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# System prompt for banking bot
SYSTEM_PROMPT = """You are a professional banking assistant. You help customers with:
- Account information and balance inquiries
- Transaction history and details
- Loan and credit information
- Card services and payments
- General banking questions and guidance
- Financial advice (general guidance only, not personalized investment advice)

Always be helpful, professional, and follow banking compliance guidelines. 
If you don't know something, direct the customer to contact their bank directly.
Never ask for sensitive information like passwords or full card numbers."""

# Get API key
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    st.error("❌ MISTRAL_API_KEY not found. Please set your API key in the .env file or Streamlit secrets.")
    st.info("For Streamlit Cloud, go to Settings → Secrets and add: MISTRAL_API_KEY=your_key")
    st.stop()

# Initialize Mistral client
try:
    from mistralai.client import MistralClient
    client = MistralClient(api_key=api_key)
except ImportError:
    try:
        from mistralai import Mistral
        client = Mistral(api_key=api_key)
    except ImportError:
        st.error("❌ Mistral AI library not installed. Run: pip install mistralai")
        st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask me anything about banking services...")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from Mistral
    with st.spinner("Banking Assistant is thinking..."):
        try:
            # Prepare messages for API
            messages = [{"role": msg["role"], "content": msg["content"]} 
                       for msg in st.session_state.messages]

            # Try with new Mistral API format
            try:
                response = client.chat.complete(
                    model="mistral-large-latest",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *messages
                    ]
                )
                assistant_message = response.choices[0].message.content
            except AttributeError:
                # Fallback to older API format
                response = client.chat(
                    model="mistral-large-latest",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *messages
                    ]
                )
                assistant_message = response.choices[0].message.content

            # Add assistant message to session state
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})

            # Display assistant message
            with st.chat_message("assistant"):
                st.markdown(assistant_message)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure your MISTRAL_API_KEY is valid and has sufficient credits.")

# Sidebar with information
with st.sidebar:
    st.markdown("### 📋 About This Bot")
    st.markdown("""
    This is a banking assistant powered by Mistral Large AI model.

    **Features:**
    - Real-time banking inquiries
    - Transaction assistance
    - General banking guidance
    - Professional customer service

    **Note:** This is an AI assistant. For sensitive transactions or account changes, 
    please contact your bank directly.
    """)

    st.markdown("### 🔧 Info")
    st.markdown(f"""
    **API Status:** {'✅ Connected' if api_key else '❌ Not Connected'}
    **Model:** Mistral Large
    **Messages:** {len(st.session_state.messages)}
    """)

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
