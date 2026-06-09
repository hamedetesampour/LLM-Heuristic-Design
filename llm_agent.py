import os
import ast
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the new Google GenAI Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_llm_mutation(route: list[int], distance: float, coordinates: list) -> list[int]:
    """
    Submits the spatial data to the Gemini API to generate a heuristic route mutation.
    """
    prompt = f"""
    You are an expert operations research algorithm solving the Traveling Salesperson Problem.
    The current route sequence is: {route}
    The total Euclidean distance of this route is: {distance:.2f}
    The 2D coordinates of the cities (index 0 to {len(route)-1}) are:
    {coordinates}

    Analyze the coordinates. Apply a logical structural mutation (such as a 2-opt swap 
    or segment reversal) to untangle crossing paths and reduce the total distance.
    
    CRITICAL INSTRUCTION: Output ONLY a valid Python list representing the new sequence of integers. 
    Do not include any explanation, markdown backticks, or text outside the list brackets.
    """

    try:
        # We switch to an older model to use a fresh daily quota bucket
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                system_instruction="You are a deterministic mathematical parser. You output only raw Python lists."
            )
        )

        raw_output = response.text.strip()
        
        # Sanitize output: strip markdown and extract only the list structure
        sanitized_output = re.search(r'\[(.*?)\]', raw_output)
        if not sanitized_output:
            return route
            
        list_string = sanitized_output.group(0)
        new_route = ast.literal_eval(list_string)
        
        # Validation: Verify the LLM returned a mathematically sound permutation
        if isinstance(new_route, list) and set(new_route) == set(route) and len(new_route) == len(route):
            return new_route
        else:
            return route 

    except Exception as e:
        print(f"Gemini Mutation API or Parsing Error: {e}")
        return route # Fallback to original sequence to prevent runtime crash