# blockdag.py

import json
from datetime import datetime
import os

LEDGER_FILE = "blockdag_ledger.json"

def publish_to_blockdag(entry_hash, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {"hash": entry_hash, "timestamp": timestamp}

    # Create the ledger file if it doesn't exist
    if not os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "w") as f:
            json.dump([], f, indent=4)

    # Append the new record
    with open(LEDGER_FILE, "r") as f:
        data = json.load(f)

    data.append(record)

    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return True
