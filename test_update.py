#!/usr/bin/env python3
import json
import requests
from datetime import datetime

# Test data
test_data = {
    "leftTeam": {"id": 1, "name": "TEST TEAM A", "logo": None},
    "rightTeam": {"id": 2, "name": "TEST TEAM B", "logo": None},
    "leftScore": 2,
    "rightScore": 1,
    "seriesName": "GARENA MASTERS IX",
    "seriesNumber": "TEST SERIES"
}

print("🧪 Testing Tournament Update System")
print("-" * 40)

try:
    # Test server API
    response = requests.post('http://localhost:8000/api/update', 
                           json=test_data, 
                           timeout=5)
    if response.status_code == 200:
        print("✅ Server API: SUCCESS")
    else:
        print(f"❌ Server API: Failed ({response.status_code})")
except Exception as e:
    print(f"❌ Server API: Error - {e}")

try:
    # Also write file directly as backup
    with open('tournament_data.json', 'w') as f:
        json.dump({
            **test_data,
            'timestamp': datetime.now().isoformat(),
            'server_time': datetime.now().timestamp(),
            'last_update': int(datetime.now().timestamp() * 1000)
        }, f, indent=2)
    print("✅ File Write: SUCCESS")
except Exception as e:
    print(f"❌ File Write: Error - {e}")

print(f"\n📊 Test scores: {test_data['leftTeam']['name']} {test_data['leftScore']} - {test_data['rightScore']} {test_data['rightTeam']['name']}")
print("🎬 Check your OBS overlay now!") 