from managers.game_manager import game_manager
from pprint import pprint

# For guide to Python with JSON, see http://docs.python-guide.org/en/latest/scenarios/json/
manager = game_manager()

#"Game" Loop
manager.game_loop()

pprint(manager.json_manager.get_data())
print("Global Scores:")
pprint(manager.scores_manager.get_global_scores())

