from collections.abc import Hashable
hash_list = [hash(i) for i in object_list if isinstance(i, Hashable)]
sum_ = 0
for i in hash_list:
    if hash_list.count(i) > 1:
        sum_ += hash_list.count(i)
        hash_list = list(filter(lambda a: a != i, hash_list))
print(sum_)
