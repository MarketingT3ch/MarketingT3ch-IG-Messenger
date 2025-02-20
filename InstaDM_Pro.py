from instagrapi import Client
import time
import hashlib
import requests
import random
import base64
import os

# ======================= CONFIGURATION =======================
ENCODED_GITHUB_TOKEN = "Z2hwX0ZYZFlQOHc4ajMycHlIaVQ0UXJiQnR1WnpVMEZ0QTNpeVVUcA=="  # Replace with your encoded token
GITHUB_USERNAME = "MarketingT3ch1"
GITHUB_REPO = "Marketing_T3ch_Approval"
GITHUB_FILE = "approved.txt"  # Approved codes file in GitHub repository

# Decode token before using
GITHUB_TOKEN = base64.b64decode(ENCODED_GITHUB_TOKEN).decode()

CONTACT_DETAILS =r"""


  ___           _                                    ____  __  __ _       ____                 _           
 |_ _|_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   |  _ \|  \/  ( )___  / ___|  ___ _ __   __| | ___ _ __ 
  | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  | | | | |\/| |// __| \___ \ / _ \ '_ \ / _` |/ _ \ '__|
  | || | | \__ \ || (_| | (_| | | | (_| | | | | | | | |_| | |  | | \__ \  ___) |  __/ | | | (_| |  __/ |   
 |___|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/|_|  |_| |___/ |____/ \___|_| |_|\__,_|\___|_|   
                         |___/                                                                             
                                                                                                                    
📌 Purpose   : Automatic Instagram DM's Sending
📌 Supports  : Multi-account & bulk messaging
📌 Version   : 1.1
📌 Developer : Marketing T3ch

🔒 Approval Required!
📢 Send your code to the admin for approval.

📌 Contact Admin:
   📍 Instagram:  marketing_t3ch
   📍 Telegram :  @MarketingT3ch
   📍 WhatsApp :  +923482082405
====================================================================
"""


WAIT_TIME = 30  # 30 seconds
RETRY_INTERVAL = 5  # 5 seconds

# ======================= APPROVAL SYSTEM =======================

def get_pc_identifier():
    """Generate a stable, unique identifier for the current PC."""
    unique_data = os.getenv("COMPUTERNAME", "") + os.getenv("USER", "") + os.getenv("PROCESSOR_IDENTIFIER", "")
    return hashlib.md5(unique_data.encode()).hexdigest()[:12]  # Shortened stable hash

def get_approval_status(approval_code):
    """Check if the approval code exists in the approved.txt file in the GitHub repository."""
    url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/main/{GITHUB_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            approved_codes = response.text.splitlines()
            return approval_code in approved_codes
    except requests.RequestException as e:
        print(f"⚠️ Error checking approval: {e}")
    return False

# Approval Code Generation
approval_code = "MT11-" + get_pc_identifier()[:4] + "-" + get_pc_identifier()[4:8] + "-" + get_pc_identifier()[8:12]

print(CONTACT_DETAILS)
print("\nYour Approval Code:", approval_code)

start_time = time.time()
approved = False

while True:
    if get_approval_status(approval_code):
        print("\n✅ Your approval has been granted. Tool is now running...")
        break
    else:
        elapsed_time = time.time() - start_time
        if elapsed_time > WAIT_TIME:
            print("\nApproval still pending. Please contact the admin.")
            exit()
        print("\n⏳ Approval pending... Retrying in 5 seconds.")
    
    time.sleep(RETRY_INTERVAL)

# ======================= INSTAGRAM BOT CODE =======================


# ✅ Load text files safely
def load_text_file(filename, read_all=False):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip() if read_all else [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found!")
        return []

# ✅ Improved Instagram Login with Safe Session Handling
def login(username, password):
    cl = Client()
    session_file = f"{username}_cookies.pkl"

    # 🔍 Check if session file exists
    if os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            cl.login(username, password)  # Re-authenticate using session
            if cl.username == username:  # Ensure session is for correct user
                print(f"✅ Session loaded successfully for {username}")
                return cl
            else:
                print(f"⚠️ Session file mismatch! Removing and re-logging in for {username}...")
                os.remove(session_file)  # Delete corrupt session
        except Exception as e:
            print(f"⚠️ Error loading session for {username}: {e}. Re-logging in...")
            os.remove(session_file)  # Delete corrupt session

    try:
        cl.login(username, password)  # Fresh login
        cl.dump_settings(session_file)  # Save session properly
        print(f"🔐 New session saved for {username}")
        return cl
    except Exception as e:
        print(f"❌ Login failed for {username}: {e}")
        return None

# ✅ Fetch user ID safely
def fetch_user_id(cl, username):
    try:
        return cl.user_id_from_username(username)
    except Exception as e:
        print(f"⚠️ Skipping {username}, error fetching ID: {e}")
        return None

# ✅ Send DM with full message
def send_dm(cl, usernames, message):
    count = 0

    for username in usernames:
        user_id = fetch_user_id(cl, username)
        if not user_id:
            continue

        try:
            cl.direct_send(message, [user_id])
            print(f"✅ Message sent to {username}")

            count += 1
            if count % 5 == 0:
                print("⏳ Taking 2-minute rest...")
                time.sleep(120)

            delay = random.randint(10, 20)
            print(f"⏳ Waiting {delay} seconds before next message...")
            time.sleep(delay)

        except Exception as e:
            print(f"⚠️ Failed to send message to {username}: {e}")

# ✅ Main function
def main():
    accounts = load_text_file('account.txt')
    usernames = load_text_file('usernames.txt')
    message = load_text_file('message.txt', read_all=True)  # Full message

    if not accounts or not usernames or not message:
        print("⚠️ Error: Required files are missing or empty.")
        return

    for account in accounts:
        try:
            username, password = account.split(':')
            print(f"\n🔄 Logging in as {username}...")
            cl = login(username, password)

            if cl:  # Ensure login was successful
                send_dm(cl, usernames, message)  # Send full message
                print("✅ All users have received messages successfully!")
                time.sleep(random.randint(30, 60))
        except Exception as e:
            print(f"⚠️ Error with account {username}: {e}")

if __name__ == '__main__':
    main()
