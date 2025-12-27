from content_generation.graph_state.graph_state import GraphState

def faq_page_node(state: GraphState):
    product = state["product"]
    questions = state["questions"]

    faq_items = []

    for q in questions:
        category = q["category"]
        question_text = q["question"]

        if category == "Usage":
            answer = product.how_to_use

        elif category in ["Safety", "Side Effects", "Sensitivity"]:
            answer = product.side_effects

        elif category in ["Ingredients", "Informational"]:
            answer = ", ".join(product.ingredients)

        elif category in ["Pricing", "Value for Money"]:
            answer = product.price

        elif category == "Comparison":
            answer = (
                "GlowBoost focuses on brightening with Vitamin C and Hyaluronic Acid, "
                "while other serums may vary in formulation and price."
            )

        else:
            answer = "Please refer to the product information for details."

        faq_items.append({
            "question": question_text,
            "answer": answer
        })

    return {
        "faq_page": {
            "page_type": "faq",
            "items": faq_items
        }
    }
