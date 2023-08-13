import requests
import json
from config import stable_diffusion_token

url = "https://stablediffusionapi.com/api/v3/text2img"


async def stable_diffusion_query(prompt: str):
    payload = json.dumps({
        "key": stable_diffusion_token,
        "prompt": prompt,
        "negative_prompt": None,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": None,
        "webhook": None,
        "track_id": None
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resp_json = json.loads(response.text)
    return resp_json
