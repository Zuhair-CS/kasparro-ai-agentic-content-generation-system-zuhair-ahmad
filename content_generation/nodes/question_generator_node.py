from content_generation.graph_state.graph_state import GraphState

def question_generator_node(state: GraphState):
    product = state["product"]

    questions = [
        {"category": "Informational", "question": f"What is {product.name}?"},
        {"category": "Ingredients", "question": "What ingredients does this product contain?"},
        {"category": "Usage", "question": f"How should {product.name} be used?"},
        {"category": "Application Timing", "question": "When should this serum be applied during the day?"},
        {"category": "Skin Type Suitability", "question": "Which skin types is this product suitable for?"},
        {"category": "Benefits", "question": "What are the main benefits of using this serum?"},
        {"category": "Effectiveness", "question": "How effective is this product for brightening skin?"},
        {"category": "Safety", "question": "Is this product safe to use on sensitive skin?"},
        {"category": "Side Effects", "question": "Are there any side effects associated with this product?"},
        {"category": "Sensitivity", "question": "Will this serum cause irritation for sensitive skin?"},
        {"category": "Frequency of Use", "question": "How often should this serum be used?"},
        {"category": "Layering", "question": "Can this serum be layered with other skincare products?"},
        {"category": "Storage", "question": "How should this product be stored?"},
        {"category": "Pricing", "question": "What is the price of this product?"},
        {"category": "Value for Money", "question": "Is this serum good value for its price?"},
        {"category": "Comparison", "question": "How does this serum compare to other vitamin C serums?"},
        {"category": "Beginners", "question": "Is this product suitable for beginners?"},
        {"category": "Results Timeline", "question": "How long does it take to see results from this serum?"},
        {"category": "Compatibility with Sunscreen", "question": "Can this serum be used with sunscreen?"},
        {"category": "Daily Use", "question": "Can this serum be used daily?"}
    ]

    return {"questions": questions}
