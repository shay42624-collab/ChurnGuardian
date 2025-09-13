import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Streamlit UI setup
st.set_page_config(page_title="ChurnGuardian", page_icon="🛡️")
st.title("🛡️ ChurnGuardian: AI Customer Retention Engine")

# User input
feedback = st.text_area("Paste customer feedback or support message")

# Button to trigger analysis
if st.button("Analyze Churn Risk") and feedback.strip():
    st.info("🧠 Analyzing sentiment and churn risk...")

    # Step 1: Analyze sentiment
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Classify this customer message as Positive, Negative, or Neutral."},
            {"role": "user", "content": feedback}
        ]
    )
    sentiment = response.choices[0].message.content.strip()

    # Step 2: Estimate churn risk based on sentiment
    if sentiment == "Negative":
        churn_risk = "High"
    elif sentiment == "Neutral":
        churn_risk = "Medium"
    else:
        churn_risk = "Low"

    # Step 3: Display results
    st.markdown("### 🧾 Analysis Results")
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Estimated Churn Risk:** {churn_risk}")
