<h1>SOLVING CHROME DINOSAUR WITH SUPERVISED LEARNING</h1>

## Introduction

This project is the sixth in a series of projects in which simple games will be developed using the pygame library, and these games will be conquered using machine learning algorithms and artificial intelligence in general.

The motivation behind this approach lies in frequent situations where certain evaluation metrics, when applied to specific algorithms, prove to be inaccurate and obscure their true practical significance. In extreme cases, algorithms with poor performance may be inaccurately assessed positively by specific metrics that, in practice, do not reflect their true effectiveness and distort their evaluation.

When developing algorithms to win games, we have two main evaluation metrics that are simple and have empirical significance:

1. Whether the algorithm won or not.
2. If it won, how efficient its performance was.

## Implementing the Game

The game was implemented using the pygame library for the interface and uses artwork that faithfully replicates the original game. The application consists of two screens:

<p align="center"> 
    <img src="./examples/home_screen.png" width="550" height="400">
</p>
  
The home screen features a dinosaur animated by an invincible machine learning model, providing a demonstration of how to play the game. A prompt instructs the user to press a key to start a game, which resumes from the current position of the dinosaur and obstacles. If the user has played before, the last score is displayed.

<p align="center"> 
    <img src="./examples/game_screen.png" width="550" height="400">
</p>

At the beginning of the game, obstacles like cacti and birds appear, prompting the player to move to avoid collisions. The user can make two moves: jumping or crouching. Colliding with an obstacle returns the user to the home screen, where they can view their final score and start a new game.

## Intelligent Agent Strategies

To address this problem, the supervised learning approach was used, more specifically, the techniques of decision tree and support vector machine. Data was collected and refined using the following steps:

1. Initially, data was collected when the dinosaur successfully navigated an obstacle
2. This data was used to train less robust initial models
3. The created models were set to play, and the data were collected
4. The new data was used to train more robust models

> **Note 1**: The initial and final data are located in `dino_game\data\dino.csv` and `dino_game\data\new_dino.csv`, respectively.

> **Note 2**: This approach was necessary to address erratic and inconsistent gameplay behavior exhibited by a human player.

The initial data, generated from games played by a human player, allowed for the training of models that produced decision boundaries incorporating the noise from human behavior during gameplay, as follows:

<p align="center">
    <img src="./examples/decision_boundary_decision_tree_data_player.png" width="350" height="300">
    <img src="./examples/decision_boundary_svm_linear_data_player.png"    width="350" height="300">
</p>

The final data reveal certain patterns and are displayed below:

<p align="center"> 
    <img src="./examples/data.png" width="500" height="400">
</p>

Analysis of the data shows that:

- A significant horizontal distance results in the agent continuing to run
- Approach to obstacle type 0 (bird) prompts crouching
- Approach to obstacle type 1 (cactus) prompts jumping

> **Note 1**: Since the data is limited to screen coordinates and booleans, it is presented in a well-defined format, with the x-axis being mirrored to accurately represent the game.

> **Note 2**: As testing was conducted in the game environment itself, the data was not split into training and testing sets.

Initially, when training a decision tree, it is important to consider that it segments the data at each node, and these segments are parallel to the variable axes:

<p align="center"> 
    <img src="./examples/decision_boundary_decision_tree.png" width="350" height="300">
    <img src="./examples/decision_tree.png"                   width="350" height="300">
</p>

Interpreting the decision tree results, it is evident that:

- Initially, the minimum horizontal distance is checked, and the dinosaur continues running if not met
- Once the minimum distance is met, the obstacle type is checked to determine the necessary movement

Training the SVM with a linear kernel yielded similar results to the decision tree, with hyperplanes adjusted in a manner parallel to the axes:

<p align="center"> 
    <img src="./examples/decision_boundary_svm.png"                 width="350" height="300">
    <img src="./examples/decision_boundary_svm_support_vectors.png" width="350" height="300">
</p>

> **Note**: It's noteworthy that only points reflecting jumping and crouching movements were used as support vectors for decision boundary adjustment.

In the end, two invincible models were obtained, and the game's home screen allows users to inspect these models before starting a game (agents are randomly selected when the game runs).

## Dino Chrome Pack Organization
```
dino_game/                    Top-level package
      __init__.py
      tools.py
      constants.py
      base.py
      cloud.py
      enemies.py
      dinosaur.py
      obstacles.py
      chrome_dino.py          It brings together the functionalities of the modules to implement the game
      media/                  Folder with the files used in the game's interface
              ...
      models/                 File with the trained ML models
              dtc.pkl
              svm_linear.pkl
      data/
              dino.csv        Data collected from game matches by a human player
              new_dino.csv    Data collected in game matches by early ML models
```
## Running the Game

Using Windows OS and make sure you have [Python 3](https://www.python.org/) installed.

Clone the project:

```bash
  git clone https://github.com/filipemedeiross/solving_chrome_dinosaur.git
```

Access the project directory:

```bash
  cd solving_chrome_dinosaur
```

Creating a virtual environment (for the example we use the location directory parameter as `.venv`):

```bash
  python -m venv .venv
```

Activating the virtual environment:

```bash
  .venv\Scripts\activate
```

Install all required packages specified in requirements.txt:

```bash
  pip install -r requirements.txt
```

Use the following command to run the game:

```bash
  python main.py
```

## References

Yaser S. Abu-Mostafa, Malik Magdon-Ismail, and Hsuan-Tien Lin. **Learning from Data**. AMLBook, 2012.

Numpy: <https://numpy.org/doc/stable/>

Sklearn: <https://scikit-learn.org/stable/modules/classes.html>

Pygame: <https://www.pygame.org/docs/>

Images and sounds used: <https://opengameart.org/>
