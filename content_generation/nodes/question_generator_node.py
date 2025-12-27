from schemas.question_schema import QuestionSchema
from content_generation.graph_state.graph_state import GraphState

def question_generator_node(state: GraphState):
    product = state["product"]

    questions = [
        QuestionSchema(category="Usage", question=f"How should {product.name} be used?"),
        QuestionSchema(category="Safety", question="Are there any side effects?"),
        QuestionSchema(category="Purchase", question="What is the price of this product?"),
        QuestionSchema(category="Informational", question="What are the key ingredients?"),
        QuestionSchema(category="Comparison", question="How does this compare to other serums?")
    ]

    return {"questions": questions}
