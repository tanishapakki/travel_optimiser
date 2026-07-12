import pytest

from app.utils.prompt_loader import load_prompt


def test_load_prompt_substitutes_variables():
    prompt = load_prompt(
        "planner_v1.txt",
        user_prompt="Plan a 3 day Paris trip.",
    )

    assert "Plan a 3 day Paris trip." in prompt
    assert "{user_prompt}" not in prompt


def test_load_prompt_missing_variable_raises_error():
    with pytest.raises(
        ValueError,
        match="Missing prompt variable: user_prompt",
    ):
        load_prompt("planner_v1.txt")


def test_load_prompt_missing_file_raises_error():
    with pytest.raises(
        FileNotFoundError,
        match="Prompt file not found",
    ):
        load_prompt("does_not_exist.txt")