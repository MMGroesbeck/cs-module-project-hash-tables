"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import itertools

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
# # Version 1:
# diff_chart = {}
# out = ""
# for i,j in itertools.product(q,q):
#     diff = f(i) - f(j)
#     if diff in diff_chart:
#         diff_chart[diff].append((i,j))
#     else:
#         diff_chart[diff] = [(i,j)]
# for x,y in itertools.product(q, q):
#     xy_sum = f(x) + f(y)
#     if xy_sum in diff_chart:
#         for pair in diff_chart[xy_sum]:
#             vars = f"f({x}) + f({y}) = f({pair[0]}) - f({pair[1]})"
#             nums = f"{f(x)} + {f(y)} = {f(pair[0])} - {f(pair[1])}"
#             # print(vars + "   " + nums)
#             out = out + f"{vars:30} {nums}\n"

# Version 2:
# charts is [diff_chart, sum_chart]
charts = [{},{}]
out = ""
for i,j in itertools.product(q,q):
    vals = (f(i)-f(j), f(i)+f(j))
    for ind in range(2):
        if vals[ind] in charts[ind]:
            charts[ind][vals[ind]].append((i,j))
        else:
            charts[ind][vals[ind]] = [(i,j)]
for diff in charts[0]:
    if diff in charts[1]:
        for i,j in itertools.product(charts[0][diff], charts[1][diff]):
            vars = f"f({j[0]}) + f({j[1]}) = f({i[0]}) - f({i[1]})"
            vals = f"{f(j[0])} + {f(j[1])} = {f(i[0])} - {f(i[1])}"
            # print(f"{vars:30} {vals}")
            out = out + f"{vars:30} {vals}\n"

# print(out)