# Imports for:
import time  # management of timings and intervals
import keyboard  # detecting specific keyboard inputs as controls
import threading  # simultaneous task running


def control(car):
    """
    Function that lets user control the car with WASD keys and Esc to quit.

    Keyboard controls Layout:
    W - accelerate
    A - turn steering wheel left
    S - brake
    D - turn steering wheel right
    Esc - turn of the engine

    :param car:
    :return:
    """
    while car.idle_stopped == 0:
        try:
            # React to controls only if engine is running
            if car.engine_running:
                if keyboard.is_pressed("w"):
                    car.accelerate()
                if keyboard.is_pressed("a"):
                    car.turn("left")
                if keyboard.is_pressed("s"):
                    car.decelerate()
                if keyboard.is_pressed("d"):
                    car.turn("right")
                if keyboard.is_pressed("esc"):
                    car.idle_stopped = 1
                    break
            # Control to start the engine and allow other controls
            elif keyboard.is_pressed("g"):
                car.start_engine()
        finally:
            pass
    print("Control thread ended.")


class Car:
    """
    Class describing the Car object. Car will idle upon engine start and act accordingly upon receiving orders in the
    form of user pressing control keys using his keyboard.
    The scaling of values is purely guesswork and is not to be validated. Values like velocity, turning radius are for
     simulation purposes only and may not be balanced or resembling their real world counterparts.
    """
    def __init__(self, outside_temp=25, max_velocity=100, acceleration=2):
        """
        Constructor with assignable values (default if not assigned) of parameters:
        :param outside_temp: - temperature from which oil will start rising to 90 degrees
        :param max_velocity: - maximal achievable velocity of the vehicle
        :param acceleration: - rate at which the vehicle accelerates and brakes
        """
        self.max_velocity = max_velocity
        self.acceleration = acceleration
        self.oil_temp = outside_temp

        self.brakes = acceleration * 4

        # Basic starting values:
        self.velocity = 0
        self.turning_radius = 0
        self.fuel = 100
        self.engine_running = 0
        self.idle_stopped = 0

    def start_engine(self):
        """
        Starting the engine starts idle in background
        :return:
        """
        self.engine_running = 1
        thread3 = threading.Thread(target=self.idle)
        thread3.start()

    def idle(self):
        """
        Function that implements:
        -passive velocity loss to 0
        -passive oil temperature increase to 90 degrees Celsius
        -passive steering wheel unwinding to position 0 in function of current speed
        -passive fuel consumption (majorly sped up for simulation purposes)

        Additional info:
        -the car slows down in function of the absolute value of its turning radius
        -turning radius approaches zero in function of current velocity so it's essentially limited until slow down
        :return:
        """
        try:
            while not self.idle_stopped:
                if self.velocity > 0:
                    self.velocity -= self.velocity * abs(self.turning_radius) / (self.max_velocity * 5)
                if self.oil_temp < 90:
                    self.oil_temp += 0.1 * (1 + 5 * self.velocity / self.max_velocity)
                if self.turning_radius != 0 and self.velocity != 0:
                    self.turning_radius -= self.turning_radius * self.velocity / self.max_velocity
                if self.fuel > 0:
                    self.fuel -= 0.5
                # Stop idle if out of fuel
                else:
                    self.engine_running = 0
                    break
                time.sleep(0.1)
        finally:
            pass
        print("Idle thread ended.")

    def accelerate(self):
        """
        Function propelling the vehicle's speed in function of it's current velocity * (-1) scaled by it's maximal
        velocity and acceleration
        :return:
        """
        self.velocity += self.acceleration - self.velocity * (self.acceleration / self.max_velocity)
        time.sleep(0.1)

    def decelerate(self):
        """
        Function slowing the vehicle down according to it's velocity scaled by max_velocity and acceleration
        :return:
        """
        if self.velocity > 0:
            self.velocity -= self.velocity * (self.brakes / self.max_velocity)
        time.sleep(0.1)

    def turn(self, side):
        """
        Function turning the steering wheel in the direction specified by "side"
        :param side: - direction to turn the wheels to
        :return:
        """
        if side == "right":
            # Check if change will not exceed the 180° limit
            if self.turning_radius < 161:
                self.turning_radius += 10
        if side == "left":
            # Check if change will not exceed the -180° limit
            if self.turning_radius > -161:
                self.turning_radius -= 10
        time.sleep(0.1)

    def print_logs(self, interval):
        """
        Function printing logs consisting of cars velocity, turning radius and oil temperature
        :param interval: - number of seconds between each log
        :return:
        """
        try:
            while True:
                if self.idle_stopped:
                    break
                # Only log if engine is running
                if self.engine_running:
                    # The just function helps keep the logs at a static length for an easier reading experience
                    print("Velocity: " + str(int(self.velocity)).rjust(3, ' ') + "km/h"
                          + " Turning radius: " + str(int(self.turning_radius)).rjust(4, ' ') + "°"
                          + " Oil temperature: " + str(int(self.oil_temp)) + "°C"
                          + " Fuel: " + str(int(self.fuel)) + "%")
                # Stop logging when out of fuel - engine dead
                elif self.fuel <= 0:
                    print("Vehicle run out of fuel.")
                    self.idle_stopped = 1
                    break
                time.sleep(interval)
        finally:
            pass
        # Prompt user Logs ended
        print("Logging thread ended. ")


def main():
    """
    Main function
    :return:
    """
    interval_of_logging = 1
    # Display set interval
    print("Logging interval = " + str(interval_of_logging) + " s")
    print("To start engine press the \"g\" key. While logging press the \"Esc\" key to stop. ")
    # Example of a car object with 10°C outside temperature, 200 km/h max speed, and acceleration factor of 5
    porsche = Car(10, 200, 5)

    # Usage of threading lets some tasks run simultaneously (f.e. logging and controls)
    thread1 = threading.Thread(target=porsche.print_logs, args=(interval_of_logging,))
    thread2 = threading.Thread(target=control, args=(porsche,))
    thread2.start()
    thread1.start()
    return


if __name__ == "__main__":
    main()
