"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import itertools

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
diff_chart = {}
for i,j in itertools.product(q,q):
    diff = f(i) - f(j)
    if diff in diff_chart:
        diff_chart[diff].append((i,j))
    else:
        diff_chart[diff] = [(i,j)]
for x,y in itertools.product(q, q):
    xy_sum = f(x) + f(y)
    if xy_sum in diff_chart:
        for pair in diff_chart[xy_sum]:
            vars = f"f({x}) + f({y}) = f({pair[0]}) - f({pair[1]})"
            nums = f"{f(x)} + {f(y)} = {f(pair[0])} - {f(pair[1])}"
            print(vars + "   " + nums)