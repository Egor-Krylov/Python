result = "утверждение верно"
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (not (x and y and z) == (not x) or (not y) or (not z)):
                result = "утверждение не верно"
print(result)
