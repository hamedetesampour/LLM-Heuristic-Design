import os
import ast
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
        # Initialize the Gemini 3.5 Flash model
        model = genai.GenerativeModel(
            model_name='gemini-3.5-flash', 
            system_instruction="You are a deterministic mathematical parser. You output only raw Python lists."
        )
        
        # Call the API with a low temperature for logical consistency
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
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

