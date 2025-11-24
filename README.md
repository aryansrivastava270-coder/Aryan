# Guess The Number Game

## Overview
This project is a simple command-line based **Guess the Number** game implemented in Python.  
The player selects one of three difficulty levels and attempts to guess a randomly generated secret number within the allowed number of attempts (depending on level).

This project demonstrates basic Python programming concepts such as loops, conditional logic, input handling, and modular structuring of game rules.

## Features
- Three difficulty levels:
  - **Easy**: Number between 1–10 (unlimited attempts)
  - **Medium**: Number between 1–50 (7 attempts)
  - **Hard**: Number between 1–100 (5 attempts)
- Secret number is randomly generated.
- Win/loss detection.
- Clean and simple terminal-based user interaction.

## Technologies Used
- **Python 3.x**

## How to Run the Project
1. Install Python 3.x on your system.
2. Download or clone this project folder.
3. Open a terminal in the project directory.
4. Run the file:

```
python guess_the_number.py
```

## Functional Requirements
This project satisfies the following functional requirements:

1. Difficulty selection module  
2. Random number generation module  
3. User guessing and game-loop logic  
4. Input/output interaction  

## Non-Functional Requirements
This project fulfills at least four non-functional requirements:

1. **Usability** – Simple and intuitive text-based UI.  
2. **Reliability** – Handles incorrect guesses and ensures proper game termination.  
3. **Maintainability** – Clean structure; difficulty settings can be easily modified.  
4. **Performance** – Minimal resource usage; runs instantly on any machine.

## Problem Statement
Build an interactive Python-based game where the player must guess a secret number.  
The game should offer multiple difficulty levels and limit attempts based on the level selected.

## System Architecture
A simple linear architecture:
- Input module → Difficulty selection
- Logic module → Random number generation + Game loop
- Output module → Display results to user

## Workflow Diagram
1. Display difficulty options  
2. User selects difficulty  
3. System sets range & attempt limit  
4. System generates secret number  
5. User guesses until:
   - Correct guess → Win  
   - Attempts exhausted → Lose  

## Future Enhancements
- Add GUI using Tkinter or PyQt
- Add a scoring system
- Add multiple rounds mode
- Add sound effects or animations
- Add logging for attempts and performance

# Screenshots

<img width="649" height="385" alt="image" src="https://github.com/user-attachments/assets/06413ca0-df5b-46a1-98e8-400e5973af08" />

<img width="452" height="398" alt="image" src="https://github.com/user-attachments/assets/555de9ca-3f8d-45c2-b4e9-b360b55182d0" />

<img width="533" height="544" alt="image" src="https://github.com/user-attachments/assets/c2840e5e-b666-40c8-bffe-dcfff3a0b7db" />

