<h1>Tic Tac Toe Game Project Guide</h1>

## Overview

This project implements a simple Tic Tac Toe game in Python using object-oriented programming concepts. Players take turns marking spaces on a 3x3 grid with their respective symbols (X or 0) until one player wins or the game ends in a draw.

## How It Works

### Game Flow

1. Two players are initialised with their respective symbols ('X' and '0') and prompted to enter their names.
2. A 3x3 board is displayed where players can make their moves.
3. Players take turns entering positions (1-9) to mark spaces on the board.
4. The game checks for a winner after each move and ends if a player achieves a winning pattern.
5. If no winner is found, the game ends in a draw if all spaces on the board are filled.

### Logic

- The board is represented as a list with 9 elements, initially filled with empty spaces (' ').
- Players' moves are validated to ensure they are within the range and the chosen space is not already occupied.
- Winning patterns are checked after each move to determine if a player has won the game.
- If all spaces are filled and no winner is found, the game ends in a draw.

## Exception Handling

- **ValueError**: Handles invalid input when players enter non-numeric values or positions outside the range (1-9).
- **IndexError**: Ensures that the position entered by the player is within the valid range for accessing the board.
- **OccupiedPositionError**: Custom exception to handle cases where players try to mark already occupied spaces.

## Visual Representation

```mermaid
graph TD;
  A[Start Game] --> B{Player 1's Turn?};
  B -->|Yes| C[Player 1 makes a move];
  B -->|No| D[Check for Winner or Draw];
  C --> E[Print Updated Board];
  E --> F[Check for Winner];
  F -->|Yes| G[Declare Player 1 as Winner];
  F -->|No| H{Board Full?};
  H -->|Yes| I[Declare Draw];
  H -->|No| B;
  D -->|Winner| J[Declare Winner];
  D -->|Draw| I;

style A fill:#66c2a5,stroke:#333,stroke-width:2px;
style B fill:#fc8d62,stroke:#333,stroke-width:2px;
style C fill:#8da0cb,stroke:#333,stroke-width:2px;
style D fill:#e78ac3,stroke:#333,stroke-width:2px;
style E fill:#a6d854,stroke:#333,stroke-width:2px;
style F fill:#ffd92f,stroke:#333,stroke-width:2px;
style G fill:#e5c494,stroke:#333,stroke-width:2px;
style H fill:#b3b3b3,stroke:#333,stroke-width:2px;
style I fill:#ff0000,stroke:#333,stroke-width:2px;
style J fill:#66c2a5,stroke:#333,stroke-width:2px;
```

## Repository Structure

- `tic_tac_toe.py`: Contains the Python code for the Tic Tac Toe game.
- `README.md`: Markdown file providing an overview of the project, instructions, and usage guide.

## Usage

1. Clone the repository to your local machine.
2. Run `python tic_tac_toe.py` in your terminal to start the game.
3. Follow the prompts to enter player names and make moves.

<h2 align="left">I code with</h2>
<img alt="svgImg" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIHZpZXdCb3g9IjAgMCA0OCA0OCI+CjxwYXRoIGZpbGw9IiMwMjc3QkQiIGQ9Ik0yNC4wNDcsNWMtMS41NTUsMC4wMDUtMi42MzMsMC4xNDItMy45MzYsMC4zNjdjLTMuODQ4LDAuNjctNC41NDksMi4wNzctNC41NDksNC42N1YxNGg5djJIMTUuMjJoLTQuMzVjLTIuNjM2LDAtNC45NDMsMS4yNDItNS42NzQsNC4yMTljLTAuODI2LDMuNDE3LTAuODYzLDUuNTU3LDAsOS4xMjVDNS44NTEsMzIuMDA1LDcuMjk0LDM0LDkuOTMxLDM0aDMuNjMydi01LjEwNGMwLTIuOTY2LDIuNjg2LTUuODk2LDUuNzY0LTUuODk2aDcuMjM2YzIuNTIzLDAsNS0xLjg2Miw1LTQuMzc3di04LjU4NmMwLTIuNDM5LTEuNzU5LTQuMjYzLTQuMjE4LTQuNjcyQzI3LjQwNiw1LjM1OSwyNS41ODksNC45OTQsMjQuMDQ3LDV6IE0xOS4wNjMsOWMwLjgyMSwwLDEuNSwwLjY3NywxLjUsMS41MDJjMCwwLjgzMy0wLjY3OSwxLjQ5OC0xLjUsMS40OThjLTAuODM3LDAtMS41LTAuNjY0LTEuNS0xLjQ5OEMxNy41NjMsOS42OCwxOC4yMjYsOSwxOS4wNjMsOXoiPjwvcGF0aD48cGF0aCBmaWxsPSIjRkZDMTA3IiBkPSJNMjMuMDc4LDQzYzEuNTU1LTAuMDA1LDIuNjMzLTAuMTQyLDMuOTM2LTAuMzY3YzMuODQ4LTAuNjcsNC41NDktMi4wNzcsNC41NDktNC42N1YzNGgtOXYtMmg5LjM0M2g0LjM1YzIuNjM2LDAsNC45NDMtMS4yNDIsNS42NzQtNC4yMTljMC44MjYtMy40MTcsMC44NjMtNS41NTcsMC05LjEyNUM0MS4yNzQsMTUuOTk1LDM5LjgzMSwxNCwzNy4xOTQsMTRoLTMuNjMydjUuMTA0YzAsMi45NjYtMi42ODYsNS44OTYtNS43NjQsNS44OTZoLTcuMjM2Yy0yLjUyMywwLTUsMS44NjItNSw0LjM3N3Y4LjU4NmMwLDIuNDM5LDEuNzU5LDQuMjYzLDQuMjE4LDQuNjcyQzE5LjcxOSw0Mi42NDEsMjEuNTM2LDQzLjAwNiwyMy4wNzgsNDN6IE0yOC4wNjMsMzljLTAuODIxLDAtMS41LTAuNjc3LTEuNS0xLjUwMmMwLTAuODMzLDAuNjc5LTEuNDk4LDEuNS0xLjQ5OGMwLjgzNywwLDEuNSwwLjY2NCwxLjUsMS40OThDMjkuNTYzLDM4LjMyLDI4Ljg5OSwzOSwyOC4wNjMsMzl6Ij48L3BhdGg+Cjwvc3ZnPg=="/>
