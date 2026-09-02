from pathlib import Path
from model import State

def reducer(state: State) -> dict:
   title = state["plan"].blog_title
   body ="\n\n".join(state["sections"]).strip()

   final_md = f"# {title}\n\n{body}\n"

   filename = title.lower().replace(" ", "_") + ".md"
   output_path = Path("blogs", filename)
   output_path.write_text(final_md, encoding="utf-8")

   return {"final": final_md}