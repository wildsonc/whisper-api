# Simple Whisper API

## Description

This project implements an audio transcription API using OpenAI's Whisper model and FastAPI. The API provides endpoints for transcribing audio from a provided URL or an uploaded audio file. It allows for choosing between different sizes of Whisper models and configuring transcription parameters.

## Features

- Transcribe audio from a URL.
- Transcribe audio from an uploaded file.
- Support for multiple Whisper model sizes (tiny, base, small, medium, large).
- Configurable language and other transcription parameters.

## Installation

Before starting, ensure you have Python 3.8+ installed. Follow these steps to install dependencies and run the server locally:

```bash
git clone https://github.com/wildsonc/whisper-api.git
cd whisper-api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 80
```

## Usage

After starting the server, the API will be available at `http://127.0.0.1:80`.

Docs are available at `http://127.0.0.1:80/docs`.

### Endpoints

- POST `/transcribe`: Transcribes audio from a URL.
- POST `/transcribe/file`: Transcribes audio from an uploaded file.

### Body

```json
{
  "url": "http://example.com/audio.mp3",
  "model": "small", # optional, defaults to "small"
  "settings": { # optional
    "language": "pt",
    "initial_prompt": "Some text",
    "temperature": 0.4
  }
}
```

### File Upload

To transcribe audio from an uploaded file, send a POST request to `/transcribe/file`. This endpoint accepts form data with the audio file, model selection, and optional settings.

#### cURL Example

```bash
curl -X POST "http://127.0.0.1:80/transcribe/file" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path_to_your_audio_file.mp3;type=audio/mpeg" \
     -F "model=small" \
     -F "language=pt" \
     -F "initial_prompt=Some text"

```
