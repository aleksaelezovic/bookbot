def count_words(content):
    count = len(content.split())
    return count


def get_character_count(content):
    dic = {}
    for c in content.lower():
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    return dic


def count_to_sorted(count):
    list = []
    for k in count:
        list.append({"char": k, "num": count[k]})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(item):
    return item["num"]
