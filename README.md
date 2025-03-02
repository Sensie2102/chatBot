# ChatBot

This project is a **conversational ChatBot** application built using **Python**, leveraging the power of **Langchain** for managing conversation logic, **MongoDB** for data persistence, and **Streamlit** for the user interface.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or above
- MongoDB (running locally or via a cloud provider like MongoDB Atlas)
- Recommended: Create a virtual environment to manage dependencies

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```
   git clone https://github.com/Sensie2102/chatBot.git
   ```
2. Navigate to the project directory:
   ```
   cd chatBot
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Configure MongoDB connection:

   - Ensure your MongoDB instance is running.
   - Update the connection string in the script (if not already set).

6. Start the chatbot interface using Streamlit:
   ```
   streamlit run app.py
   ```
7. Open your browser to the Streamlit interface:
   ```
   http://localhost:8501
   ```

## Project Structure

chatBot/ ├── app.py # Streamlit UI logic ├── chatbot_logic.py # Core chatbot functions using Langchain ├── database.py # MongoDB connection and query functions ├── requirements.txt # Required Python libraries ├── .gitignore # Files to exclude from git └── README.md # Project documentation (this file)

## Key Libraries Used

- **Langchain**: To manage conversation flows and logic
- **Streamlit**: To provide a user-friendly web interface for interacting with the chatbot
- **MongoDB**: To store conversation history and other relevant data

## Available Scripts

- `streamlit run app.py`: Starts the chatbot interface

## Features

- Conversational AI with Langchain
- Real-time user interaction using Streamlit
- Data storage and retrieval using MongoDB
- Easy to extend for more advanced features (e.g., sentiment analysis, user authentication)

## Future Enhancements

- Add support for multi-session chat history
- Enhance conversation logic with more complex Langchain chains
- Add user-specific profiles stored in MongoDB

## Contact

For questions, suggestions, or feedback, please reach out at:

- GitHub: [Sensie2102](https://github.com/Sensie2102)
