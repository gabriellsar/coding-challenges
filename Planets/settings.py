import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
BALL_SIZE = (30, 30)
BALL_SPEED = 450
BALL_COLOR = "red"
G_CONSTANT = 6.67
BG_COLOR = "#002633"

PLANETS = {
    'SATURN': {"cor": "brown", "mass": 200},
    'EARTH': {"cor": "green", "mass": 100},
    'NEPTUNE': {"cor": "blue", "mass": 50},
    'MERCURY': {"cor": "red", "mass": 20}
}
