<img src= "joker bot.png">

![License](https://img.shields.io/github/license/clown83848474/Discord-Bot.svg)
![size](https://img.shields.io/github/repo-size/clown83848474/Discord-Bot)
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Discord.py">

# Joker Bot


> This is my first Discord bot, where I practiced and learned Discord.py and its features. The code might be a bit messy, but it can be helpful for beginners looking to explore the power of the library.

## Features
  * Easy to run (just make sure Discord.py is installed, and run!)
  * Includes DataBase For Economy
  * No external keys needed (besides a Discord Bot token)
  * config.py File So You Dont Need To Edit The Code
  * A Lot Of Commands For Moderation, Economy And More!
  * Clean and beautiful Design For Embeds
### Requirements
  * Python +3.7V
  * Discord.py
  * dotenv
  * youtube_dl
  * wavelink
### Setup
  * ***__1- Installing Requirements:__***
  ```
  pip install discord.py
  pip install dotenv
  pip install youtube_dl
  pip install wavelink
  ```
  * ***__2- Editing config.py:__***
  ```py
  token = "YOUR_TOKEN"
  prefix = "PREFIX"
  help_thumbnail = "BANNER LINK!"
  TICKET_EMBED = "BANNER LINK!"
  POLL_EMBED = "BANNER LINK!"
  THEME_COLOUR = discord.Colour.random()
  ```
  **NOTE: Make Sure To Enable The Intents In Developer Portal**
  <img src="https://discordpy.readthedocs.io/en/stable/_images/discord_privileged_intents.png" >
  
  * ***__3- Running The Code:__***
  ```sh
  python main.py
  ```

## Commands:
* **help**
* **Moderation**: ban , kick , clear , poll
* **Economy**: work , beg , balance , deposit, withdraw , shop , buy , sell , bag | server_coins , servers_shop , buy_item | addcoins_sv , add_money
* **Ticket**: tcreate , tclose
* **Events**: number , giveaway , darkweb
* **Information**: support , server , ping , vote
* **Music**: join , leave , play , pause , stop , resume , volume
## Editing
This bot (and the source code here) might not be easy to edit for inexperienced programmers. The main purpose of having the source public is to show the capabilities of the libraries, to allow others to understand how the bot works, and to allow those knowledgeable about discord.py and Discord bot development to contribute. There are many requirements and dependencies required to edit and compile it, and there will not be support provided for people looking to make changes on their own. Instead, consider making a feature request (see the above section). If you choose to make edits, please do so in accordance with the MIT License.
