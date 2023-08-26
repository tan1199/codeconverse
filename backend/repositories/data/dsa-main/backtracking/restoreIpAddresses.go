var ans = make([]string, 0) 

func helper(index int, s *string, ip string, byteCount int) {

    if(byteCount == 4 && index == len(*s)){
        ans = append(ans, ip[1:])
    }

    if(byteCount>=4){
        return
    }


    cur := 0
    start :=  index

    for index<len(*s) && ((cur*10 + int((*s)[index]) - 48) <= 255)  {
        cur = cur*10 + int((*s)[index]) - 48
        index += 1
        helper(index, s, ip + "." + (*s)[start:index], byteCount+1)
        if(cur == 0){
            break
        }
    }
}


func restoreIpAddresses(s string) []string {
    ans = make([]string, 0)  
    helper(0, &s, "", 0)
    return ans
}
