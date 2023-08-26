func maxSubarraySumCircular(nums []int) int {
    
    N := len(nums)

    cur := 0
    ans := -30001
    sum := 0
    allNeg := true

    for i:=0; i<N; i++{
        cur += nums[i]
        sum += nums[i]
        ans = max(ans, cur)
        if(cur<0){
            cur = 0
        }

        if(nums[i]>=0){
            allNeg = false
        }
    }

    cur = 0
    for i:=0; i<N; i++{
        cur += nums[i]
        ans = max(ans, sum - cur)
        if(cur>0){
            cur = 0
        }
    }

    if(allNeg) {
        ans = nums[0]
        for _, val := range nums{
            ans = max(ans, val)
        }
        return ans
    }

    return ans
}

func max(a int, b int) int {
    if(a>b){
        return a
    }

    return b
}
