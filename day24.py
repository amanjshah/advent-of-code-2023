import os
from sympy import symbols, Eq, solve

data = [[list(map(int, positions.split(", "))), list(map(int, velocities.split(", ")))] for positions, velocities in
        [line.split(" @ ") for line in open(os.path.join("input-data-2023", "23-24.txt")).read().strip().split("\n")]]
rocks = (xr, _), (yr, _), (zr, _) = symbols("xr, vxr"), symbols("yr, vyr"), symbols("zr, vzr")


def getSimultaneousEquations():
    times, eqs = symbols("t1, t2, t3"), []
    for i, ((xh, yh, zh), (vxh, vyh, vzh)) in enumerate(data[:3]):
        time, hail = times[i], ((xh, vxh), (yh, vyh), (zh, vzh))
        for (rockPosition, rockVelocity), (hailPosition, hailVelocity) in zip(rocks, hail):
            eqs.append(Eq(rockPosition - hailPosition, time * (hailVelocity - rockVelocity)))
    return eqs


def getResult():
    res = solve(getSimultaneousEquations())
    assert (len(res) == 1)
    return sum(res[0][key] for key in (xr, yr, zr))


print(getResult())
