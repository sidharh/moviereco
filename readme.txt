Movie Recommendation System 🎥
================================

This is a **Movie Recommendation System** built using **Streamlit** and **TMDb API**. The application recommends movies based on user-selected input and displays movie posters fetched from the TMDb API.

--------------------------------
Features
--------------------------------
- Recommends movies based on similarity.
- Fetches and displays movie posters using the TMDb API.
- Interactive user interface built with Streamlit.

--------------------------------
Installation
--------------------------------

1. Clone the Repository:
   git clone https://github.com/your-username/movie-recommendation.git
   cd movie-recommendation

2. Install Dependencies:
   Make sure you have Python installed. Then, install the required libraries:
   pip install -r requirements.txt

3. Add Your TMDb API Key:
   Replace the placeholder `your_api_key_here` in the `fetch_poster` function inside `app.py` with your actual TMDb API key:
   api_key = "your_api_key_here"

--------------------------------
Usage
--------------------------------

1. Run the Application:
   Start the Streamlit app by running:
   streamlit run app.py

2. Open in Browser:
   Once the app starts, it will provide a local URL (e.g., http://localhost:8501). Open this URL in your browser to use the app.

--------------------------------
File Structure
--------------------------------
movie-recommendation/
│
├── app.py               # Main application file
├── movies_list.pkl      # Pickle file containing movie data
├── similarity.pkl       # Pickle file containing similarity matrix
├── requirements.txt     # List of dependencies
└── readme.txt           # Project documentation

--------------------------------
Deployment
--------------------------------
You can deploy this app using **Streamlit Community Cloud**, **Heroku**, or any cloud platform. For example, to deploy on Streamlit Community Cloud:
1. Push your project to a GitHub repository.
2. Go to https://share.streamlit.io/.
3. Deploy your app by linking your GitHub repository.

--------------------------------
Dependencies
--------------------------------
- streamlit
- pandas
- requests
- pickle

Install all dependencies using:
pip install -r requirements.txt

--------------------------------
Screenshots
--------------------------------
(Add your screenshot here)

--------------------------------
License
--------------------------------
This project is licensed under the MIT License. See the LICENSE file for details.

--------------------------------
Acknowledgments
--------------------------------
- TMDb API (https://www.themoviedb.org/documentation/api) for movie data and posters.
- Streamlit (https://streamlit.io/) for the interactive UI framework.

--------------------------------
Author
--------------------------------
Developed by Sidharth. Feel free to reach out for any questions or suggestions!