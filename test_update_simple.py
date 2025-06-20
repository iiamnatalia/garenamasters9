#!/usr/bin/env python3
import json
from datetime import datetime

# Test data
test_data = {
    "leftTeam": {"id": 1, "name": "TEST TEAM A", "logo": None},
    "rightTeam": {"id": 2, "name": "TEST TEAM B", "logo": None},
    "leftScore": 2,
    "rightScore": 1,
    "seriesName": "GARENA MASTERS IX",
    "seriesNumber": "TEST SERIES",
    "timestamp": datetime.now().isoformat(),
    "server_time": datetime.now().timestamp(),
    "last_update": int(datetime.now().timestamp() * 1000)
}

print("🧪 Testing Tournament Update System (File-based)")
print("-" * 50)

try:
    # Write test data to file
    with open('tournament_data.json', 'w') as f:
        json.dump(test_data, f, indent=2)
    print("✅ tournament_data.json updated successfully!")
    
    # Also create animation test
    with open('animation_data.json', 'w') as f:
        json.dump({
            "type": "slideIn",
            "timestamp": datetime.now().isoformat(),
            "server_time": datetime.now().timestamp()
        }, f, indent=2)
    print("✅ animation_data.json updated successfully!")
    
    print(f"\n📊 Test data written:")
    print(f"   {test_data['leftTeam']['name']} {test_data['leftScore']} - {test_data['rightScore']} {test_data['rightTeam']['name']}")
    print(f"   Series: {test_data['seriesNumber']}")
    print(f"   Timestamp: {test_data['timestamp']}")
    
    print(f"\n🎬 Check your OBS overlay now!")
    print(f"   You should see 'TEST TEAM A 2 - 1 TEST TEAM B'")
    print(f"   The debug panel should show 'file' mode")

except Exception as e:
    print(f"❌ Error: {e}")

print("\n💡 If this works in OBS, we know the file approach works!")
print("💡 If not, there might be a deeper OBS browser issue.") 