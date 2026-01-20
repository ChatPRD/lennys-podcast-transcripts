# Lenny's Podcast Transcripts Archive

A comprehensive archive of transcripts from [Lenny's Podcast](https://www.youtube.com/@LennysPodcast), organized for easy use with AI coding assistants and language models.

## About Lenny's Podcast

Lenny's Podcast features interviews with world-class product leaders and growth experts, providing concrete, actionable, and tactical advice to help you build, launch, and grow your own product.

## Quick Start

**Browse by topic:** Start with [index/README.md](index/README.md) to explore episodes by topic.

**Search transcripts:**
```bash
grep -r "product-market fit" episodes/
```

## Repository Structure

```
├── episodes/                    # 269 episode transcripts
│   └── {guest-name}/
│       └── transcript.md
├── index/                       # AI-generated topic index
│   ├── README.md                # Main entry point
│   ├── product-management.md    # Episodes about product management
│   ├── leadership.md            # Episodes about leadership
│   └── ...                      # 50+ topic files
└── scripts/
    └── build-index.sh           # Script to regenerate index
```

## Episode Format

Each episode has its own folder named after the guest(s), containing a `transcript.md` file with:

1. **YAML Frontmatter** - Structured metadata including:
   - `guest`: Name of the guest(s)
   - `title`: Full episode title
   - `youtube_url`: Link to the YouTube video
   - `video_id`: YouTube video ID
   - `publish_date`: Publication date (YYYY-MM-DD)
   - `description`: Episode description
   - `duration_seconds`: Episode length in seconds
   - `duration`: Human-readable duration
   - `view_count`: Number of views at time of archival
   - `channel`: Channel name

2. **Transcript Content** - Full text transcript of the episode

## Topic Index

The `index/` folder contains AI-generated keyword tags for each episode, organized by topic:

| Topic | Description |
|-------|-------------|
| [Product Management](index/product-management.md) | 57+ episodes on PM skills and practices |
| [Leadership](index/leadership.md) | Episodes on management and leadership |
| [Growth Strategy](index/growth-strategy.md) | Growth tactics and frameworks |
| [Product-Market Fit](index/product-market-fit.md) | Finding and measuring PMF |

See [index/README.md](index/README.md) for the complete list of 50 topics.

## Rebuilding the Index

The index is generated using Claude CLI. To regenerate:

```bash
./scripts/build-index.sh
```

This processes transcripts through Claude to generate keyword tags. The script is idempotent - it skips episodes already present in keyword files, so it can be run multiple times safely.

## Usage with AI

### Loading Transcripts

Each transcript is a standalone markdown file that can be easily parsed by AI systems. The YAML frontmatter provides structured metadata that can be extracted programmatically.

### Example: Reading a Transcript

```python
import yaml

def read_transcript(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Split frontmatter and content
    parts = content.split('---')
    if len(parts) >= 3:
        frontmatter = yaml.safe_load(parts[1])
        transcript = '---'.join(parts[2:])
        return frontmatter, transcript
    return None, content

# Example usage
metadata, transcript = read_transcript('episodes/brian-chesky/transcript.md')
print(f"Guest: {metadata['guest']}")
print(f"Title: {metadata['title']}")
```

## Episode Count

This archive contains **269 transcripts** from Lenny's Podcast episodes.

## Data Sources

- **Transcripts**: Sourced from the Lenny's Podcast Transcripts Archive
- **Metadata**: Extracted from the [Lenny's Podcast YouTube channel](https://www.youtube.com/@LennysPodcast)

## Contributing

If you notice any issues with the transcripts or metadata, please open an issue or submit a pull request.

## Projects Built with These Transcripts

Here are some projects that have been built using this transcript archive:

**[Lenny Playbook](https://lilys.ai/collections/141200?s=1)** by LilysAI – Turns Lenny Podcast transcripts into structured notes, visual infographics, and a chat interface to explore ideas and get actionable answers.

**[Learn from Lenny](https://x.com/learnfromlenny)** by [@IamAdiG](https://x.com/IamAdiG) - An AI agent on X that provides credible product advice based on Lenny's podcasts. Tag it to get spot-on advice with no fluff.

**[Lenny Skills Database](https://refoundai.com/lenny-skills/)** by Refound AI - A searchable database of 86 actionable skills extracted from 297 podcast episodes. Learn how the best product teams actually work.

**[Lenny MCP](https://github.com/akshayvkt/lenny-mcp)** by [Akshay Chintalapati](https://x.com/akshayvkt) - A Model Context Protocol server that provides access to Lenny's podcast content for AI applications.

**[Recapio - Lenny's Podcast Summaries](https://recapio.com/channel/lennyspodcast)** - AI-generated summaries, transcripts, key insights, and chat interface for Lenny's Podcast episodes.

**[Lenny's Frameworks](https://lennys-frameworks.vercel.app/)** - A collection of frameworks and mental models extracted from Lenny's Podcast episodes.

**[Lenny Listens](https://lenny-listens.vercel.app/)** - Uses Lenny’s interviewing methodology to generate AI-led interviews you can run with real customers.

**[Lenny's Advice Arena](https://lennysadvicearena.lovable.app/)** - An interactive experience for exploring product advice from Lenny's Podcast.

**[Lenny Gallery](https://lennygallery.manus.space/)** by Alan Chan - An infographic gallery with visual summaries of key episodes, built with Manus AI.

**[Lenny Distilled](https://lennydistilled.com)** by [Harsh Nene](https://www.linkedin.com/in/harshnene/) - A curated collection of PM wisdom to dip into anytime...discover a new insight each visit, trace it back to the source quote and YouTube moment. Mapped to the PM craft across 6 dimensions, minimalist design, multiple languages.

**[Lenny's Library in Radia.io](https://getradia.io/resources/lennys-library)** by Kas Eelman - Leveraging transcripts to provide additional insight in to the product competency assessment for Radia users with citations, meta-data and the original episodes.

**[Lenny for Claude](https://github.com/arjunlall/lenny-for-claude)** by [Arjun Lall](https://x.com/_arjun) - MCP server that surfaces podcast advice inside Claude Code and Claude Desktop. Includes /lenny slash command and optional plan mode hook.

**[Lennyhub RAG](https://github.com/traversaal-ai/lennyhub-rag)** by Hamza Farooq - A production grade knowledge graph RAG, enabling multi-turn questions 

**[Lenny Ideation Constellation & Search](https://lennys-search.vercel.app/)** - A semantic search engine and idea explorer for Lenny's Podcast. Find exactly what the guests said, or visually discover how their ideas connect, cluster, and contradict across episodes.

**[LennySan RAG-o-Matic](https://github.com/deanpeters/lennysan-rag-o-matic)** by Dean Peters - A low-barrier, learn-by-building PM pm research tool for exploring Lenny Rachitsky's 320+ podcast episodes using AI and RAG from the CLI, with future support for Jupyter notebooks, time-series exploration, and more.

**[Ask Lenny](https://ask-lenny.vercel.app/)** by Prayerson Christian - AI research assistant that answers questions using real quotes from Lenny's podcast.

**[Lenny's Wisdom Wall](https://lennys-wisdom-wall.vercel.app)** by Shrikant Kadu - An interactive exploration featuring interesting insights and curated contradictions from Lenny's podcast guests.

**[Time Capsule](https://sameerbajaj.com/tools/timecapsule)** by [@sameerbajaj](https://x.com/sameerbajaj) - Describe your situation and get a personalized letter with advice from product leaders who were in your exact moment.

Have you built something with these transcripts? Open a PR to add your project to this list!

## Disclaimer

This archive is for educational and research purposes. All content belongs to Lenny's Podcast and the respective guests. Please visit the official YouTube channel to support the creators.

## License

The transcripts are provided for personal and educational use. Please respect the original content creators' rights.
