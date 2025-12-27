from langgraph.graph import StateGraph, START, END
from content_generation.graph_state.graph_state import GraphState

from content_generation.nodes.product_parser_node import product_parser_node
from content_generation.nodes.question_generator_node import question_generator_node
from content_generation.nodes.faq_page_node import faq_page_node
from content_generation.nodes.product_page_node import product_page_node
from content_generation.nodes.comparison_page_node import comparison_page_node
from content_generation.nodes.output_writer_node import output_writer_node

workflow = StateGraph(GraphState)

workflow.add_node("product_parser", product_parser_node)
workflow.add_node("question_generator", question_generator_node)
workflow.add_node("faq_page", faq_page_node)
workflow.add_node("product_page", product_page_node)
workflow.add_node("comparison_page", comparison_page_node)
workflow.add_node("output_writer", output_writer_node)

workflow.add_edge(START, "product_parser")
workflow.add_edge("product_parser", "question_generator")
workflow.add_edge("question_generator", "faq_page")
workflow.add_edge("faq_page", "product_page")
workflow.add_edge("product_page", "comparison_page")
workflow.add_edge("comparison_page", "output_writer")
workflow.add_edge("output_writer", END)
