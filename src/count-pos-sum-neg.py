def count_positives_sum_negatives(arr):
    """From list, tally positive numbers, sum the negatives.""" 
    answer_array = []
    positives = 0
    sum_negs = 0
    if arr == []:
        return arr
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            sum_negs += i
    answer_array.append(positives)
    answer_array.append(sum_negs)
    return answer_array
