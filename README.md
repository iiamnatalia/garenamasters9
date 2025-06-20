# Tournament Overlay System

A local tournament overlay system designed for vMix, OBS, and other streaming software.

## Quick Setup

### 1. Start the Local Server
```bash
python simple_server.py
```
This will start a server at `http://localhost:8000`

### 2. Open the Controller
Open your web browser and go to:
```
http://localhost:8000/controller.html
```

### 3. Set up the Overlay in vMix/OBS

#### For OBS:
1. Add a new "Browser Source"
2. Set the URL to: `http://localhost:8000/index.html`
3. Set Width: `1920` and Height: `1080`
4. Check "Refresh browser when scene becomes active"

#### For vMix:
1. Add Input → Web Browser
2. Set the URL to: `http://localhost:8000/index.html`
3. Set Width: `1920` and Height: `1080`

## How to Use

### Adding Teams
1. In the controller, enter a team name
2. Optionally upload a team logo
3. Click "Add Team"

### Setting up a Battle
1. Select teams from the Left Team and Right Team dropdowns
2. Click "Setup Battle"
3. The overlay will update automatically

### Controlling Scores
- Use the + and - buttons to change scores
- Or use keyboard shortcuts (Ctrl+Q/A for left team, Ctrl+P/L for right team)

### Animations
- Click the animation buttons to trigger slide/fade effects
- Or use keyboard shortcuts (Ctrl+1/2/3/4)

### Status Indicator
The small colored dot in the top-right corner of the overlay shows:
- 🟢 Green: Normal operation
- 🟡 Yellow: Updating/animating
- 🔴 Red: Error

## Keyboard Shortcuts

### Score Control
- `Ctrl+Q`: Left team +1
- `Ctrl+A`: Left team -1
- `Ctrl+P`: Right team +1
- `Ctrl+L`: Right team -1
- `Ctrl+R`: Reset scores
- `Ctrl+T`: Switch teams

### Animations
- `Ctrl+1`: Slide In animation
- `Ctrl+2`: Slide Out animation
- `Ctrl+3`: Fade In animation
- `Ctrl+4`: Fade Out animation

### Other
- `Ctrl+S`: Save match to history
- `Ctrl+B`: Reset entire battle

## Troubleshooting

### Overlay not updating in vMix/OBS
1. Make sure both the controller and overlay are using the same localhost address
2. Try refreshing the browser source in vMix/OBS
3. Check that the local server is still running

### Teams/scores not showing
1. Make sure you've clicked "Setup Battle" after selecting teams
2. Check the controller for any error messages
3. Try clearing your browser cache and reloading

### Fonts not loading
Make sure the `fonts/` folder is in the same directory as the HTML files.

## Technical Notes

- The system now uses **server-based communication** instead of localStorage for OBS/vMix compatibility
- Data is exchanged via HTTP API endpoints (`/api/data` and `/api/animation`)
- Polling occurs every 100ms for responsive updates
- Data is stored in JSON files on the server
- The overlay starts visible by default for streaming software compatibility
- Works reliably across different browser engines (regular browsers, OBS CEF, vMix browsers)

## File Structure
```
├── index.html          # The overlay (for vMix/OBS)
├── controller.html     # The control panel
├── simple_server.py    # Local HTTP server
├── fonts/              # Font files
└── README.md          # This file
``` 