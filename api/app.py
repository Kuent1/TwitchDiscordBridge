from fastapi import FastAPI, Form, HTTPException, Request
import subprocess
from fastapi.middleware.cors import CORSMiddleware
import httpx
import markdown2
import docker

app = FastAPI()
client = docker.from_env()

# CORS middleware to allow cross-origin requests


@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Route to submit tokens and generate .env file


@app.post("/submitTokens")
async def generate_env(twitchToken: str = Form(...), discordToken: str = Form(...)):
    # Create .env file content
    env_content = f"TWITCH={twitchToken}\nDISCORD={discordToken}"

    # Write content to .env file
    try:
        with open(".env", "w") as env_file:
            env_file.write(env_content)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to write .env file")

    return {"message": "Successfully generated .env file"}

# Route to fetch Markdown documentation from Github repo


@app.get("/markdown")
async def get_markdown():
    try:
        url = f"https://raw.githubusercontent.com/ollprogram/TwitchDiscordBridge/newgendev/README.md"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            markdown_content = response.text
            html_content = markdown2.markdown(markdown_content)
            return html_content
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching Markdown content: {e}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {e}")

# Routes to start and stop the app container


# Docker Compose file path
DOCKER_COMPOSE_FILE = 'docker-compose.yml'


@app.post('/start')
async def start_containers():
    try:
        # Start containers using docker-compose up
        subprocess.run(
            ["docker-compose", "-f", DOCKER_COMPOSE_FILE, "up", "-d"], check=True)
        return {'message': 'Containers started successfully'}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/stop')
async def stop_containers():
    try:
        # Stop containers using docker-compose down
        subprocess.run(
            ["docker-compose", "-f", DOCKER_COMPOSE_FILE, "down"], check=True)
        return {'message': 'Containers stopped successfully'}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
