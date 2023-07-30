# Image Annotation Tool

This is a simple web app designed to facilitate image labeling. The labeled images are stored in a MongoDB database for future use and training.

## Project Structure

- The application and server settings such as hostname and port can be configured in the `app_config.py` and `server-config` files located under the `configs` directory.
- An example of an Image in JSON format, which can be stored in MongoDB, can be found in the `example_image.json` file under the `utils` directory.


### Start Server
To start the server, navigate to the project directory and run the following command:
```
python main.py
```

#### Run API tests
To run API tests, navigate to the project directory and execute the following command:
```
python -m pytest
```
NOTE: update app_config.py to reflect where the url pointing to the mongodb instance running so that the tests can work.

#  Run App and database locally


## Building Docker Images

While in root GH dir :

1. Build the image annotation tool Docker image:

   ```
   docker build -t image-annotation-tool -f ./docker/server.dockerfile .
   ```

2. Build the MongoDB Docker image:

   ```
   docker build -t fast-mongo-db -f ./docker/mongoDB.dockerfile .
   ```

## Running Entire Stack with Docker

After the images have been built, you can run the containers. But before that, you need to create a network that allows the containers to communicate with each other.

1. Create a custom Docker network:

   ```
   docker network create image_tool_nw
   ```

2. Run the MongoDB container:

   ```
   docker run -d --network image_tool_nw --name mongo-db-instance -p 27017:27017 fast-mongo-db
   ```

3. Run the image annotation tool container:

   ```
   docker run -d --network image_tool_nw --name annotation-tool-instance -p 8000:8000 image-annotation-tool
   ```

With these steps, both the MongoDB instance and the image annotation tool are running in separate Docker containers and can communicate with each other over the custom network.

4. Test the image by using Curl (linux) :
    ```
    curl -X POST 'http://127.0.0.1:8000/upload/' -H 'Content-Type: application/json' --data-raw '{
    "url": "http://example.com/image.jpg",
    "camera_type": "Canon",
    "location": "Waldkirch Factory",
    "dpi": 500,
    "domain": "Supply Chain Monitoring",
    "label": ["Envelope", "S", "Paper"]
    }
    '
    ```
    or powershell equivelant:
    ```
    $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
    $headers.Add("Content-Type", "application/json")

    $body = "{
    `n    `"url`": `"http://example.com/image.jpg`",
    `n    `"camera_type`": `"Canon`",
    `n    `"location`": `"Waldkirch Factory`",
    `n    `"dpi`": 500,
    `n    `"domain`": `"Supply Chain Monitoring`",
    `n    `"label`": [`"Envelope`", `"S`", `"Paper`"]
    `n}
    `n"

    $response = Invoke-RestMethod 'http://127.0.0.1:8000/upload/' -Method 'POST' -Headers $headers -Body $body
    $response | ConvertTo-Json
    ```