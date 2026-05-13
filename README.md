# Cloudflare-Flask-POC

A small Flask web application intended for testing a local app through a Cloudflare Tunnel.

## What is included

- `app.py` serves a simple HTML page at `/`.
- `/api/hello` returns a JSON response with a message and the client IP address.
- `requirements.txt` pins the Python dependency needed to run the app.
- `.gitignore` excludes local virtual environments, caches, logs, and editor files.

## Requirements

- Python 3.10 or newer
- `cloudflared` if you want to expose the local app through Cloudflare Tunnel

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Flask app:

```bash
python app.py
```

The app will be available at:

```text
http://localhost:5000
```

## API

Call the test endpoint:

```bash
curl http://localhost:5000/api/hello
```

Example response:

```json
{
  "client_ip": "127.0.0.1",
  "message": "Hello, World!"
}
```

## Cloudflare Tunnel

With the Flask app running locally, expose it through Cloudflare Tunnel:

```bash
cloudflared tunnel --url http://localhost:5000
```
