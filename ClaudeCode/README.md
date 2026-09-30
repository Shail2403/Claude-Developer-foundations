# India State News API

A simple FastAPI-based REST API for managing news items associated with Indian states. The API supports CRUD operations on state news and comes with sample data for testing.

## Features

- **GET all news**: Retrieve news for all states
- **GET state news**: Retrieve news for a specific state  
- **POST news**: Create or replace news for a state
- **DELETE news**: Remove news for a state
- **Data validation**: Pydantic validation for all inputs
- **State name normalization**: State names are automatically normalized to "Capitalized" format
- **Word count validation**: Full descriptions limited to 300 words
- **Auto-generated API docs**: Swagger UI at `/docs`

## Project Structure

```
ClaudeCode/
├── main.py                 # FastAPI application
├── requirements.txt        # Project dependencies
├── venvapi/               # Python virtual environment
├── README.md              # This file
└── CLAUDE.md              # Project requirements
```

## Setup and Running

### 1. Create Virtual Environment
```bash
cd ClaudeCode/
python3 -m venv venvapi
source venvapi/bin/activate  # On Windows: venvapi\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 4. Access API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### GET /indnews
Retrieve news for all states.

**Response**: Array of news items

```bash
curl http://localhost:8000/indnews
```

### GET /indnews/{state_name}
Retrieve news for a specific state.

**Parameters**:
- `state_name` (path): Name of the state (e.g., "Maharashtra")

**Response**: News item for the specified state

**Error**: 404 if state has no news

```bash
curl http://localhost:8000/indnews/maharashtra
```

### POST /indnews/{state_name}
Create or replace news for a specific state.

**Parameters**:
- `state_name` (path): Name of the state

**Request Body**:
```json
{
  "state": "Maharashtra",
  "title": "News Title",
  "short_description": "Brief description",
  "full_description": "Detailed description (optional, max 300 words)",
  "thumbnail_url": "https://example.com/image.jpg (optional)"
}
```

**Response**: Created/updated news item with HTTP 201 status

```bash
curl -X POST http://localhost:8000/indnews/maharashtra \
  -H "Content-Type: application/json" \
  -d '{
    "state": "Maharashtra",
    "title": "Tech Hub Growth",
    "short_description": "Mumbai emerging as tech center",
    "full_description": "Maharashtra strengthens its tech hub position...",
    "thumbnail_url": "https://example.com/maharashtra.jpg"
  }'
```

### DELETE /indnews/{state_name}
Delete news for a specific state.

**Parameters**:
- `state_name` (path): Name of the state

**Response**: HTTP 204 No Content on success

**Error**: 404 if state has no news

```bash
curl -X DELETE http://localhost:8000/indnews/maharashtra
```

## Data Format

Each news item contains:
- `state` (required): Name of the state
- `title` (required): News headline
- `short_description` (required): Brief summary
- `full_description` (optional): Detailed description (max 300 words)
- `thumbnail_url` (optional): URL to thumbnail image

## State Name Normalization

State names are automatically normalized to "Capitalized" format (first character uppercase, rest lowercase):
- `maharashtra` → `Maharashtra`
- `DELHI` → `Delhi`
- `tamilnadu` → `Tamilnadu`

## Storage

News data is stored in an in-memory Python dictionary. Sample data is included for the following states:
- Maharashtra
- Karnataka
- Delhi
- Tamil Nadu
- Gujarat

**Note**: Data persists only during the application runtime. Server restart will reset to initial sample data.

## Implementation Details

- **Framework**: FastAPI with Uvicorn server
- **Data Validation**: Pydantic models
- **Type Hints**: Full type hints throughout the codebase
- **API Standards**: RESTful design with proper HTTP status codes
- **Error Handling**: Appropriate HTTP error responses with detailed messages

## Example Usage

### Get all news
```bash
curl http://localhost:8000/indnews | python3 -m json.tool
```

### Get news for a specific state
```bash
curl http://localhost:8000/indnews/karnataka | python3 -m json.tool
```

### Create new news
```bash
curl -X POST http://localhost:8000/indnews/punjab \
  -H "Content-Type: application/json" \
  -d '{
    "state": "Punjab",
    "title": "Agricultural Excellence",
    "short_description": "Punjab leads in agricultural production",
    "full_description": "Punjab is known for its agricultural innovations and production.",
    "thumbnail_url": "https://example.com/punjab.jpg"
  }' | python3 -m json.tool
```

### Replace existing news
```bash
curl -X POST http://localhost:8000/indnews/maharashtra \
  -H "Content-Type: application/json" \
  -d '{
    "state": "Maharashtra",
    "title": "Updated News",
    "short_description": "Updated summary",
    "full_description": "Updated detailed description"
  }' | python3 -m json.tool
```

### Delete news
```bash
curl -X DELETE http://localhost:8000/indnews/karnataka
```

## Code Quality

The project follows:
- **PEP 8**: Python style conventions
- **Type Hints**: Complete type annotations
- **Modular Design**: Clean separation of concerns
- **Documentation**: Docstrings on all functions and classes
- **Validation**: Comprehensive Pydantic validation
