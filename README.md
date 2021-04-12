# Skyblock-Monitor
Quick auction house monitor I wrote for Skyblock

## Webscraper
- The webscraper script scrapes the Skyblock wikipedia page for a list of all items

## Auction house monitor
- The monitor script uses the Hypixel API to access player data and auction house data
- You specify an item from the previously scraped data and along with a price and the script will check all of the item listings for a price at or below the price. If it finds an acceptable item, it sends you an email to let you know
- Requires your account username, API key, UUID. Also it requires a gmail for it ping you (sender address can be the same as recipient address)
- The user interface is uh, not the best, but maybe when I have time I'll improve it
