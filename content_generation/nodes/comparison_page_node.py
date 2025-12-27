from content_generation.graph_state.graph_state import GraphState

def comparison_page_node(state: GraphState):
    product = state["product"]

    fictional_product_b = {
        "name": "RadiantX Vitamin Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Brightening"],
        "price": "₹799"
    }

    comparison = {
        "page_type": "comparison",
        "product_a": {
            "name": product.name,
            "ingredients": product.ingredients,
            "benefits": product.benefits,
            "price": product.price
        },
        "product_b": fictional_product_b
    }

    return {"comparison_page": comparison}
