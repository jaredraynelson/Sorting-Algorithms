from random import random, seed, sample
from time import perf_counter_ns

def selection_sort(lyst):
    '''
    TAKES IN A LIST, AND RETURNS A SORTED LIST
    '''
    k = 0
    end = len(lyst)
    while k < len(lyst):
        # WITH EACH ITERATION, THE LOWEST ELEMENT WILL BE IN IT'S
        # DEFINITE LOCATION.

        min_val = lyst[k]
        for i in lyst[k:end]:
            if i < min_val:
                min_val = i
        # TAKES THE VALUE AT THE INDEX OF THE SMALLER LYST
        min_val_index = lyst[k:end].index(min_val)
        # THE INDEX VALUE IS OFFSET BY K, SO MUCH +K TO INDEX
        # TO FIND THE TRUE VALUE.
        lyst[k], lyst[min_val_index+k] = lyst[min_val_index+k], lyst[k]
        k = k + 1

    return lyst


def insertion_sort(lyst):
    '''
    TAKES IN A LIST, AND RETURNS A SORTED LIST
    '''
    k = 0
    max_val = lyst[k]
    min_val = lyst[k]
    while k < len(lyst)-1:
        next_index = k + 1
        if lyst[next_index] >= max_val:
            max_val = lyst[next_index]
        elif lyst[next_index]<=min_val:
            min_val = lyst.pop(next_index)
            lyst.insert(0,min_val)
        # THE CASE THAT THE VALUES FALL BETWEEN THE SMALLEST AND
        # LARGEST VALUES OF THE SMALLER LIST.
        else:
            iterable_lyst = list(range(0,lyst.index(max_val)))
            for i in iterable_lyst:
                next_index_i = i+1
                if (lyst[next_index] > lyst[i]) and (lyst[next_index]<= lyst[next_index_i]):
                    pop_val = lyst.pop(next_index)
                    lyst.insert(next_index_i,pop_val)
        k = k + 1
    return lyst


def mergesort(lyst):
    '''
    TAKES IN A LIST, AND RETURNS A SORTED LIST
    '''
    if len(lyst)>1:
        mid = len(lyst)//2

        right_lyst = lyst[:mid]
        left_lyst = lyst[mid:]
        mergesort(right_lyst)
        mergesort(left_lyst)

        i = j = k = 0

        while i < len(right_lyst) and j < len(left_lyst):
            if right_lyst[i] > left_lyst[j]:
                lyst[k] = left_lyst[j]
                j = j + 1
            else:
                lyst[k] = right_lyst[i]
                i = i + 1
            k = k + 1

        while i<len(right_lyst):
            lyst[k] = right_lyst[i]
            i = i + 1
            k = k + 1
        while j<len(left_lyst):
            lyst[k] = left_lyst[j]
            j = j + 1
            k = k + 1
    return lyst


def quicksort(lyst):
    '''
    TAKES IN A LIST, AND RETURNS A SORTED LIST
    '''
    if lyst==[]:
        return lyst
    if len(lyst)==1:
        return lyst
    if len(lyst)==2:
        if lyst[0]>lyst[1]:
            lyst[0], lyst[1] = lyst[1], lyst[0]
            return lyst
        else:
            return lyst

    pivot_index = 0
    pivot_value = lyst[pivot_index]
    left_mark = 1
    right_mark = len(lyst)-1

    correct_pivot_placement = False
    # THIS WILL CONTINUE UNTIL THE PIVOT PLACE IS SWAPPED WITH THE CORRECT VALUE.
    while not correct_pivot_placement:
        # GO UNTIL THE PATHS OF LEFT MARK AND RIGHT MARK CROSS.
        while left_mark < right_mark:
            while lyst[left_mark] <= pivot_value and left_mark < right_mark:
                left_mark = left_mark + 1
            while lyst[right_mark] > pivot_value and right_mark >= left_mark:
                right_mark = right_mark - 1
            # IF THIS CASE IS TRUE, THEN THE VALUES WILL SWITCH.
            if lyst[right_mark] <= pivot_value and lyst[left_mark] > pivot_value and left_mark < right_mark:
                lyst[left_mark], lyst[right_mark] = lyst[right_mark], lyst[left_mark]

        lyst[pivot_index], lyst[right_mark] = lyst[right_mark], lyst[pivot_index]
        correct_pivot_placement = True

    if right_mark == pivot_index:
        left_mark_lyst = lyst[pivot_index:left_mark]
        right_mark_lyst = lyst[left_mark:]
    elif left_mark == len(lyst)-1:
        right_mark_lyst = lyst[left_mark:]
        left_mark_lyst = lyst[pivot_index:left_mark]
    else:
        left_mark_lyst = lyst[:right_mark]
        right_mark_lyst = lyst[right_mark:]

    # THIS CASE MEANS THE LIST IS ALREADY SORTED
    if right_mark_lyst == lyst:
        return right_mark_lyst
    # THIS CASE MEANS THE LIST IS ALREADY SORTED
    if left_mark_lyst == lyst:
        return right_mark_lyst

    # RECURSIVE PORTION OF THE FUNCTION
    left_mark_lyst = quicksort(left_mark_lyst)
    right_mark_lyst = quicksort(right_mark_lyst)

    lyst = left_mark_lyst + right_mark_lyst

    return lyst


