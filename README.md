# SummaDoc

SummaDoc is a cutting-edge document summarization tool designed to process and summarize large documents efficiently. It leverages advanced AI models and robust text processing techniques to deliver concise and accurate summaries.

## Key Features

1. **Document Parsing**: The `Ingestor` class uses `LlamaParse` to extract content from various document formats and convert it into Markdown for further processing.
2. **Text Splitting**: The `Splitter` class employs `RecursiveCharacterTextSplitter` for efficient and customizable text chunking, ensuring optimal input for summarization.
3. **AI-Powered Summarization**: The `Summarizer` class utilizes the `facebook/bart-large-cnn` model to generate summaries, with support for GPU acceleration for faster processing.
4. **Web Interface**: A user-friendly frontend built with Streamlit for seamless interaction.
5. **API Integration**: A FastAPI backend for handling file uploads and summarization requests.

## Installation

### Prerequisites
- Python >= 3.12
- `uv` CLI tool (for dependency management)
- A valid `LLAMA_CLOUD_API_KEY` (set in the `.env` file)

### Steps
1. Install `uv`:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/Dybal-Ilia/SummaDoc.git
   cd SummaDoc
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
4. Set up the `.env` file with your `LLAMA_CLOUD_API_KEY`:
   ```env
   LLAMA_CLOUD_API_KEY=your_api_key_here
   ```

## Usage

### Running the Backend
Start the FastAPI backend server:
```bash
uvicorn src.app.backend.main:app --reload
```

### Running the Frontend
In a separate terminal, launch the Streamlit frontend:
```bash
streamlit run src/app/frontend/ui.py
```

Access the application via the provided Streamlit links.

### Summarizing Documents
1. Upload a document using the **Browse files** button in the frontend.
2. Wait for the summarization process to complete.
3. View and copy the summarized text.

## Component Interaction

SummaDoc is designed with a modular architecture where each component interacts seamlessly to achieve efficient document summarization. Below is a detailed description of how the components work together:

1. **Frontend (Streamlit)**:
   - Provides a user-friendly interface for uploading documents and viewing summaries.
   - Sends the uploaded document to the backend via API calls.

2. **Backend (FastAPI)**:
   - Handles file uploads and routes requests to the appropriate processing components.
   - Coordinates the ingestion, splitting, and summarization processes.

3. **Document Ingestion (Ingestor)**:
   - Receives the uploaded document from the backend.
   - Uses `LlamaParse` to extract content and convert it into Markdown format.
   - Returns the parsed content to the backend for further processing.

4. **Text Splitting (Splitter)**:
   - Takes the parsed content from the `Ingestor`.
   - Splits the content into manageable chunks using `RecursiveCharacterTextSplitter`.
   - Ensures that chunks are optimized for summarization by maintaining context through overlap.

5. **Summarization (Summarizer)**:
   - Processes the text chunks from the `Splitter`.
   - Uses the `facebook/bart-large-cnn` model to generate summaries for each chunk.
   - Combines the individual summaries into a cohesive final summary.

6. **Uploads Directory**:
   - Temporarily stores uploaded files during processing.
   - Ensures files are cleaned up after processing to maintain efficiency and security.

### Workflow

1. **User Interaction**:
   - The user uploads a document via the Streamlit interface.
   - The frontend sends the file to the backend.

2. **Processing Pipeline**:
   - The backend routes the file to the `Ingestor` for content extraction.
   - The extracted content is passed to the `Splitter` for chunking.
   - The chunks are sent to the `Summarizer` for generating summaries.

3. **Result Delivery**:
   - The backend compiles the final summary and sends it back to the frontend.
   - The user views and interacts with the summary on the Streamlit interface.

This modular design ensures that each component can be developed, tested, and maintained independently while working together to deliver a seamless user experience.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve SummaDoc.

