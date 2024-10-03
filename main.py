from reading import read_data
from scene import Scene
from theory import calculate_function
from visualisation import draw_charts

data = read_data('starting_conditions.json')

scene_v= Scene(data, 0)
scene_square_v = Scene(data, 1)

prediction_v = scene_v.simulate(data["accuracy"])
prediction_square_v = scene_square_v.simulate(data["accuracy"])
predictions = {"v" : prediction_v, "square_v": prediction_square_v}


functions = calculate_function(data)
draw_charts(predictions, functions)
