# TODO: 일단 잘 모르겠으면 노가다를 해본 다음에 그 아래 노가다들의 규칙을 찾는 방법도 하나의 방법이겠네
# TODO: 너무 어렵게 풀어서 다시 풀어보는 연습을 하면 좋을 듯
for i in range(1, 20):
    for j in range(1, 20):
        if i % 2 != 0:
            if (i * j) % 2 == 0:
                print(f"{i} * {j} = {i * j}", end = "\n")
            elif j < 19:
                print(f"{i} * {j} = {i * j}", end = " / ")
            else:
                print(f"{i} * {j} = {i * j}")
        else:
            if (i * j) % (i * 2) == 0:
                print(f"{i} * {j} = {i * j}", end = "\n")
            elif j < 19:
                print(f"{i} * {j} = {i * j}", end = " / ")
            else:
                print(f"{i} * {j} = {i * j}")


# 일단 잘 모르겠으면 노가다를 해본 다음에 그 아래 노가다들의 규칙을 찾는 방법도 하나의 방법이겠네

# cnt = 1
# for j in range(1, 20):
#     if (cnt * j) % 2 == 0:
#         print(f"{cnt} * {j} = {cnt * j}", end = "\n")
#     elif j < 19:
#         print(f"{cnt} * {j} = {cnt * j}", end = " / ")
#     else:
#           print(f"{cnt} * {j} = {cnt * j}")

# cnt = 2
# for j in range(1, 20):
#     if (cnt * j) % 4 == 0:
#         print(f"{cnt} * {j} = {cnt * j}", end = "\n")
#     elif j < 19:
#         print(f"{cnt} * {j} = {cnt * j}", end = " / ")
#     else:
#           print(f"{cnt} * {j} = {cnt * j}")

# cnt = 3
# for j in range(1, 20):
#     if (cnt * j) % 2 == 0:
#         print(f"{cnt} * {j} = {cnt * j}", end = "\n")
#     elif j < 19:
#         print(f"{cnt} * {j} = {cnt * j}", end = " / ")
#     else:
#           print(f"{cnt} * {j} = {cnt * j}")