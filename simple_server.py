#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import urllib.parse
from datetime import datetime

class TournamentHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/update':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                # Prepare data with timestamp
                file_data = {
                    **data,
                    'timestamp': datetime.now().isoformat(),
                    'server_time': datetime.now().timestamp(),
                    'last_update': int(datetime.now().timestamp() * 1000)  # milliseconds
                }
                
                # Save tournament data (both for API and direct file access)
                with open('tournament_data.json', 'w') as f:
                    json.dump(file_data, f, indent=2)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Updated tournament data: {data.get('leftScore', 0)}-{data.get('rightScore', 0)}")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
                
            except Exception as e:
                print(f"Error updating data: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        
        elif self.path == '/api/animation':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                # Prepare animation data
                anim_data = {
                    **data,
                    'timestamp': datetime.now().isoformat(),
                    'server_time': datetime.now().timestamp()
                }
                
                # Save animation trigger (both for API and direct file access)
                with open('animation_data.json', 'w') as f:
                    json.dump(anim_data, f, indent=2)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Animation triggered: {data.get('type', 'unknown')}")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
                
            except Exception as e:
                print(f"Error triggering animation: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            super().do_POST()
    
    def do_GET(self):
        if self.path == '/api/data':
            try:
                # Read tournament data
                if os.path.exists('tournament_data.json'):
                    with open('tournament_data.json', 'r') as f:
                        data = json.load(f)
                else:
                    data = {
                        'leftTeam': None,
                        'rightTeam': None,
                        'leftScore': 0,
                        'rightScore': 0,
                        'seriesName': 'GARENA MASTERS IX',
                        'seriesNumber': 'SERIES 1',
                        'timestamp': datetime.now().isoformat(),
                        'server_time': datetime.now().timestamp()
                    }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        
        elif self.path == '/api/animation':
            try:
                # Read animation data
                if os.path.exists('animation_data.json'):
                    with open('animation_data.json', 'r') as f:
                        data = json.load(f)
                else:
                    data = {
                        'type': 'none',
                        'timestamp': datetime.now().isoformat(),
                        'server_time': 0
                    }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            # Log requests for debugging
            if self.path.endswith('.json'):
                print(f"[{datetime.now().strftime('%H:%M:%S')}] File request: {self.path}")
            super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    
    # Initialize data files if they don't exist
    if not os.path.exists('tournament_data.json'):
        initial_data = {
            'leftTeam': None,
            'rightTeam': None,
            'leftScore': 0,
            'rightScore': 0,
            'seriesName': 'GARENA MASTERS IX',
            'seriesNumber': 'SERIES 1',
            'timestamp': datetime.now().isoformat(),
            'server_time': datetime.now().timestamp(),
            'last_update': int(datetime.now().timestamp() * 1000)
        }
        with open('tournament_data.json', 'w') as f:
            json.dump(initial_data, f, indent=2)
    
    if not os.path.exists('animation_data.json'):
        initial_anim = {
            'type': 'none',
            'timestamp': datetime.now().isoformat(),
            'server_time': 0
        }
        with open('animation_data.json', 'w') as f:
            json.dump(initial_anim, f, indent=2)
    
    with socketserver.TCPServer(("", PORT), TournamentHandler) as httpd:
        print(f"🎮 Tournament Server Started!")
        print(f"📊 Controller: http://localhost:{PORT}/controller.html")
        print(f"🎬 Overlay: http://localhost:{PORT}/index.html")
        print(f"📡 API: http://localhost:{PORT}/api/data")
        print(f"📁 Files: tournament_data.json & animation_data.json")
        print("-" * 50)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n�� Server stopped") 