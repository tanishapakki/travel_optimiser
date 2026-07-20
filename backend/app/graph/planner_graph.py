
from pathlib import Path

from langgraph.graph import START,END 

from app.graph.state import PlannerState
from app.models.itinerarydays import ItineraryDays
from app.services.llm_client import generate_structured
from langgraph.graph import StateGraph

from app.schemas.trip import TripInput
from app.schemas.itinerary import Itinerary

PROMPT_PATH =(
    Path(__file__).resolve().parent.parent/"prompts"/"planner_v1.txt"
)

PLANNER_PROMPT=PROMPT_PATH.read_text(encoding="utf-8")


def planner_node(state: PlannerState) -> dict:
    print("Planner node executed")
    trip_input = TripInput.model_validate(state["trip_input"])

    prompt= PLANNER_PROMPT.format(
        start_location=trip_input.start_location,
        destination=trip_input.destination,
        start_date= trip_input.destination,
        end_date=trip_input.end_date,
        travellers=trip_input.travellers,
        days=trip_input.start_date-trip_input.end_date,
    )

    itinerary= generate_structured(prompt=prompt, schema=Itinerary,)
    print("Generated itinerary:", itinerary)

    return{
        "itinerary":itinerary
    }
    
def build_planner_graph():
    graph= StateGraph(PlannerState)
    
    graph.add_node("planner",planner_node)
    
    graph.add_edge(START, "planner")
    graph.add_edge("planner",END)

    return graph.compile()

planner_graph = build_planner_graph()


