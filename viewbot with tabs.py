import subprocess
import time

def generate_profiles(num_profiles):
    profiles = []
    for i in range(num_profiles):
        profile = f"Profile{i+1}"
        profiles.append(profile)
    return profiles

def open_youtube_tabs(num_tabs, link):
    profiles = generate_profiles(num_tabs)
    tabs = []
    for i in range(num_tabs):
        profile = profiles[i]
        args = [
            "chrome",
            "--profile-directory=" + profile,
            link
        ]
        tab = subprocess.Popen(args)
        tabs.append(tab)
        time.sleep(1)  # Wait for a second between opening tabs

# Ask for the number of tabs and the YouTube link
num_tabs = int(input("Enter the total number of tabs to open: "))
youtube_link = input("Enter the YouTube link to open in all tabs: ")

# Open the specified YouTube link in multiple tabs with automatically generated profiles
open_youtube_tabs(num_tabs, youtube_link)
