# Golf Trajectory Plotter

This project simulates the trajectory of a golf ball based on user inputs and generates a graph of the ball's height and distance.

## Project Structure

```
golf-trajectory-plotter
├── src
│   ├── simple_simulation2.py  # Golf carry and rollout simulator
│   └── plot_trajectory.py      # Generates the trajectory graph
├── requirements.txt            # Lists project dependencies
├── .gitignore                  # Specifies files to ignore in Git
└── README.md                   # Documentation for the project
```

## Description

### `src/simple_simulation2.py`
This file contains the golf carry and rollout simulator. It takes user inputs for:
- Ball Speed (m/s)
- Launch Angle (degrees)
- Backspin Rate (RPM)

The simulator calculates various outputs including:
- Carry Distance
- Peak Height
- Total Distance

It uses numerical integration to simulate the trajectory of the golf ball.

### `src/plot_trajectory.py`
This file is responsible for generating a graph of the golf ball's trajectory. It imports data from `simple_simulation2.py`, specifically the height and distance values, and uses Matplotlib to create a curve representing the trajectory.

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Run the simulator:
   ```
   python src/simple_simulation2.py
   ```
   Follow the prompts to enter the ball speed, launch angle, and backspin rate.

2. After running the simulator, you can plot the trajectory by executing:
   ```
   python src/plot_trajectory.py
   ```

## License

This project is licensed under the MIT License.