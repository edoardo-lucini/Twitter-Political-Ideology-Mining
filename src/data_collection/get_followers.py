import os
from writers.writers import Writer
import threading

from dotenv import load_dotenv
load_dotenv()

bearer_tokens = os.environ.get("BEARER1")
writer = Writer(bearer_tokens)

lock = threading.Lock() 

def collect_followers(accounts, number_of_followers=float("inf")):
    threads = []
    number_of_followers = float("inf") if "all" else number_of_followers 

    for account in accounts:
        output_path = f"data\\users-list\\raw\\{account}-followers-list.csv"
        threads.append(threading.Thread(target=writer.followers_writer, args=(account, number_of_followers, output_path, lock)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        
if __name__ == "__main__":
    accounts = ["ClientEarth", "EnergySvgTrust", "thecarbontrust", "TheCCoalition"]
    number_of_followers = "all"

    collect_followers(accounts, number_of_followers)
