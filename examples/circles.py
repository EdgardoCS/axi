import math
import random
import axi


def circle(cx, cy, r, n):
    points = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        x = cx + math.cos(a) * r
        y = cy + math.sin(a) * r
        points.append((x, y))
    return points


def random_points_on_circle(cx, cy, r, n):
    result = []
    a = random.random() * 2 * math.pi
    da = 2 * math.pi / n
    for i in range(n):
        x = cx + math.cos(a) * r
        y = cy + math.sin(a) * r
        result.append((x, y))
        a += da
    return result


def add(x, y, r, paths):
    if r < 1:
        return
    paths.append(circle(x, y, r, 90))
    points = random_points_on_circle(x, y, r, 1)
    for x, y in points:
        add(x, y, r / 2, paths)


def main():
    paths = []
    add(0, 0, 2, paths)
    new_path = [paths.pop()]
    drawing = axi.Drawing(new_path).rotate_and_scale_to_fit(2, 2)
    axi.draw(drawing)


if __name__ == '__main__':
    main()
