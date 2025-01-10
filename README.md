# Project overview
This project is a chatbot for Promtior developed to interact with users and answer questions related to the company’s services by utilizing rich context from a variety of sources, such as PDF documents and webpages. It uses natural language processing technology, based on OpenAI, to generate intelligent responses. Contextualized replies and conversational logic are handled using the LangChain framework. The chatbot has been deployed on the Railway platform, and with its simple web interface, it will respond to inquiries about what services Promtior offers, when the company was founded, and more.

## Strategy
The methodology behind this project involves several key steps. First, data is gathered from two primary sources: the Promtior website (www.promtior.ai) and the PDF document from the Technical Test (AI Engineer). These data sets are combined into a unified vector store, enabling efficient querying. When a user submits a question, the system processes the inquiry by extracting relevant context from these data sources and retrieves the most appropriate response using a GPT-4 model. This is facilitated through a connection to the OpenAI API, which generates accurate answers based on the available information. Finally, the application is deployed on the Railway platform for seamless operation.

## Main challenges encountered
One of the main challenges encountered was retrieving and integrating information from both the Promtior website and the PDF document. The solution involved combining these data sources into a unified vector store to streamline the retrieval process.

A second challenge arose during deployment when I needed to remove the OpenAI API key from the code to ensure the application could be deployed correctly. This was addressed by configuring environment variables to securely store the API key, allowing for proper deployment on the Railway platform.


# Implementation Overview
## Core Functionality
The chatbot leverages GPT-4 from OpenAI to process user queries and provide context-based answers. The application integrates data from two main sources: the Promtior website and a PDF document containing relevant information. This data is combined and stored in a vector store using FAISS, which ensures fast and accurate retrieval during query processing.

## Data Integration
To handle the data, LangChain was used to facilitate the retrieval of contextual information. Information from the PDF is extracted using PyMuPDF, while web data is loaded via WebBaseLoader. The combined data is processed by the GPT-4 model to generate accurate responses, all managed through FastAPI.

## Frontend & User interaction
The frontend is a simple HTML interface built with HTML and JavaScript. It allows users to input their queries and view chatbot responses. When the user types their query into the input field and presses the “Submit” button, JavaScript handles the event by sending the query to the backend using a GET request through the fetch API. The backend processes the query, generates a response using the GPT-4 model, and sends the result back to the frontend. The response is displayed below the user’s query in the chatbox, maintaining a smooth conversational flow.

JavaScript is responsible for handling user interactions, including managing the button click event and making the API request. The HTML structure provides the input field for user queries and a section where both user inputs and chatbot responses are displayed. CSS is used for styling the chat interface, ensuring an intuitive and user-friendly design. The backend, powered by FastAPI, ensures that the chatbot's logic and responses are processed efficiently and correctly.


## Key Technologies
- *LangChain:* facilitates conversation management and data retrieval for query processing.
- *FastAPI:* provides the backend framework to expose the chatbot API.
- *FAISS:* used for efficient data storage and retrieval from the combined sources (PDF and website).
- *OpenAI GPT-4:* powers the chatbot's ability to generate contextual and intelligent responses.
- *PyMuPDF:* extracts text from the Promtior PDF for use in chatbot responses.
- *Railway:* deployed the application to the cloud, ensuring smooth operation.
- *HTML & JavaScript:* used to build the chatbot’s simple frontend interface.

## Key Files
- *app.py:* the core file of the application. It exposes the main routes for the chatbot, including / for the welcome page and /chat for processing user queries. It integrates data from the website and the PDF document, stores it in FAISS, and uses GPT-4 to generate responses based on user input.
- *Procfile:* essential for deployment on the Railway platform. It specifies the command to run the application with uvicorn, ensuring the application is executed correctly in a production environment.
- *index.html:* the frontend file that allows users to interact with the chatbot. Built with HTML, CSS, and JavaScript, it provides the interface for users to input queries and receive real-time responses from the chatbot.
- *requirements.txt:* lists the necessary dependencies for the project, such as LangChain, OpenAI, FastAPI, FAISS, PyMuPDF, and others, to ensure the proper setup of the environment.

## Deployment
The application is deployed on the Railway platform for easy management and scalability. The deployment process involves the use of a Procfile, which ensures proper execution of the application via uvicorn.
GitHub tntegration: the project's GitHub repository was directly connected to Railway, allowing Railway to detect and build the project automatically. The Procfile played an essential role, specifying the command to run the application with uvicorn, which serves the FastAPI app.
Environment configuration: the necessary environment variable, OPENAI_API_KEY, was securely configured within Railway’s environment settings. This ensured that the application could access OpenAI’s API securely, without exposing sensitive information in the code.
Deployment and testing: Railway automatically deployed the application to the cloud and provided a public URL for testing the chatbot’s functionality. The URL to access the live chatbot is: https://chatbot-promtior-production.up.railway.app/ . This URL was used to verify that the chatbot was responding correctly to user queries in the live environment.

## Running the Project Locally
Clone the GitHub repository, using the following command: 
git clone https://github.com/tatipozna/chatbot-promtior.git
Install dependencies, using pip and the requirements.txt file:
pip install -r requirements.txt
Run the application, using the following command with uvicorn:
uvicorn app:app --reload
Access the application: it will run at http://127.0.0.1:8000, where the chatbot can be tested locally.

## Possible Future Improvements
The user interface could be enhanced to make it more interactive and visually appealing, with features such as message bubbles or additional customization options for a more modern design. Additionally, the efficiency of retrieving responses could be optimized by improving the extraction process from the PDF and the website, which would lead to faster and more accurate answers. Finally, expanding the database with more detailed information about Promtior's services would enhance the chatbot's ability to generate more precise and comprehensive responses.
