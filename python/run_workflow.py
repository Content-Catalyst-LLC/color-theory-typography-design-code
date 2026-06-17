from map_tools.workflows import build_article_outputs, build_canvas_cards
summary = build_article_outputs()
build_canvas_cards()
print("Meaning article-map workflow complete.")
print(f"Articles: {summary['article_count']}")
print(f"Sections: {summary['section_count']}")
