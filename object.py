import numpy as np


class Object:
    def __init__(self, data: dict, resistance_type: int) -> None:
        self.mass_ = data['mass']
        self.coordinates_ = np.array([0, 0])
        self.velocity_ = np.array([data['velocity_x'], data['velocity_y']])
        self.g_ = np.array([0.0, data['g']])
        self.resistance_coefficient_ = data['resistance_coefficient']
        self.resistance_type_ = resistance_type


    def update_velocity(self, dt: float) -> None:
        self.velocity_ = self.velocity_ - (
                self.g_ + (self.resistance_coefficient_ / self.mass_) * self.velocity_ * np.linalg.norm(
            self.velocity_) ** self.resistance_type_) * dt

    def calc_acceleration(self):
        return self.g_ + (self.resistance_coefficient_ / self.mass_) * self.velocity_ * np.linalg.norm(
            self.velocity_) ** self.resistance_type_

    def update_position(self, dt: float) -> None:
        self.coordinates_ = self.coordinates_ + self.velocity_ * dt

    def update(self, dt: float) -> None:
        self.update_position(dt)
        self.update_velocity(dt)

    def check_landing(self) -> bool:
        if self.coordinates_[1] < 0:
            return True
        return False
