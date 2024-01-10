import tempfile
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

import whisper
from app.schemas import Model, Payload

app = FastAPI()


@app.post("/transcribe")
async def transcribe(data: Payload):
    model = whisper.load_model(data.model)
    result = model.transcribe(data.url, **data.settings.model_dump())
    result["text"] = result["text"].strip()
    return result


@app.post("/transcribe/file")
async def transcribe_file(
    file: Annotated[UploadFile, File()],
    model: Annotated[Model | None, Form()] = Model.small,
    language: Annotated[str | None, Form()] = "pt",
    initial_prompt: Annotated[str | None, Form()] = None,
):
    model = whisper.load_model(model)

    with tempfile.NamedTemporaryFile(
        delete=True, mode="wb", suffix=".mp3"
    ) as temp_file:
        audio_data = await file.read()
        temp_file.write(audio_data)
        temp_file.seek(0)
        result = model.transcribe(
            temp_file.name, language=language, initial_prompt=initial_prompt
        )
        result["text"] = result["text"].strip()
        return result
