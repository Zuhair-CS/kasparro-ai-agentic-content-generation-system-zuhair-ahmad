from content_generation.graph_state.graph_state import GraphState

def faq_page_node(state: GraphState):
    product = state["product"]
    questions = state["questions"]

    faq = {
        "page_type": "faq",
        "items": [
            {
                "question": q.question,
                "answer": product.how_to_use if q.category == "Usage" else product.price
            }
            for q in questions[:5]
        ]
    }

    return {"faq_page": faq}
