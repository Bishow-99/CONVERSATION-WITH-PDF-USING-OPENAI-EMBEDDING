# PDF-SEARCH-WITH-OPENAI-EMBEDDING
This repository is designed to facilitate the extraction of information from multiple PDF documents using OpenAI and Langchain. The implemented functionality allows users to query these PDF files seamlessly. Additionally, the retrieved data is presented in a user-friendly interface created with Streamlit, enhancing the overall user experience.



# Installation Process

Certainly! Below are the steps explained in a more organized and concise manner:

<b> 1. Generate OpenAI API Key:</b>
   * Obtain an OpenAI API key to access the OpenAI embedding service. You can sign up on the OpenAI platform to obtain your API key.

<b> 2. Create .env File:</b>
   * In your project directory, create a file named `.env`.
   * Inside the `.env` file, add the following line:
     OPENAI_API_KEY="your_api_key"
     Note: Replace "your_api_key" with the actual API key you obtained from OpenAI.

<b>3.Run the Repository:</b>
  * If you are using Docker or running the repository without Docker, the `.env` file ensures that your OpenAI API key is securely stored.
  * Ensure that your environment is set up properly.

<b>4. Install Requirements:</b>
  * Execute the following command to install the required dependencies listed in `requirements.txt`:
    
     pip install -r requirements.txt


<b> 5. Run Streamlit Server:</b>
   *  Start the Streamlit server by running the following command:
     streamlit run main.py

<b> 6. Use Streamlit App:</b>
  *   Click on the Streamlit URL provided in the console after running the previous command.
  *  The Streamlit app interface will open in your web browser.

<b> 7. Query PDFs:</b>
  * Use the app interface to interact with PDFs and write queries.
  * The application utilizes OpenAI embedding to fetch answers from multiple PDFs based on the queries you provide.



# How it works?

![image(6597)](https://github.com/Bishow-99/PDF-SEARCH-WITH-OPENAI-EMBEDDING/assets/80660041/399c37c8-7719-4314-b3ca-fec1c0632713)


1. **Text Extraction from PDF:**
   *  Begin by extracting text from PDF documents.
   *  Divide the extracted text into smaller, manageable chunks to facilitate processing.

2. **Text Encoding and Embedding:**
   *   Encode each chunk of text to create embeddings that capture semantic meaning and contextual information.
   *   Utilize an algorithm that transforms the text into vector representations or lists of numbers, effectively preserving the essence of the content.

3. **Chatting with PDF:**
   *  When interacting with the PDF, break down user queries into similar chunks.
   *  Apply the same encoding algorithm to convert each query chunk into vector representations, maintaining consistency with the encoding used for the PDF text.

4. **Semantic Matching and Ranking:**
   *  Engage in a conversational process where the encoded user query chunks are compared with the encoded PDF text chunks.
   *  Based on semantic matching, generate a ranked list of responses or relevant information from the PDF, providing the user with contextually appropriate answers.
