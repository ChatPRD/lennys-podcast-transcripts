# Lenny's Podcast Episode Selector - Usage Guide

## Overview

This front-end application allows you to browse and select episodes from Lenny's Podcast archive. It features a dropdown selector that displays episode metadata including guest information, duration, view counts, and descriptions.

## Files

- **index.html** - The main web interface with episode selector dropdown
- **episodes.json** - JSON file containing metadata for all 269 episodes
- **generate_episodes_data.py** - Python script to regenerate episodes.json from transcript files

## How to Use

### Method 1: Open Directly in Browser (Recommended)

1. Simply open `index.html` in your web browser:
   - Double-click the file, or
   - Right-click and select "Open with" your preferred browser, or
   - Drag and drop the file into your browser window

2. Select an episode from the dropdown menu

3. View the episode metadata including:
   - Episode title
   - Guest name
   - Duration
   - View count
   - Description
   - Direct link to watch on YouTube

### Method 2: Serve with Local Web Server

If you prefer to serve it via a local web server:

```bash
# Using Python 3
python3 -m http.server 8000

# Then open: http://localhost:8000
```

Or using any other static file server.

## Updating Episode Data

If new episodes are added to the `episodes/` directory:

1. Run the data generation script:
   ```bash
   python3 generate_episodes_data.py
   ```

2. This will regenerate `episodes.json` with updated episode metadata

3. Refresh the browser to see the new episodes

## Features

- **269 Episodes**: Complete archive of Lenny's Podcast transcripts
- **Searchable Dropdown**: All episodes sorted alphabetically by guest name
- **Rich Metadata**: View duration, view counts, descriptions, and more
- **YouTube Integration**: Direct links to watch episodes on YouTube
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Beautiful UI**: Modern gradient design with smooth animations

## Technical Details

- Pure HTML/CSS/JavaScript - no build process required
- No external dependencies - works offline once loaded
- Episodes data loaded from JSON file
- Fully responsive and accessible design

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

Enjoy browsing Lenny's Podcast episodes!
