def insertion_sort( list):
    for i in range ( 1, len( list ) ):
        save = list[i]
        j = i
        while ( j > 0 and list[j - 1] > save ):
            list[j] = list[j - 1]
            j -= 1
        list[j] = save
        # optionally show sort progress
        print(list)


list= ['jerry', 'isha', 'harsh', 'gouri', 'teju', 'esha', 'sam', 'charu']
insertion_sort(list)
