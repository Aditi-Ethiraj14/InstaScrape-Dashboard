📊 Instagram Profile Dashboard

This is a Streamlit-based Instagram Profile Dashboard that fetches and displays Instagram profile metrics (followers, following, posts) for given usernames. It also shows a ranking chart and latest news in the sidebar.

🛠 Features

Fetch Instagram profile details for one or more usernames.

Display follower count, following count, posts, and account name.

Followers comparison chart (logarithmic scale).

Sidebar with latest news headlines.

Fallback Instagram Session ID: If a session ID is not entered in the sidebar, the app uses a hardcoded session ID from the code.

⚙️ Setup
1. Clone this repository
git clone https://github.com/your-repo/instagram-dashboard.git
cd instagram-dashboard

2. Install dependencies
pip install -r requirements.txt

3. Install required packages manually if needed
pip install streamlit pandas matplotlib instagpy requests

🧩 Usage

Run the app:

streamlit run app.py

Enter Instagram usernames separated by commas (example: champagnepapi,nasa,9gag).


📚 Dependencies

Python 3.x

Streamlit

Pandas

Matplotlib

InstaGPy
 (Instagram scraping library)

Requests

💡 Notes

Instagram may block scraping if session IDs expire or if too many requests are made.

You may need to update your session ID periodically.
