# Simple Frontend + FastAPI Project

This project demonstrates a simple interaction between the frontend (HTML + CSS) and a Python backend (FastAPI), while safely handling secret data.

## .env

The `.env` file stores sensitive environment variables (passwords, tokens, keys).  
It **should not be committed** to Git — instead, use `.env.example`.

## Secret Masking

Secrets are sent to the frontend **partially hidden** (e.g., `SecRetBegin****End`) to:  
- **Verify that the secret exists**  
- **Avoid exposing the full secret**  
- **Enhance application security**
