---
name: project_overview
description: India State News API - FastAPI app with in-memory state news storage
metadata:
  type: project
---

## India State News API

**Status**: Complete and tested

**Purpose**: REST API for managing news items associated with Indian states. Frontend displays news on an India map where clicking a state shows associated news.

**Technology Stack**:
- Python 3.12.3
- FastAPI framework
- Uvicorn ASGI server
- Pydantic for validation
- In-memory storage (no database)

**Key Implementation Details**:
- State names normalized to "Capitalized" format (e.g., "Maharashtra")
- Full description limited to 300 words max
- Optional fields: `full_description` and `thumbnail_url`
- Sample data included for 5 Indian states
- Auto-generated API docs at `/docs`
- All 4 REST operations implemented: GET all, GET one, POST (create/replace), DELETE

**Storage**: Python dictionary in memory - data resets on server restart

**How to apply**: When working on this API in future sessions, remember that state names must always be in Capitalized format and validation enforces the 300-word limit.
