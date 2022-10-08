# Missing Ranges (Source. Leetcode 163) Given a sorted integer array
# where the range of elements are in the inclusive range [lower, upper],
# return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, 
# return ["2", "4->49", "51->74", "76->99"].
def __get_range(a, b):
    if b - a > 1:
        if b - a == 2:
            return str(a+1)
        else:
            return str(a+1) + "->" + str(b-1)
    return None

def missing_ranges(nums, lower, upper):
    assert(upper >= max(nums))
    
    outlist = []
    lower = max(lower, nums[0])
    for i in range(len(nums)):
        if nums[i] > lower:
            if nums[i] - 1 == lower:
                outlist.append(str(lower))
            else:
                outlist.append(str(lower) + "->" + str(nums[i] - 1))
        lower = max(lower, nums[i] + 1)
    
    if lower < upper:
        outlist.append(str(lower) + "->" + str(upper))
    print(outlist)
            
        
        
if __name__=="__main__":
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    missing_ranges(nums, lower, upper)