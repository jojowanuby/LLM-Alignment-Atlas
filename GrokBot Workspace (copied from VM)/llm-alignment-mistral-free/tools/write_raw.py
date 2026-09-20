
from pathlib import Path
ROOT = Path("/workspace/llm-alignment-mistral-free")
CATS = {}
for line in (ROOT/"01_QUESTION_CATALOG.tsv").read_text().splitlines()[1:]:
    p = line.split("\t")
    if len(p) >= 3:
        CATS[p[0]] = (p[1], p[2])

def write_raw(qid, response, web=False, refusal=False, model="Modellversion nicht eindeutig ausgewiesen (Fast)", blocker=None):
    cat, q = CATS[qid]
    lines = [
        "TEST_ID: ALIGN-MISTRAL-FREE-2026-09-07",
        f"QUESTION_ID: {qid}",
        f"CATEGORY: {cat}",
        f"QUESTION: {q}",
        f"WEB_SEARCH_USED: {str(web).upper()}",
        f"REFUSAL: {str(refusal).upper()}",
        f"TARGET_MODEL_VISIBLE: {model}",
        "PHASE: logged-in-free",
        "RAW_RESPONSE:",
        response.rstrip(),
    ]
    if blocker:
        lines.append(f"BLOCKER: {blocker}")
    path = ROOT/"raw"/f"{qid}.md"
    path.write_text("\n".join(lines) + "\n")
    return path
