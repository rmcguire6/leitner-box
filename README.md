# LEITNER BOX

## Overview

The Leitner box is a tool for using spaced repetition to memorize and remember anything forever.

This app takes a very simple approach.

A first time user inputs a username, password and the number of new cards they want to create every time they use the app.

The app then takes the new user to the create cards page to create that many new cards.

Every user, after the new cards are created and verified, is taken to the practice page.

The new cards for the day are presented first and then the old cards. Any cards that are missed are shown again until all the cards are correctly remembered.

At this point the user sees an ending message with congratulations, statistics on how many cards were gotten right, and a reminder to do it again tomorrow.

When returning to the app the user must log in with email and password before going to the create cards page.

## Features

- The user can create their user settings: their name, password, and the number of new cards they want to create each day.
- The user can create their new cards which are verified by the user and immediately saved to the database.
- The user can use their cards to memorize by vocalizing the answer, clicking the card to see the correct answer, and marking their answer right or wrong. If the user answers wrong the card is put into the undone queue.
- When the user answers all current cards correctly the user sees congratulations, statistics on correctnes, and a reminder to memorize again tomorrow.

### Project Status

- [x] Write epics and user stories
- [x] Sketch page layouts
- [] Wireframe with Figma
- [x] Decide tech stack
- [x] Create Flask backend
- [x] Create database user schema
- [x] Create database card schema
- [x] Create database
- [x] Create test data and load into database
- [x] Create backend routes
- [x] Add Create React App boilerplate
- [x] Create routing and pages
- [] Create login/signup page
