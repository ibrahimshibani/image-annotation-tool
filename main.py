import json
import uvicorn

if __name__ == "__main__":
    with open('configs/server-config.json', 'r') as f:
        config = json.load(f)

    uvicorn.run("server:app", host=config['host'], port=config['port'], reload=False)
