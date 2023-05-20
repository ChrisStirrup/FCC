import random
import copy


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            while value > 0:
                self.contents.append(key)
                value -= 1


    def draw(self, num_of_balls):
        draw_bag = self.contents
        global balls_drawn
        balls_drawn = []
        while num_of_balls > 0 and len(draw_bag) > 0:
            num_of_balls -= 1
            drawn_ball = random.randint(1, len(draw_bag)) - 1
            balls_drawn.append(draw_bag[drawn_ball])
            draw_bag.pop(drawn_ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        copy_hat.draw(num_balls_drawn)
        set_expected_balls = set(expected_balls)
        set_balls_drawn = set(balls_drawn)
        if set_expected_balls.issubset(set_balls_drawn):
            matches += 1
    experiment_outcome = matches / num_experiments
    print(experiment_outcome)
