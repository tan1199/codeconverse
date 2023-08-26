type point struct{
    row int
    col int
}

func getPoint(r int, c int) point{
    return point{
        row: r,
        col: c,
    }
}

func rangeAddQueries(n int, queries [][]int) [][]int {
    arr := make([][]int, n)
    for i:=0; i<n; i++ {
        arr[i] = make([]int, n)
    }
    
    
    for _, query := range queries{
        start := getPoint(query[0], query[1])
        end := getPoint(query[2], query[3])
        
        flag := end.col+1 < n 
        
        for i:=start.row; i<=end.row; i++{
            arr[i][start.col] += 1
            if(flag){
                arr[i][end.col+1] -= 1
            }
        }
    }
    
    for i:=0; i<n; i++{
        ans := 0
        for j :=0; j<n; j++{
            ans += arr[i][j]
            arr[i][j] = ans
        }
    }
    
    return arr
}

func numInRange(cur point, queries *[][]int) int {
    ans := 0
    
    for i:=0; i<len(*queries);i++{
        start := getPoint((*queries)[i][0], (*queries)[i][1])
        end := getPoint((*queries)[i][2], (*queries)[i][3])
        if(inRange(cur, start, end)){
            ans+=1
        }
    }
    
    return ans
}

func inRange(cur point, start point, end point) bool{
    return start.row<=cur.row && cur.row<=end.row && start.col<=cur.col && cur.col<=end.col
}

func getIndex(row int, col int, n int) int {
    return n*row + col 
}
