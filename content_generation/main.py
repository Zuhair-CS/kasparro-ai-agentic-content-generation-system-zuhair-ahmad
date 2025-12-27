from content_generation.workflow.workflow import workflow

RAW_PRODUCT = {
    "name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2-3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "₹699"
}

graph = workflow.compile()
result = graph.invoke({"raw_product": RAW_PRODUCT})

print(result["faq_page"])
