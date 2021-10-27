# SteamFind

## What is it?

`SteamFind` is a Steam AppID Resolver Utility, allowing a user to easily find Steam Apps via their IDs, or a query.

It's written completely in Python, and relies on a few different packages (included in `requirements.txt`).

## Features

In it's current version - `v1.0.0` - the program has the following working features:

- ID to ID Lookup.
- Specific ID Lookup.

**ID to ID Lookup**: Performs a Lookup on a user-provided range of IDs.

**Specific ID Lookup**: Performs a Lookup on a Specific user-provided ID.

Upcoming features:

- Query Lookup.
- GUI Mode.


In upcoming versions, `SteamFind` will allow the user to provide a `query`, which will then be used to scrape the entirety of Steam's App IDs, in search of that same `query`.

This process, however, is going to be very slow, to prevent bandwith hogging and bot-detection by Steam's servers.


A `GUI` mode is also being worked on, which will provide the user with a web-based dashboard, with access to all of `SteamFind`'s features.


## Installation

To install `SteamFind`:

- `cd (root_folder)/SteamFind`.
- `pip install -r requirements.txt` | `python -m pip install requirements.txt`.

## Usage

There are a few flags you can set when running `SteamFind`:

- `--id` - To specify a Steam AppID to lookup.
- `--start` - To specify the first Steam AppID for a range-lookup.
- `--end` - To specify the last Steam AppID for a range-lookup.
- `--name` - To specify the Query for a query-lookup (*not available*).
- `--gui` - To launch the program in GUI Mode (*not available*).


**Examples**:

*Command*: `.\steam_find.py --start 1593500 --end 1593550`

*Result*: All Steam AppIDs from `1593500` to `1593550` will be scraped.


*Command*: `.\steam_find.py --id 1593500`

*Result*: Steam App with ID - `1593500` - will be scraped.


*Command*: `.\steam_find.py --name <query>` - *not available*.

*Result*: All of Steam's Library will be scraped, in search of `query`.


## API

To access `SteamFind`'s functionality via an API Endpoint, you can use the following URL:

`https://steamfindapi.herokuapp.com/steamApp?appID=<appID>`

**Example**: [God of War](https://steamfindapi.herokuapp.com/steamApp?appID=1593500)