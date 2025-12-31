# UFC Card Scraper and Stats Viewer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Libraries](https://img.shields.io/badge/Libraries-Requests%20%7C%20BeautifulSoup%20%7C%20Pandas-green)

A Python web scraping tool that lets you input any UFC event number, fetches the full fight card from the official UFC website, and displays:

- All matchups (red vs. blue corner)
- Weight class
- Results (method, round, time) for past events
- Detailed official stats for each fighter (striking/takedown accuracy, per-minute rates, win methods, defense, etc.)

Future goal: Add a simple ML-based win probability estimation for upcoming fights using fighter stats.

## Motivation

I built this to practice web scraping on a more complex, dynamic website (ufc.com). The goal was to create a command-line tool where you enter a UFC event number and get back the entire card with rich fighter details—something fun and useful for MMA fans.

I also plan to extend it with machine learning: for upcoming events, predict win probabilities; for past events, just show results.

## How It Works

1. **Input**: Enter a valid UFC event number (e.g., 323 for a past event, or the next upcoming one).
2. **Event Page**: The script constructs the URL (`https://www.ufc.com/event/ufc-` + number) and scrapes the fight card.
3. **Fighter Stats**: Using fighter names, it visits each athlete's official page and extracts career stats.
4. **Output**: Prints a clean, formatted view of the card with results and individual fighter breakdowns.

Example (for past events like UFC 323):
- Matchups and results
- Per-fighter sections with striking, takedowns, win methods, and more

## Current Status

- Works for displaying events: Card details + comprehensive fighter stats
- error handling for missing pages or incomplete data

**Known Limitations**:
- Old events (pre-UFC 100) have different HTML structures and limited stats—some data may be incomplete or skipped.
- The UFC website's HTML isn't always uniform, which was the biggest challenge (required careful selector handling and fallbacks).

The prediction feature (ML estimation) is next, looking for a reliable and accurate way to create a strong estimation
