import json
import os
from content_generation.graph_state.graph_state import GraphState

def output_writer_node(state: GraphState):
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/faq.json", "w") as f:
        json.dump(state["faq_page"], f, indent=2)

    with open("outputs/product_page.json", "w") as f:
        json.dump(state["product_page"], f, indent=2)

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(state["comparison_page"], f, indent=2)

    return {}
