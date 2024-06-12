import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd
import requests


def fetch_live_match_data():
    url = "https://www.uefa.com/euro2024/matches/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    matches = []
    match_elements = soup.find_all('div', class_='match-row')

    for match in match_elements:
        team1_element = match.find('div', class_='team team--home')
        team2_element = match.find('div', class_='team team--away')
        score_element = match.find('div', class_='js-score')
        status_element = match.find('div', class_='match-status')

        if team1_element and team2_element and score_element and status_element:
            team1 = team1_element.text.strip()
            team2 = team2_element.text.strip()
            score = score_element.text.strip()
            status = status_element.text.strip()

            matches.append({
                'Team 1': team1,
                'Team 2': team2,
                'Score': score,
                'Status': status,
            })
    return matches

def main():
    st.title("UEFA EURO 2024 Live Match Data")

    data = fetch_live_match_data()

    if data:
        for match in data:
            st.subheader(f"{match['Team 1']} vs {match['Team 2']}")
            st.write(f"Score: {match['Sore']}")
            st.write(f"Status: {match['Status']}")
        
    else:
        st.write("No live match data available at the moment.")

if __name__ == "__main__":
    main()
