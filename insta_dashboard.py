import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from instagpy import InstaGPy
import requests

st.set_page_config(page_title="Instagram Dashboard", layout="wide")


with st.sidebar:
    st.title("⚙ Config & News")
    SESSION_ID = st.text_input("Enter Instagram Session ID", type="password")

    st.markdown("### 📰 Latest News")
    topic = st.selectbox("Select Topic", ["Technology", "Science", "Business", "Sports", "Entertainment"])
    news_api_key = "2816297eacfc4a069e0bf69417caa7ef"

    def fetch_news(topic):
        url = f"https://newsapi.org/v2/top-headlines?category={topic.lower()}&language=en&apiKey={news_api_key}"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()["articles"][:5]
        return []

    news_articles = fetch_news(topic)
    for article in news_articles:
        st.markdown(f"[{article['title']}]({article['url']})")
        if article.get("urlToImage"):
            st.image(article["urlToImage"], width="stretch")


st.title("📊 InstaScrape Dashboard")
st.markdown("Enter Instagram usernames (comma separated) and see follower rankings.")

usernames_input = st.text_area(
    "Enter Instagram usernames",
    value="nasa,isrosight,ecell_srmist,srmuniversityofficial,ecell_srmuap,iitbombay_ecell,srmdei.official,srmschoolofcomputing,startup.pedia,srmist_dsa"
)

HARDCODED_SESSION_ID = "YOUR_HARDCODED_SESSION_ID_HERE"

if st.button("Fetch Data"):
    if not SESSION_ID:
        SESSION_ID = HARDCODED_SESSION_ID  

    insta = InstaGPy(
        use_mutiple_account=False,
        session_ids=[SESSION_ID]
    )

    usernames = [u.strip() for u in usernames_input.split(",") if u.strip()]
    if not usernames:
        st.warning("⚠ Please enter at least one username.")
    else:
        data = []
        errors = []
        with st.spinner("Fetching data..."):
            for username in usernames:
                try:
                    details = insta.get_user_basic_details(username, pretty_print=False)
                    data.append({
                        "Username": details["username"],
                        "Full Name": details["full_name"],
                        "Followers": details["follower_count"],
                        "Following": details["following_count"],
                        "Posts": details["media_count"]
                    })
                except Exception as e:
                    errors.append(f"Error fetching {username}: {e}")

        if errors:
            st.error("⚠ Some errors occurred:")
            for err in errors:
                st.write(err)

        if data:
            df = pd.DataFrame(data).sort_values(by="Followers", ascending=False).reset_index(drop=True)

            df.index = df.index + 1
            df = df.head(len(usernames))

            st.subheader("📈 Instagram Accounts Ranking")
            st.dataframe(df, width=1000, height=400)

            st.subheader("📊 Followers Comparison Chart")
            fig, ax = plt.subplots(figsize=(12, 6))  # wider figure for labels
            ax.bar(df["Username"], df["Followers"], color="skyblue")
            ax.set_yscale("log")
            ax.set_ylabel("Followers")
            ax.set_xlabel("Username")
            ax.set_title("Instagram Followers Comparison")
            ax.set_xticks(range(len(df["Username"])))
            ax.set_xticklabels(df["Username"], rotation=45, ha="right", fontsize=9)
            for i, v in enumerate(df["Followers"]):
                ax.text(i, v, f"{v:,}", ha="center", va="bottom", fontsize=8)
            plt.tight_layout()
            st.pyplot(fig)

st.markdown("""
---
Created with ❤️ by Aditi Ethiraj 
""")
