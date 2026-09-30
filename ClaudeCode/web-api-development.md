# API Development Task

**NOTE :** Before starting project make new virtual environment in ClaudeCode/ folder named 'venvapi' and you are allowed to do any installation or anything in that but never touch venvv which is part of main folder.

Using the project requirements defined in `CLAUDE.md`, build a complete FastAPI application.

The application should represent a simple **India State News** API.

The frontend concept is an India map where each state displays one news item. Clicking a state should open the news associated with that state.

## API Endpoints

The application should include:

* `GET /indnews` — return news for all states
* `GET /indnews/{state_name}` — return the news for a specific state
* `POST /indnews/{state_name}` — replace/create the news for a specific state
* `DELETE /indnews/{state_name}` — remove the news for a specific state

Each state can have only **one news item** at a time.

When new news is added for a state, the previous news for that state should be replaced.

## News Data

Each news item should contain:

* `state`
* `title`
* `short_description`
* `full_description`
* `thumbnail_url`

Rules:

* `state` is required.
* `title` is required.
* `short_description` is required.
* `full_description` is optional.
* `thumbnail_url` is optional.
* `full_description` should contain no more than 300 words.
* `thumbnail_url` should be accepted as an optional image URL.
* There is no authentication, authorization, user account, or role system.

## Storage

Store the state news in an **in-memory data structure**.

No database is required.

The application should contain sample news for several Indian states so the API can be tested immediately.

## Behaviour

`GET /indnews` should return the available state news so that a frontend could use it to display news on an India map.

`GET /indnews/{state_name}` should return only the news belonging to that state.

`POST /indnews/{state_name}` should first validate the submitted news data and then replace any existing news for that state.

If no thumbnail is provided, the news should still be accepted.

If a state has no news, the API should return an appropriate HTTP error response.

Generate clean, modular, well-documented code following the requirements in `CLAUDE.md`.

Before implementing the application, identify any ambiguous requirements and ask for clarification one question at a time.
