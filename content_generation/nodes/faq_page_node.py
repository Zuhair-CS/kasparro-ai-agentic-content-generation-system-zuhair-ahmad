from content_generation.graph_state.graph_state import GraphState

def faq_page_node(state: GraphState):
    product = state["product"]
    questions = state["questions"]

    faq_items = []

    for q in questions[:5]:
        if q.category == "Usage":
            answer = product.how_to_use

        elif q.category == "Safety":
            answer = product.side_effects

        elif q.category == "Informational":
            answer = ", ".join(product.ingredients)

        elif q.category == "Purchase":
            answer = product.price

        elif q.category == "Comparison":
            answer = (
                "GlowBoost focuses on brightening with Vitamin C and Hyaluronic Acid, "
                "while other serums may vary in formulation and price."
            )

        else:
            answer = "Information not available."

        faq_items.append({
            "question": q.question,
            "answer": answer
        })

    return {
        "faq_page": {
            "page_type": "faq",
            "items": faq_items
        }
    }
