from unittest.mock import MagicMock, patch

from groq import APITimeoutError

from app.services.llm_client import generate


def test_logs_error_and_retry_success(caplog):
    mock_response = MagicMock()

    mock_response.usage.prompt_tokens = 100
    mock_response.usage.completion_tokens = 50
    mock_response.usage.total_tokens = 150

    mock_response.choices[0].message.content = "Hello"

    mock_request = MagicMock()

    timeout_error = APITimeoutError(
        request=mock_request,
    )

    with patch(
        "app.services.llm_client.client.chat.completions.create",
        side_effect=[
            timeout_error,
            mock_response,
        ],
    ):
        with caplog.at_level("INFO"):
            result = generate(
                messages=[
                    {
                        "role": "user",
                        "content": "Hello",
                    }
                ],
                prompt_name="planner_v1",
            )

    assert result == "Hello"

    assert "status=error" in caplog.text
    assert "APITimeoutError" in caplog.text
    assert "status=success" in caplog.text
    assert "tokens_in=100" in caplog.text
    assert "tokens_out=50" in caplog.text
    assert "total_tokens=150" in caplog.text
    assert "latency_ms=" in caplog.text