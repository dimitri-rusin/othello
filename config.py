import datetime

# 1. Generate the timestamp_of_now
now = datetime.datetime.now()
timestamp_of_now = now.strftime("output/%Y%m%d%H%M%S")

# 2. Configuration values from your JSON string
config = {
  "batch_size": 64,
  "epochs": 100,
  "num_epochs_per_checkpoint": 100,
  "num_games_for_supervised_training": 10,
  "number_of_games": 2,
  # "output_path": 'generated_20230814012642_mcts',
  "output_path": '{timestamp_of_now}',
  "random_seed": 42,
}

# 3. Print fish shell commands to set the environment variables
for key, value in config.items():
  # Convert the key to uppercase for the environment variable name
  env_var_name = f"OTHELLO_{key.upper()}"
  if key == 'output_path':
    value = value.replace('{timestamp_of_now}', timestamp_of_now)
  print(f'set -gx {env_var_name} {value}')