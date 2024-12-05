import tkinter as tk
from tkinter import messagebox
import requests


# OMDB API key (Replace 'your_api_key' with your actual API key)
API_KEY = 'your_api_key'

# Function to search movie
def search_movie():
    movie_name = entry.get()
    if not movie_name:
        messagebox.showwarning("Input Error", "Please enter a movie name")
        return

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey=c925c977"
    response = requests.get(url)
    movie_data = response.json()

    if movie_data['Response'] == 'True':
        title_label.config(text="Title: " + movie_data['Title'])
        year_label.config(text="Year: " + movie_data['Year'])
        genre_label.config(text="Genre: " + movie_data['Genre'])
        director_label.config(text="Director: " + movie_data['Director'])
        plot_label.config(text="Plot: " + movie_data['Plot'])
    else:
        messagebox.showerror("Error", "Movie not found!")

# Setting up the GUI
root = tk.Tk()
root.title("IMDb Movie Finder")

# Creating and placing widgets
tk.Label(root, text="Enter Movie Name:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=search_movie)
search_button.grid(row=0, column=2, padx=10, pady=10)

title_label = tk.Label(root, text="Title: ")
title_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=10)

year_label = tk.Label(root, text="Year: ")
year_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=10)

genre_label = tk.Label(root, text="Genre: ")
genre_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=10)

director_label = tk.Label(root, text="Director: ")
director_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=10)

plot_label = tk.Label(root, text="Plot: ")
plot_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=10)

# Running the application
root.mainloop()