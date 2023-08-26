class TimeMap {

    HashMap<String, ArrayList<Node>> map;
    
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        Node newNode = new Node(timestamp, value);
        if(this.map.containsKey(key)){
            map.get(key).add(newNode);
        } else {
            ArrayList<Node> arr = new ArrayList<>();
            arr.add(newNode);
            map.put(key, arr);
        }
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)) return "";
        
        ArrayList<Node> list = map.get(key);
        int low = 0;
        int high = list.size()-1;
        
        while(low<high){
            int mid = (low + high + 1)/2;
            if(timestamp == list.get(mid).timestamp) return list.get(mid).value;
            else if(timestamp < list.get(mid).timestamp) high = mid -1;
            else low = mid;
        }
        
        return (0<=low && low<list.size() && list.get(low).timestamp<=timestamp) ? list.get(low).value : "";
        
    }
}



class Node{
    int timestamp;
    String value;
    
    Node(int timestamp, String key){
        this.timestamp = timestamp;
        this.value = key;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
