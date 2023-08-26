func totalFruit(fruits []int) int {
    
    start := 0
    end := 0
    ans := 0

    basket := make(map[int]int, 0)

    for ;end<len(fruits); {
        cur := fruits[end]
        if _, ok := basket[cur]; ok || len(basket)<2{
            if(ok){
                basket[cur] += 1
            } else {
                basket[cur] = 1
            }
        } else {
            for ;len(basket)==2; {
                basket[fruits[start]] -= 1

                if(basket[fruits[start]] == 0){
                    delete(basket, fruits[start])
                }
                start += 1
            }
            basket[cur] = 1
        }
        end += 1
        ans = max(ans, end-start)

        // fmt.Println(start, end, basket, len(basket))
    }

    return ans
}



func max(a int, b int) int {
    if(a>b){
        return a
    }
    return b
}
