

from pathlib import Path
from tempfile import template


PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts" 

def load_prompt(prompt_name: str, **variables) -> str:
    """variables is user prompt"""
    prompt_path = PROMPTS_DIR / prompt_name

    print("PROMPTS_DIR:", PROMPTS_DIR)
    print("PROMPT PATH:", prompt_path)


    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_name}")
    
    template = prompt_path.read_text(encoding="utf-8")  

    try: 
        return template.format(**variables)
    
    except KeyError as exc:
        missing_variable = exc.args[0]

        raise ValueError(
            f"Missing prompt variable: {missing_variable}"
        ) from exc

    