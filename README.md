# Chatbot application

## Preface

Build a chatbot application which takes a file as an input and answers user's query. The goal of this application is to accurately provide answers based on the uploaded file. This application could be used as an assistant to quickly answer questions or summarize facts from files containing large amounts of text data, making our lives easier.

## Project structure

In this project, there are 2 directories

1. `backend` containing the server side **python** code
2. `frontend` containing the client side **typescript** code.\

### Backend

**Requirements**: Python 3.10 or above.

1. `main.py` which is the entry point to server
2. This project has a few Python packages as dependencies, you can install them in your virtual environment using `requirements.txt`. If you were to use other dependencies, then please add them to `requirements.txt`.
3. Use [`conda`](https://docs.conda.io/projects/conda/en/stable/) package manager to create a virtual environment `chatbot` using `conda create -n chatbot python=3.10` and then `conda activate chatbot` to activate the environment.
4. Then install the python packages using `pip install -r requirements.txt`

#### Running the backend server

To launch the server, navigate to the `backend` directory and run:

##### `uvicorn main:app --reload`

This will start the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Frontend

The project structure within the `frontend` directory follows the official `create-react-app` structure as in the [docs](https://create-react-app.dev/docs/folder-structure). 

**Requirements**: Use `node V20.11.1` and `npm 10.2.4`. 

#### How to launch the react app

1. Navigate to the `frontend` directory and run `npm install`
2. Then, run:

   ##### `npm start`

   This will launch the app in development mode.\
   Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


### Backend

1. The end goal is to have a meaningful result based on the user query and uploaded file.
2. Implement the storage and handling of the incoming files from the frontend. Use any database management system like MongoDB or MySQL for this.

### Frontend

1. Add a pop up which notifies that the file has been uploaded properly.
2. Extend the app's functionality to accept `.txt`,`.docx` & `.pdf` files in addition to `.csv` files.

