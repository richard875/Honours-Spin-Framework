import os
import time
import random

from functions.bitonic_sort import bitonic_sort_test
from functions.brick_sort import brick_sort_test
from functions.bubble_sort import bubble_sort_test
from functions.bucket_sort import bucket_sort_test
from functions.cocktail_sort import cocktail_sort_test
from functions.comb_sort import comb_sort_test
from functions.gnome_sort import gnome_sort_test
from functions.heap_sort import heap_sort_test
from functions.insertion_sort import insertion_sort_test
from functions.merge_sort import merge_sort_test
from functions.pancake_sort import pancake_sort_test
from functions.pigeonhole_sort import pigeonhole_sort_test
from functions.quick_sort import quick_sort_test
from functions.radix_sort import radix_sort_test
from functions.selection_sort import selection_sort_test
from functions.shell_sort import shell_sort_test
from functions.smooth_sort import smooth_sort_test
from functions.strand_sort import strand_sort_test


def main():
    bitonic_sort = bitonic_sort_test()
    brick_sort = brick_sort_test()
    bubble_sort = bubble_sort_test()
    bucket_sort = bucket_sort_test()
    cocktail_sort = cocktail_sort_test()
    comb_sort = comb_sort_test()
    gnome_sort = gnome_sort_test()
    heap_sort = heap_sort_test()
    insertion_sort = insertion_sort_test()
    merge_sort = merge_sort_test()
    pancake_sort = merge_sort_test()
    pigeonhole_sort = pancake_sort_test()
    quick_sort = quick_sort_test()
    radix_sort = radix_sort_test()
    selection_sort = selection_sort_test()
    shell_sort = shell_sort_test()
    smooth_sort = smooth_sort_test()
    strand_sort = strand_sort_test()

    print('bitonic_sort: {}s'.format(bitonic_sort))
    print('brick_sort: {}s'.format(brick_sort))
    print('bubble_sort: {}s'.format(bubble_sort))
    print('bucket_sort: {}s'.format(bucket_sort))
    print('cocktail_sort: {}s'.format(cocktail_sort))
    print('comb_sort: {}s'.format(comb_sort))
    print('gnome_sort: {}s'.format(gnome_sort))
    print('heap_sort: {}s'.format(heap_sort))
    print('insertion_sort: {}s'.format(insertion_sort))
    print('merge_sort: {}s'.format(merge_sort))
    print('pancake_sort: {}s'.format(pancake_sort))
    print('pigeonhole_sort: {}s'.format(pigeonhole_sort))
    print('quick_sort: {}s'.format(quick_sort))
    print('radix_sort: {}s'.format(radix_sort))
    print('selection_sort: {}s'.format(selection_sort))
    print('shell_sort: {}s'.format(shell_sort))
    print('smooth_sort: {}s'.format(smooth_sort))
    print('strand_sort: {}s'.format(strand_sort))

if __name__ == "__main__":
    main()