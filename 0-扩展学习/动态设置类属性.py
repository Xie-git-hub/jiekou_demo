"""
======================
Author: 柠檬班-小简
Time: 2020/7/8 21:38
Project: day7
Company: 湖南零檬信息技术有限公司
======================
"""

class AABB:

    cc = "hello"
    pass

# setattr,hasattr,getattr,delattr

setattr(AABB,"name","hello")
print(AABB.name)


print(AABB.__dict__)

values = dict(AABB.__dict__.items())
print(values)
for key,value in values.items():
    if key.startswith("__"):
        pass
    else:
        delattr(AABB,key)

print(AABB.__dict__)
