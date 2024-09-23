# PicQuery: Interactive Image Questioning App

**PicQuery** is a Streamlit-based application that allows users to upload an image and ask questions about it using Google's Gemini Pro model for AI-powered image analysis. The app provides insightful answers based on the input image and the user's text query.

![Home](screen_shots\one.png)


## Features

- Upload images in `.jpg`, `.jpeg`, or `.png` format.
- Ask questions about the uploaded image using text input.
- Get AI-generated answers using Google Gemini Pro model (version `1.5-flash`).
- Display the uploaded image for visual reference.

## Technologies Used

- **Streamlit**: The web framework used for building the interactive application.
- **Google Generative AI (Gemini Pro Model)**: AI service used to generate responses based on the image and text input.
- **Python-dotenv**: Used for managing environment variables, including the Google API key.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/picquery.git
   cd picquery
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory of the project, and add your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload an image and optionally enter a text prompt to ask a question about the image.

3. Click the "Submit" button to get an AI-generated response related to the image.

## Requirements

- Python 3.8 or above
- Streamlit
- Google Generative AI
- Python-dotenv

The required libraries can be found in the `requirements.txt` file.

## How it Works

- The app allows users to upload an image, which is processed by the Google Gemini AI model.
- Users can ask questions about the uploaded image using the text input box.
- The model returns responses based on the image and/or the user's query.

## Example

![Home](screen_shots\two.png)
![Home](screen_shots\three.png)

- **Upload an Image**: Upload an image file, such as a picture of a landscape, animal, or object.
- **Ask a Question**: For example, "What is this animal?" or "Describe the environment."
- **Get a Response**: The AI will analyze the image and provide a text-based response, offering details or answering questions about the content.

## Project Structure

- **app.py**: The main application script that defines the Streamlit app interface.
- **requirements.txt**: Contains the list of dependencies to install.
- **.env**: File (not included in the repository) where the API key for Google Generative AI is stored.

## License

This project is open-source and available under the [MIT License](LICENSE).
