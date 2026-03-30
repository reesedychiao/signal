# Signal

Autonomous news intelligence and briefing agent.

## Overview

The modern news landscape produces thousands of articles daily across hundreds of sources. Existing tools either overwhelm you with everything or algorithmically filter you into a bubble. Signal solves this by allowing you to define your interests, and an autonomous AI agent continuously monitors the information landscape, synthesizes narratives across sources, and delivers structured intelligence briefings on what actually matters within your domains.

## Architecture

## Setup

### Prerequisites

- Python 3.10+
- Docker

### Installation

```bash
git clone ...
cd signal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```
NEWS_API_KEY=your_key_here
```

## Data Sources

- NewsAPI - top headlines
- BBC News RSS
- MIT Tech Review RSS
- The Guardian RSS
