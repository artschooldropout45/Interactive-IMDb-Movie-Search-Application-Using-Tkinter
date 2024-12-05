# IMDb Movie Finder

## Description

IMDb Movie Finder is a Python-based application built using the Tkinter library. It allows users to search for movies and retrieve details such as:

- Title
- Release Year
- Genre
- Director
- Plot

The application uses the OMDb API to fetch movie data based on user input. With its intuitive GUI, users can easily look up information about their favorite movies.

---

## Features

- **Search Functionality**: Enter the name of a movie to fetch its details.
- **Real-Time Data**: Retrieves movie information from the OMDb API.
- **User-Friendly Interface**: Built using Tkinter for simplicity and ease of use.
- **Error Handling**: Displays error messages for invalid or missing input.

---

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `requests` library

---

## How to Use

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install requests
   ```
3. Replace `your_api_key` in the script with your OMDb API key.
4. Run the application:
   ```bash
   python imdbproj.py
   ```
5. Enter a movie name in the input field and click **Search** to view the movie details.

---

## Example

Search for a movie (e.g., "Inception") and get the following details:

- **Title**: Inception
- **Year**: 2010
- **Genre**: Action, Adventure, Sci-Fi
- **Director**: Christopher Nolan
- **Plot**: A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.

---

## API Reference
This project uses the [OMDb API](http://www.omdbapi.com/) to fetch movie data. Sign up to get your API key.

---

