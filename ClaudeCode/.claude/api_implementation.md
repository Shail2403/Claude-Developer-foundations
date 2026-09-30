---
name: api_implementation
description: Complete CRUD API endpoints for state news management
metadata:
  type: project
---

## API Implementation Details

**File**: `main.py` (186 lines)

### Endpoints

1. **GET /indnews**
   - Returns all available state news
   - Response: Array of NewsResponse objects
   - Status: 200 OK

2. **GET /indnews/{state_name}**
   - Returns news for specific state
   - Response: Single NewsResponse object
   - Status: 200 OK if found, 404 if not

3. **POST /indnews/{state_name}**
   - Creates new or replaces existing news
   - Request body: NewsItem with validation
   - Response: Created/updated NewsResponse
   - Status: 201 Created
   - Validation: full_description max 300 words

4. **DELETE /indnews/{state_name}**
   - Deletes news for specific state
   - Status: 204 No Content if successful, 404 if not found
   - Response: Empty (no content)

### Data Models

**NewsItem** (Request model - includes validation):
- `state`: required, string
- `title`: required, string
- `short_description`: required, string
- `full_description`: optional, string (max 300 words)
- `thumbnail_url`: optional, string (URL format)

**NewsResponse** (Response model):
- `state`: capitalized string
- `title`: string
- `short_description`: string
- `full_description`: optional, string
- `thumbnail_url`: optional, string

### Sample Data

Pre-loaded states (created at app startup):
- Maharashtra
- Karnataka
- Delhi
- Tamil Nadu
- Gujarat

Each with sample news about tech, industry, or development.

### Key Functions

- `normalize_state_name(state: str) -> str`: Converts to Capitalized format
- `get_all_news()`: GET /indnews
- `get_state_news(state_name: str)`: GET /indnews/{state_name}
- `create_or_replace_news(state_name: str, news: NewsItem)`: POST /indnews/{state_name}
- `delete_state_news(state_name: str)`: DELETE /indnews/{state_name}

### Validation

- Pydantic field validator on `full_description` rejects if > 300 words
- State names automatically normalized via `normalize_state_name()`
- All required fields must be provided
- Optional fields can be None or omitted

### Auto-Generated Documentation

- Swagger UI: `/docs`
- ReDoc: `/redoc`
- OpenAPI schema: `/openapi.json`
