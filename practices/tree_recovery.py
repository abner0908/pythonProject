#!/usr/bin/env python

def traversal(pre_ord, in_ord):
    post_ord = ""
    first = pre_ord[0]
    fst_idx_in = in_ord.find(first)
    
    left_idx_in = fst_idx_in - 1
    right_idx_in = fst_idx_in + 1 
    in_ord_l = in_ord[:left_idx_in+1]
    in_ord_r = in_ord[right_idx_in:]

    left_chr = in_ord[left_idx_in]
    right_chr = in_ord[right_idx_in]
    left_idx_pre = pre_ord.find(left_chr)
    right_idx_pre = pre_ord.find(right_chr)

    pre_ord_l = pre_ord[1:left_idx_pre+1]
    pre_ord_r = pre_ord[right_idx_pre:]
    
    if left_idx_in >= 0:
        post_ord += traversal(pre_ord_r, in_ord_r)
    if right_idx_in < len(in_ord):
        post_ord += traversal(pre_ord_l, in_ord_l)

    return post_ord   


pre_ord = raw_input("please input the preoder of your tree:")
in_ord = raw_input("please input the inoder of your tree:")

pre_ord = pre_ord.strip()
in_ord = in_ord.strip()

traversal(pre_ord, in_ord)
