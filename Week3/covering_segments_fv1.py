# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    begin_point = []
    end_point = []
    for s in segments:
        begin_point.append(s.start)
        end_point.append(s.end)

    while len(begin_point)>0:
        safe_move_beg = min(begin_point) #it will always be the first minimum
        safe_move_index = begin_point.index(safe_move_beg) #first minimum index
        safe_move_end = end_point[safe_move_index]
        eliminate_target = []
        arrive_dot = safe_move_end
        for i in range(len(begin_point)):
            if begin_point[i]<= safe_move_end:
                arrive_dot = min(arrive_dot,end_point[i])
                eliminate_target.append(i)
        begin_point = [v for i, v in enumerate(begin_point) if i not in eliminate_target]
        end_point = [v for i, v in enumerate(end_point) if i not in eliminate_target]

        points.append(arrive_dot)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
