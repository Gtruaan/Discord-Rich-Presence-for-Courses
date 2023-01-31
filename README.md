# Discord Rich Presence for Courses 📚
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A quick handler for custom rich presence, made specially to display university courses.

![Displays as Playing \[Course Name\] on Discord](https://i.imgur.com/8Ug2f2o.png)

## Usage

First, you need to install pypresence.

`pip install pypresence`

You'll need to set up a Rich Presence App in the Discord Developer Portal. Paste your App ID in the `app_id` field on `parameters.json`. Make sure to change the name too.

To add courses, edit the ones present in the parameters file. Same if you want to add custom statuses. Make sure to provide a valid image URL for the latter.

Run the interface and the presence handler through the file `main.py`.

## To Do

* Better code formatting
* Remove the hardcoding for status and badge text
* Build into a small desktop app? Maybe with `eel`
* Handle disconnects
* An interface to edit the JSON file without touching it directly


_Made with Python 3.10.7_