def is_sorted(lyst):
    '''
    TAKES IN A LIST, AND RETURNS A BOOLEAN CONFIRMING
    WHETHER THE LIST IS SORTED
    '''
    if lyst == sorted(lyst):
        return True
    else:
        return False
    

def c_sort(lyst):
    low_num_n_lyst = min(lyst)
    high_num_n_lyst = max(lyst)
    sorted_lyst = [0 for i in range(len(lyst))]
    ind_matrix = [0 for i in range(low_num_n_lyst, high_num_n_lyst+1)]
    
    # COUNT NUMBER OF OCCURENCES:
    for i in lyst:
        i_minus_low_num_ind = i - low_num_n_lyst
        ind_matrix[i_minus_low_num_ind] += 1
    
    # print(ind_matrix)
    bool_matrix = ind_matrix.copy()
    # ADD THE ADJACENT MATRIX VALUES
    i = 0
    adj_ind_matrix_ele_summed = ind_matrix.copy()
    
    while i < len(ind_matrix)-1:
        adj_ind_matrix_ele_summed[i+1] = ind_matrix[i+1] + adj_ind_matrix_ele_summed[i]
        i += 1
    
    adj_n_shifted_matrix = [0] + adj_ind_matrix_ele_summed[:-1]

    ind_reference = adj_n_shifted_matrix.copy()
    # print(ind_reference)
    
    j = 0
    
    for i in lyst:
        ind = i - low_num_n_lyst
        location = ind_reference[ind] 
        if not bool_matrix[ind]:
            continue
        elif bool_matrix[ind] > 1:
            for j in range(bool_matrix[ind]):
                sorted_lyst[location+j] = i
        else:
            sorted_lyst[location] = i

    

    return sorted_lyst


def main():
    # GENERATING RANDOM LIST
    size = 10000
    print(f"Creating a sorted array of {size}")
    seed(0)
    random_lyst = sample(range(size*3), k=size)
    
    # COPY OF THE LYST IS PASSED INTO FUNCTIONS
    
    start = perf_counter_ns()
    s_sort_return_lyst = selection_sort(random_lyst.copy())
    end = perf_counter_ns()
    print('selection_sort duration:', (end-start)/10**6, 'miliseconds')

    start = perf_counter_ns()
    in_sort_return_lyst = insertion_sort(random_lyst.copy())
    end = perf_counter_ns()
    print('insertion_sort duration:', (end-start)/10**6, 'miliseconds')

    start = perf_counter_ns()
    merg_sort_return_lyst = mergesort(random_lyst.copy())
    end = perf_counter_ns()
    print('mergesort duration:\t', (end-start)/10**6, 'miliseconds')

    start = perf_counter_ns()
    quick_sort_return_lyst = quicksort(random_lyst.copy())
    end = perf_counter_ns()
    print('quicksort duration:\t', (end-start)/10**6, 'miliseconds')

    start = perf_counter_ns()
    c_sort_return_lyst = c_sort(random_lyst.copy())
    end = perf_counter_ns()
    print('counting_sort duration:', (end-start)/10**6, 'miliseconds')

    # IN PYTHON TIMSORT IS USED AS PRIMARY SORTING METHOD SORTED()
    start = perf_counter_ns()
    sorted(random_lyst.copy())
    end = perf_counter_ns()
    print('timsort duration:\t', (end-start)/10**6, 'miliseconds')

    print('\n')
    

    print('***RESULTS***')
    print('Selection sort is sorted:', is_sorted(s_sort_return_lyst))
    print('Insertion sort is sorted:', is_sorted(in_sort_return_lyst))
    print('Merge sort is sorted:    ', is_sorted(merg_sort_return_lyst))
    print('Quick sort is sorted:    ', is_sorted(quick_sort_return_lyst))
    print('Counting sort is sorted: ', is_sorted(c_sort_return_lyst))



if __name__ == '__main__':
    main()