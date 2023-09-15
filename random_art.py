import math
import random
import numpy as np
import cairo

DIRECTION_TRANSITION_MATRIX = {
    'R': {'R': .5, 'U': .3, 'L': .1, 'D': .1},
    'U': {'R': .1, 'U': .5, 'L': .1, 'D': .3},
    'D': {'R': .1, 'U': .1, 'L': .3, 'D': .5},
    'L': {'R': .25, 'U': .25, 'L': .25, 'D': .25}
}

SCALE_TRANSITION_MATRIX = {
    'tiny': {'tiny': 0.4, 'small': 0.3, 'medium': 0.2, 'large': 0.1},
    'small': {'tiny': 0.4, 'small': 0.2, 'medium': 0.2, 'large': 0.2},
    'medium': {'tiny': 0.25, 'small': 0.25, 'medium': 0.25, 'large': 0.25},
    'large': {'tiny': 0.7, 'small': 0.1, 'medium': 0.1, 'large': 0.1}
}

SCALE_TO_RADIUS = {
    'tiny': 2,
    'small': 3,
    'medium': 5,
    'large': 9
}


def nextPosition(x, y, direction, magnitude):
    """Compute the next position based on the current position, direction, and magnitude."""
    if direction == 'U':
        y += magnitude
    elif direction == 'D':
        y -= magnitude
    elif direction == 'L':
        x -= magnitude
    else:
        x += magnitude

    return x, y


class MoveArtist:

    def __init__(self, direction_matrix, scale_matrix, painting_name, background_image):
        """Initialize the MoveArtist with given parameters."""
        self.transition_matrix = direction_matrix
        self.directions = list(direction_matrix.keys())
        self.background_image = cairo.ImageSurface.create_from_png(background_image)
        self.canvas_width = self.background_image.get_width()
        self.canvas_height = self.background_image.get_height()
        self.position = (random.randint(0, self.canvas_width), random.randint(0, self.canvas_height))
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.canvas_width, self.canvas_height)
        self.canvas = cairo.Context(self.surface)
        # the last direction is initialized to L because L has an equal transition probability to the other directions
        self.last_direction = 'L'
        self.painting_name = painting_name
        self.scale_matrix = scale_matrix
        self.scales = list(scale_matrix.keys())
        self.last_scale = 'medium'

    def set_background(self):
        """Set the given picture as the background for the painting."""

        pattern = cairo.SurfacePattern(self.background_image)
        self.canvas.set_source(pattern)
        self.canvas.paint()

    def isValid(self, x, y):
        """Check if the given x, y position is within canvas boundaries."""
        return 0 <= x < self.canvas_width and 0 <= y < self.canvas_height

    def newScale(self):
        """Choose a new scale based on the scale transition matrix."""
        return np.random.choice(self.scales,
                                p=[self.scale_matrix[self.last_scale][next_scale] for next_scale in self.scales])

    def newDirection(self):
        """Choose a new direction based on the direction transition matrix."""
        return np.random.choice(self.directions,
                                p=[self.transition_matrix[self.last_direction][next_direction] for next_direction in
                                   self.directions])

    def writeToFile(self):
        """Save the painting to a file."""
        self.surface.write_to_png(self.painting_name)

    def paint(self):
        """Driver function to paint the painting"""

        self.set_background()
        for _ in range(20000):
            # Choose random RGB values for new dot
            red, green, blue = random.random(), random.random(), random.random()

            new_direction = self.newDirection()
            new_scale = self.newScale()
            magnitude = SCALE_TO_RADIUS[new_scale]

            new_position = nextPosition(*self.position, new_direction, magnitude)

            # Ensure that the position is within the canvas
            while not self.isValid(new_position[0], new_position[1]):
                new_direction = self.newDirection()
                new_position = nextPosition(*self.position, new_direction, magnitude)

            self.canvas.arc(*new_position, magnitude, 0, 2 * math.pi)
            self.canvas.set_source_rgb(red, green, blue)
            self.canvas.fill()

            self.position = new_position
            self.last_scale = new_scale


def main():
    """Main function to initiate the painting process."""
    painting = MoveArtist(DIRECTION_TRANSITION_MATRIX, SCALE_TRANSITION_MATRIX, 'painting.png',
                          f'Backgrounds/background{random.randint(1, 3)}.png')
    print('Painting my painting')
    painting.paint()
    print('Delivering painting')
    painting.writeToFile()
    print('Painting finished!')


if __name__ == "__main__":
    main()
