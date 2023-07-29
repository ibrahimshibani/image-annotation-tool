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