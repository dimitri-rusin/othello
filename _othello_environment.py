import datetime
import dotenv
import os

# Load environment parameters.
# =================================================================================
dotenv.load_dotenv()

OTHELLO_OUTPUT_PATH = None
if 'OTHELLO_OUTPUT_PATH' not in os.environ:
  formatted_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
  OTHELLO_OUTPUT_PATH = f'output/{formatted_now}'
# =================================================================================

environment_variable_types = {
  'OTHELLO_BATCH_SIZE': int,
  'OTHELLO_C_PUCT': int,
  'OTHELLO_EPOCHS': int,
  'OTHELLO_GENERATOR_PATH': str,
  'OTHELLO_NUM_EPOCHS_PER_CHECKPOINT': int,
  'OTHELLO_NUM_GAMES_FOR_SUPERVISED_TRAINING': int,
  'OTHELLO_NUM_PROCESSES': int,
  'OTHELLO_NUM_SIMULATIONS': int,
  'OTHELLO_NUM_STEPS_PER_CHECKPOINT': int,
  'OTHELLO_NUMBER_OF_GAMES': int,
  'OTHELLO_ORACLE_URL': str,
  'OTHELLO_OUTPUT_PATH': str,
  'OTHELLO_RANDOM_SEED': int,
}

def parameter(environment_variable_name):
  if OTHELLO_OUTPUT_PATH is not None and environment_variable_name == 'OTHELLO_OUTPUT_PATH':
    value = OTHELLO_OUTPUT_PATH
  else:
    value = os.environ.get(environment_variable_name)
  assert value is not None, f'Error: Environment variable {environment_variable_name} not set.'
  value_type = environment_variable_types[environment_variable_name]
  value = value_type(value)
  return value
