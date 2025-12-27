from content_generation.graph_state.graph_state import GraphState

def product_page_node(state: GraphState):
    product = state["product"]

    page = {
        "page_type": "product",
        "name": product.name,
        "concentration": product.concentration,
        "skin_type": product.skin_type,
        "ingredients": product.ingredients,
        "benefits": product.benefits,
        "how_to_use": product.how_to_use,
        "side_effects": product.side_effects,
        "price": product.price
    }

    return {"product_page": page}
