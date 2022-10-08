

def summaryRanges(nums: list[int]) -> list[str]:
        
    # base cases
    if len(nums) == 0:
        return ""
    if len(nums) == 0:
        return str(nums[0])
    
    outlist = []
    # start of the outlist index
    start_idx = 0
    
    string = str(nums[start_idx])
    for left_idx in range(len(nums) - 1):
        if nums[left_idx + 1] - nums[left_idx] > 1:
            if nums[start_idx] == nums[left_idx]:
                outlist.append(string)
            else:
                string += "->" + str(nums[left_idx])
                outlist.append(string)
            start_idx = left_idx + 1
            string = str(nums[start_idx])
    
    if start_idx == len(nums) - 1:
        outlist.append(string)
    else:
        string += "->" + str(nums[-1])
        outlist.append(string)
    return outlist


if __name__=="__main__":
    nums = [0,1,2,4,5,7]
    print(summaryRanges(nums))
