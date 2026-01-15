#!/usr/bin/env python3
"""
Parse all Lenny's Podcast episode transcripts and generate a JSON file
with episode metadata for the front-end selector.
"""

import os
import json
import yaml
from pathlib import Path


def parse_episode(episode_dir):
    """Parse a single episode's transcript.md file and extract metadata."""
    transcript_path = episode_dir / "transcript.md"

    if not transcript_path.exists():
        return None

    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split frontmatter and content
        if not content.startswith('---'):
            return None

        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        # Parse YAML frontmatter
        frontmatter = yaml.safe_load(parts[1])

        # Extract metadata
        episode_data = {
            'id': episode_dir.name,
            'guest': frontmatter.get('guest', ''),
            'title': frontmatter.get('title', ''),
            'youtube_url': frontmatter.get('youtube_url', ''),
            'video_id': frontmatter.get('video_id', ''),
            'description': frontmatter.get('description', '').strip(),
            'duration': frontmatter.get('duration', ''),
            'duration_seconds': frontmatter.get('duration_seconds', 0),
            'view_count': frontmatter.get('view_count', 0),
            'channel': frontmatter.get('channel', 'Lenny\'s Podcast')
        }

        return episode_data

    except Exception as e:
        print(f"Error parsing {episode_dir.name}: {e}")
        return None


def main():
    """Main function to parse all episodes and generate JSON."""
    episodes_dir = Path(__file__).parent / "episodes"

    if not episodes_dir.exists():
        print("Error: episodes directory not found")
        return

    episodes = []

    # Parse all episode directories
    for episode_dir in sorted(episodes_dir.iterdir()):
        if episode_dir.is_dir():
            episode_data = parse_episode(episode_dir)
            if episode_data:
                episodes.append(episode_data)

    # Sort episodes by guest name
    episodes.sort(key=lambda x: x['guest'].lower())

    # Write JSON file
    output_path = Path(__file__).parent / "episodes.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(episodes, f, indent=2, ensure_ascii=False)

    print(f"Generated episodes.json with {len(episodes)} episodes")


if __name__ == "__main__":
    main()
