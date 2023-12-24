import math
import os

data = [line.split(" @ ") for line in open(os.path.join("input-data-2023", "23-24.txt")).read().strip().split("\n")]
data = [[list(map(int, positions.split(", "))), list(map(int, velocities.split(", ")))] for positions, velocities in
        data]

# for each line:
# get m[tx] and c[tx] in "t = mx+c"
# get m[yt] and c[yt] in "y = mt+c"
# get m[yx] and c[yx] in "y = mx+c" by substituting t for m[tx]*x + c[tx]
lines = []
for (xp, yp, _), (xv, yv, _) in data:
    # x = xp + t*xv -> t = x/xv - xp/xv; mtx = 1/xv, ctx = -xp/xv
    # y = yp + t*yv = yp + yv(mtx*x + ctx) = (mtx*yv)x + ctx*yv+yp = (yv/xv)x + (yp-xp/xv)
    lines.append((yv / xv, yv * -xp / xv + yp))

# for each pair of m/c pairs:
# check if x = (c2-c1)/(m1-m2) is at least 200000000000000 and at most 400000000000000
# check if y = m1(calculatedX)+c1 is at least 200000000000000 and at most 400000000000000
# check that corresponding times are positive
# increment validIntersections if all conditions are True
validIntersections = 0
for i, (m1, c1) in enumerate(lines[:-1]):
    for j, (m2, c2) in enumerate(lines[i + 1:]):
        (xp1, yp1, _), (xv1, yv1, _) = data[i]
        (xp2, yp2, _), (xv2, yv2, _) = data[i + j + 1]
        if m1 != m2:
            x = (c2 - c1) / (m1 - m2)
            y = m1 * x + c1
            assert(math.isclose(y, m2*x + c2))
            t1, t2 = (x-xp1)/xv1, (x-xp2)/xv2
            assert(math.isclose(t1,(y-yp1)/yv1))
            assert(math.isclose(t2, ((y-yp2)/yv2)))
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if t1 >= 0 and t2 >= 0:
                    validIntersections += 1
print(validIntersections)


