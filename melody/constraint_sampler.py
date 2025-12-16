def constrained_sample(candidate_degrees, last_degree, last_interval):
    """
    输入：模型给的一堆候选
    输出：合法的一个
    """

    valid = []

    for d in candidate_degrees:
        interval = abs(d - last_degree)

        # ❌ 连续大跳
        if last_interval >= 5 and interval >= 5:
            continue

        # ❌ 7 级落强拍（这里简化）
        if d == 7:
            continue

        valid.append(d)

    return valid[0] if valid else last_degree
