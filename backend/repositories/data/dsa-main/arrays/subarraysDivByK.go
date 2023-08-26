func subarraysDivByK(nums []int, k int) int {

    table := make(map[int]int)
    ans := 0
    prefix := 0

    table[0] = 1

    for index, _ := range nums {
        prefix += (nums[index]%k + k) % k
        prefix = prefix%k
        
        if val, ok := table[prefix]; ok {
            ans += val
        }

        table[prefix] += 1
    }

    return ans
}


func abs(num int) int {
    if num<0{
        return -1*num
    }

    return num
}
