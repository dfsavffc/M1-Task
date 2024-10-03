from object import Object
import numpy as np

class Scene:
    def __init__(self, data: dict, resistance_type: int) -> None:
        self.object = Object(data, resistance_type)

    def calc_dt(self, eps: float) -> float:
        return eps * np.linalg.norm(self.object.velocity_) / np.linalg.norm(self.object.calc_acceleration())
    def simulate(self, eps: float) -> dict:
        results = {'abscissa': [], 'ordinate': [], 'total_time': 0}
        while not self.object.check_landing():
            dt = self.calc_dt(eps)
            curr_x, curr_y = self.object.coordinates_
            results['abscissa'].append(curr_x)
            results['ordinate'].append(curr_y)
            self.object.update(dt)
            results['total_time'] += dt

        dt = self.calc_dt(eps)
        curr_x, curr_y = self.object.coordinates_
        results['abscissa'].append(curr_x)
        results['ordinate'].append(curr_y)
        self.object.update(dt)
        results['total_time'] += dt

        return results

