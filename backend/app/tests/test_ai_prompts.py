from unittest.mock import patch

import pytest
from pydantic import BaseModel

from app.core.exception import StructuredOutputError
from app.services.llm_client import generate_structured
from app.schemas.trip import TripPlanSchema




def test_generate_structured_valid_json():
    mock_response = """
    {
        "destination": "Tokyo",
        "days": 5
    }
    """

    with patch(
        "app.services.llm_client.generate",
        return_value=mock_response,
    ) as mock_generate:
        result = generate_structured(
            prompt="Plan a 5 day Tokyo trip",
            schema=TripPlanSchema,
        )

    assert isinstance(result, TripPlanSchema)
    assert result.destination == "Tokyo"
    assert result.days == 5
    assert mock_generate.call_count == 1


def test_generate_structured_strips_markdown_fences():
    mock_response = """
    ```json
    {
        "destination": "Paris",
        "days": 3
    }
    ```
    """

    with patch(
        "app.services.llm_client.generate",
        return_value=mock_response,
    ) as mock_generate:
        result = generate_structured(
            prompt="Plan a 3 day Paris trip",
            schema=TripPlanSchema,
        )

    assert isinstance(result, TripPlanSchema)
    assert result.destination == "Paris"
    assert result.days == 3
    assert mock_generate.call_count == 1


def test_malformed_json_triggers_correction_retry():
    malformed_response = """
    {
        destination: "Paris",
        days: 3
    }
    """

    corrected_response = """
    {
        "destination": "Paris",
        "days": 3
    }
    """

    with patch(
        "app.services.llm_client.generate",
        side_effect=[
            malformed_response,
            corrected_response,
        ],
    ) as mock_generate:
        result = generate_structured(
            prompt="Plan a 3 day Paris trip",
            schema=TripPlanSchema,
        )

    assert isinstance(result, TripPlanSchema)
    assert result.destination == "Paris"
    assert result.days == 3

    assert mock_generate.call_count == 2


def test_schema_validation_error_triggers_correction_retry():
    invalid_schema_response = """
    {
        "destination": "London"
    }
    """

    corrected_response = """
    {
        "destination": "London",
        "days": 4
    }
    """

    with patch(
        "app.services.llm_client.generate",
        side_effect=[
            invalid_schema_response,
            corrected_response,
        ],
    ) as mock_generate:
        result = generate_structured(
            prompt="Plan a 4 day London trip",
            schema=TripPlanSchema,
        )

    assert isinstance(result, TripPlanSchema)
    assert result.destination == "London"
    assert result.days == 4

    assert mock_generate.call_count == 2


def test_still_invalid_after_retry_raises_structured_output_error():
    first_invalid_response = """
    {
        destination: Paris
    }
    """

    second_invalid_response = """
    {
        "destination": "Paris"
    }
    """

    with patch(
        "app.services.llm_client.generate",
        side_effect=[
            first_invalid_response,
            second_invalid_response,
        ],
    ) as mock_generate:
        with pytest.raises(StructuredOutputError) as exc_info:
            generate_structured(
                prompt="Plan a Paris trip",
                schema=TripPlanSchema,
            )

    assert mock_generate.call_count == 2

    assert "Failed to generate structured output" in str(
        exc_info.value
    )