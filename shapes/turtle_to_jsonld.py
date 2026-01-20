import os
import json
from pathlib import Path
from openai import OpenAI

# 1. Configuration
INPUT_DIR = Path("./turtle")
OUTPUT_DIR = Path("./json-ld")
MODEL = "gpt-4o"  # Use gpt-4o for complex reasoning about RDF nesting

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 2. The Specialized "FAIR² Architect" Prompt
SYSTEM_PROMPT = """
You are a senior RDF and JSON-LD Architect. Your task is to transform Turtle (TTL) into Compact, Nested JSON-LD.
Follow these rules strictly:
1. CONTEXT: Only define prefixes that are explicitly present in the provided Turtle file.
2. NESTING: Properties (sh:property) must be nested as an array of anonymous objects. 
3. NO BLANK NODE IDs: Do not use identifiers like "_:n..." for property shapes or internal nodes.
4. SIMPLIFICATION: Simplify single-value ID objects. e.g., "sh:nodeKind": { "@id": "sh:IRI" } should become "sh:nodeKind": "sh:IRI".
5. ROOT: The output should be a single JSON object with the Main Shape's @id at the top level. Do not use @graph.
6. COMPACTION: Use the shortest possible keys defined in the @context.
7. STRICTNESS: Output ONLY the JSON-LD. No explanation or markdown code blocks.
"""

def transform_file_with_ai(ttl_content):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Transform this Turtle into clean JSON-LD:\n\n{ttl_content}"}
        ],
        response_format={ "type": "json_object" } # Ensures valid JSON output
    )
    return json.loads(response.choices[0].message.content)

def batch_ai_transform():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"🚀 AI Agent starting transformation: {INPUT_DIR} ➔ {OUTPUT_DIR}")

    ttl_files = list(INPUT_DIR.glob("*.ttl"))
    for ttl_path in ttl_files:
        try:
            print(f"  [→] Processing: {ttl_path.name}...")
            
            with open(ttl_path, "r", encoding="utf-8") as f:
                ttl_content = f.read()

            # Call AI Agent
            jsonld_data = transform_file_with_ai(ttl_content)

            # Save Output
            output_path = OUTPUT_DIR / ttl_path.with_suffix(".json").name
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(jsonld_data, f, indent=4)

            print(f"  [✓] Successfully nested: {output_path.name}")

        except Exception as e:
            print(f"  [!] Failed {ttl_path.name}: {e}")

if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        print("❌ Error: Please set the OPENAI_API_KEY environment variable.")
    else:
        batch_ai_transform()