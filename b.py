from itertools import combinations

letters = []
arr = []
number_combos = { "2" : ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5" : ["j","k","l"], "6" : ["m","n","o"], "7" : ["p","q","r", "s"], "8": ["t","u", "v"], "9":["w","x","y","z"]}

def permute(input_str):
    for i in input_str:
        arr = number_combos[i]
        letters.extend(arr)
    return letters
combos = []
letters = permute('23')
print(letters)
def char_combos(cur_idx, cur_combo,cur_str,combos):
    if cur_idx == len('23'):
        # no more element, add current permutation to result list
        combos.append(cur_str)
        cur_combo.append( cur_combo[::] )
        return 
    for swap_idx in range(cur_idx, len(letters)):
        letters[swap_idx], letters[cur_idx] = letters[cur_idx], letters[swap_idx]
        cur_str += letters[cur_idx]

        cur_combo.append( letters[cur_idx] )
        char_combos(cur_idx+1, cur_combo,cur_str,combos)
        cur_str = cur_str[:-1]
        cur_combo.pop()
        letters[swap_idx], letters[cur_idx] = letters[cur_idx], letters[swap_idx]
    
    return cur_combo
    
print(char_combos(0,[],'',combos))
print(combos)