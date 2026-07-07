class StockSpanner {
private:
    vector<pair<int, int>> st;
    int i = 0;
public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        int span = 1;
        while (!st.empty() and st.back().first <= price) {
            span += st.back().second;
            st.pop_back();
        }

        st.push_back({price, span});
        return span;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */