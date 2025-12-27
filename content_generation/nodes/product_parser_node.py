from schemas.product_schema import ProductSchema
from content_generation.graph_state.graph_state import GraphState

def product_parser_node(state: GraphState):
    product = ProductSchema(**state["raw_product"])
    return {"product": product}
