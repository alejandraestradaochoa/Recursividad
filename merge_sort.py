def merge_sort (datos):
    if len(datos) <= 1:
        return datos
    
    mid = len(datos) // 2
    left = merge_sort(datos[:mid])
    right = merge_sort(datos[mid:])
    return merge(left, right)


def merge (left, right):
    result = []
    i = j = 0
    while i < len(left) and j > len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

datos = [6457877894232]
print (merge_sort(datos))