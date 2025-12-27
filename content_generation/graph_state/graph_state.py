from typing import TypedDict, NotRequired, List
from schemas.product_schema import ProductSchema
from schemas.question_schema import QuestionSchema

class GraphState(TypedDict):
    raw_product: dict
    product: NotRequired[ProductSchema]
    questions: NotRequired[List[QuestionSchema]]
    faq_page: NotRequired[dict]
    product_page: NotRequired[dict]
    comparison_page: NotRequired[dict]
