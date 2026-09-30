"""
India State News API - A simple FastAPI application for managing state-wise news.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from typing import Optional

app = FastAPI(
    title="India State News API",
    description="REST API for managing news items for Indian states",
    version="1.0.0"
)


class NewsItem(BaseModel):
    """Model for news data with validation."""
    state: str = Field(..., description="State name (required)")
    title: str = Field(..., description="News title (required)")
    short_description: str = Field(..., description="Brief description (required)")
    full_description: Optional[str] = Field(None, description="Detailed description (optional, max 300 words)")
    thumbnail_url: Optional[str] = Field(None, description="URL for news thumbnail (optional)")

    @field_validator("full_description")
    @classmethod
    def validate_description_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensure full_description does not exceed 300 words."""
        if v is None:
            return v
        word_count = len(v.split())
        if word_count > 300:
            raise ValueError(f"full_description must not exceed 300 words (got {word_count})")
        return v


class NewsResponse(BaseModel):
    """Response model for news data."""
    state: str
    title: str
    short_description: str
    full_description: Optional[str] = None
    thumbnail_url: Optional[str] = None


def normalize_state_name(state: str) -> str:
    """Normalize state name to 'Capitalized' format (first char capital, rest lowercase)."""
    return state.strip().capitalize()


# In-memory storage with sample data for Indian states
news_database: dict[str, NewsResponse] = {
    "Maharashtra": NewsResponse(
        state="Maharashtra",
        title="Tech Hub Growth",
        short_description="Mumbai emerging as global tech center",
        full_description="Maharashtra continues to strengthen its position as India's tech hub with numerous startups and IT companies establishing offices in Mumbai and Pune.",
        thumbnail_url="https://example.com/maharashtra.jpg"
    ),
    "Karnataka": NewsResponse(
        state="Karnataka",
        title="Bengaluru Innovation",
        short_description="Silicon Valley of India leads innovation",
        full_description="Bengaluru remains at the forefront of India's tech revolution, hosting numerous IT companies and startups.",
        thumbnail_url="https://example.com/karnataka.jpg"
    ),
    "Delhi": NewsResponse(
        state="Delhi",
        title="Capital Development",
        short_description="Major infrastructure projects underway",
        full_description="Delhi witnesses significant infrastructure development with metro expansion and smart city initiatives.",
        thumbnail_url="https://example.com/delhi.jpg"
    ),
    "Tamil Nadu": NewsResponse(
        state="Tamil Nadu",
        title="Industrial Growth",
        short_description="Manufacturing sector expansion",
        full_description="Tamil Nadu's manufacturing and textile industries continue to grow, attracting major investments.",
        thumbnail_url="https://example.com/tamil_nadu.jpg"
    ),
    "Gujarat": NewsResponse(
        state="Gujarat",
        title="Business Excellence",
        short_description="Business-friendly environment attracts investors",
        full_description="Gujarat continues to be a preferred destination for businesses with its business-friendly policies.",
        thumbnail_url="https://example.com/gujarat.jpg"
    ),
}


@app.get("/indnews", response_model=list[NewsResponse])
def get_all_news() -> list[NewsResponse]:
    """
    Retrieve news for all states.

    Returns:
        List of news items for all states with available news.
    """
    return list(news_database.values())


@app.get("/indnews/{state_name}", response_model=NewsResponse)
def get_state_news(state_name: str) -> NewsResponse:
    """
    Retrieve news for a specific state.

    Args:
        state_name: Name of the state (e.g., 'Maharashtra')

    Returns:
        News item for the specified state.

    Raises:
        HTTPException: 404 if state has no news.
    """
    normalized_state = normalize_state_name(state_name)

    if normalized_state not in news_database:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No news found for state: {normalized_state}"
        )

    return news_database[normalized_state]


@app.post("/indnews/{state_name}", response_model=NewsResponse, status_code=status.HTTP_201_CREATED)
def create_or_replace_news(state_name: str, news: NewsItem) -> NewsResponse:
    """
    Create or replace news for a specific state.

    Args:
        state_name: Name of the state (e.g., 'Maharashtra')
        news: News item data with validation

    Returns:
        The created or updated news item.

    Raises:
        HTTPException: 422 if validation fails.
    """
    normalized_state = normalize_state_name(state_name)

    # Create response with normalized state name
    news_response = NewsResponse(
        state=normalized_state,
        title=news.title,
        short_description=news.short_description,
        full_description=news.full_description,
        thumbnail_url=news.thumbnail_url
    )

    news_database[normalized_state] = news_response
    return news_response


@app.delete("/indnews/{state_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_state_news(state_name: str) -> None:
    """
    Delete news for a specific state.

    Args:
        state_name: Name of the state (e.g., 'Maharashtra')

    Raises:
        HTTPException: 404 if state has no news to delete.
    """
    normalized_state = normalize_state_name(state_name)

    if normalized_state not in news_database:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No news found for state: {normalized_state}"
        )

    del news_database[normalized_state]


@app.get("/", tags=["Health"])
def root() -> dict:
    """Root endpoint - API health check."""
    return {"message": "India State News API is running", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
