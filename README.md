
# Movie Recommendation System

## Overview
This Movie Recommendation System is a terminal-based project and my first venture into programming. The project is developed using Python, and it recommends movies based on user interactions. The recommendation logic works by adding points to different genres based on the user's searches or watched movies, and then suggesting movies from the highest-scoring genre. The database used for storing movies and user data is MySQL.

## Features
- **Search-Based Recommendations**: The system tracks what users search for and increases the relevance of certain genres.
- **Watch-Based Recommendations**: By tracking watched movies, the system refines its recommendations to match the user's taste.
- **Genre-Based Suggestion**: Movies are suggested based on the user's preferred genres.

## Technology Stack
- **Programming Language**: Python
- **Database**: MySQL

## Setup and Installation
To set up the Movie Recommendation System on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation.git
   ```

2. **Install Python dependencies**:
   Make sure you have Python installed and then install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Create a MySQL database and import the provided SQL script to set up the necessary tables.
   - Update the database connection settings in the Python script.

4. **Run the application**:
   ```bash
   python movie_recommendation.py
   ```

## Usage
- **Search for Movies**: Users can search for movies by name or genre.
- **Watch Movies**: The system tracks watched movies and adjusts genre scores.
- **Get Recommendations**: Based on the user's interactions, the system suggests movies from the top genres.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request to improve the recommendation logic or add new features.

## License
This project is licensed under the MIT License.

## Contact
For any questions or inquiries, please reach out to [jdeeran2004@gmail.com](mailto:jdeeran2004@gmail.com).
