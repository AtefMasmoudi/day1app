import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from groq import Groq
from dotenv import load_dotenv
import markdown

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    # Retrieve the API key from environment variables
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return HTMLResponse(
            content="<h1>Error: GROQ_API_KEY not found</h1>",
            status_code=500
        )

    client = Groq(api_key=api_key)
    message = (
    """You have arrived at Itech University — home of the legendary Production AI Engineering' course by Atef MASMOUDI! 
		This site is now LIVE in production for the very first time. Generate an electrifying welcome announcement that captures
		the energy of students who go from zero to shipping AI in weeks. 
		Mention RAG, Agents, MCP, and the thrill of deploying to AWS, Azure, and GCP.
		Make visitors feel they are about to start the most important journey of their careers!"""
        )
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    md_reply = response.choices[0].message.content
    html_reply = markdown.markdown(md_reply)
    
    full_html = f"""
    <html>
        <head><title>Itech University - Live!</title></head>
        <body style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">
            {html_reply}
        </body>
    </html>
    """
    return HTMLResponse(content=full_html)

    #reply = response.choices[0].message.content.replace("\n", "<br/>")
    #html = f"<html><head><title>Itech University!</title></head><body><p>{reply}</p></body></html>"
    #return html


