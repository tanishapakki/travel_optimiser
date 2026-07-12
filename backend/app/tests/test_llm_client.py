from app.services.llm_client import generate


result = generate(
    messages="describe the spinosaurus",
    max_tokens=100,
    system="Answer in 2 short sentences",
)

print(result)

# from unittest.mock import MagicMock, patch

# import pytest
# from groq import APIConnectionError

# from app.services.llm_client import generate


# def test_generate_retries_on_network_error():
#     mock_request = MagicMock()

#     error = APIConnectionError(
#         request=mock_request
#     )

#     with patch(
#         "app.services.llm_client.client.chat.completions.create",
#         side_effect=error,
#     ) as mock_create:

#         with pytest.raises(APIConnectionError):
#             generate("Say hi")

#         assert mock_create.call_count == 3