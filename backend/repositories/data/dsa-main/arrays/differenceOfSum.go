func differenceOfSum(nums []int) int {
    
    elementSum:=0
    digitSum:=0
    
    for i:=0; i<len(nums); i++{
        elementSum += nums[i]
        digitSum += digitsum(nums[i])
    }
    
    return max(elementSum, digitSum) - min(elementSum, digitSum)
}


func digitsum(num int) int {
    ans := 0
    
    for num>0 {
        ans += num%10
        num = num/10
    }
    
    return ans
}

func max(x int, y int) int {
    if(x>=y){
        return x
    }
    
    return y
}


func min(x int, y int) int {
    if(x<=y){
        return x
    }
    
    return y
}
