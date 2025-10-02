# 📊 InstaScrape Dashboard

This project is a Instagram Dashboard built on Streamlit and InstaGPy that fetches and displays Instagram profile metrics — followers, following, posts — for given usernames.
The app also generates a **followers comparison chart** and shows the **latest news headlines** in the sidebar via the News API.

---

## ✨ App Live On

https://instascrape-dashboard.streamlit.app/

---

## 🎥 Getting Started

<img width="2511" height="1315" alt="image" src="https://github.com/user-attachments/assets/e75051a0-4339-4465-9ad0-80aa910b2932" />
<img width="2390" height="1213" alt="image" src="https://github.com/user-attachments/assets/cc5662ba-c77d-4f17-9152-285ff13a29e3" />

You can watch a quick demo of the dashboard here(Use SRMIST mail id):  
📺 **[InstaScrape Dashboard Demo](https://drive.google.com/file/d/1_w0gib8_HrJyLMuzY6CeyxK2xP0m3Cm3/view?usp=sharing)**

---

## 🛠 Features

- Extract Profile Data: Username, full name, followers count, following count, and post counts.
- Generate Rankings: Displays a table ranking the profiles based on followers.
- Visualization: A logarithmic scale bar chart comparing followers across profiles.
- Latest News Sidebar: Pulls the top 5 news articles from News API based on selected topics.
- Multiple Account Analysis: Supports batch username input for multiple profiles providing quick analysis on a clean, interactive dashboard built with Streamlit.

---

## ⚙ Setup

1. Clone the repository:
```bash
git clone https://github.com/your-repo/instascrape-dashboard.git
cd instascrape-dashboard
```
2. Install dependencies:
```bash
pip install instagpy
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run insta_dashboard.py
```
Enter session ID in the sidebar via cookies of Instagram (if not works via hardcode)
Enter Instagram usernames separated by commas
(example: nasa,isrosight,ecell_srmist)

---

## 📚 Dependencies

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **InstaGPy** — Instagram scraping library
- **Requests**
- **BeautifulSoup4, lxml** — for HTML parsing and scraping
- **certifi, emoji, PySocks, urllib3** — required by InstaGPy and requests

---

## 💡 Notes

- Instagram may block scraping if session IDs expire or too many requests are made.
- You may need to update your session ID periodically to avoid errors.

---

Made with ❤️ by **Aditi Ethiraj**

---
