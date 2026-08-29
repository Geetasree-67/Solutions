class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s;
        int ans = 0;
        int add = 0;
        
        for(auto c : operations) {
            if(c == "+") {
                add += s.top();
                int temp = s.top();
                s.pop();
                
                add += s.top();
                s.push(temp);
                s.push(add);
                add = 0;  // Reset add after pushing
            }
            else if(c == "D") {
                s.push(s.top() * 2);
            }
            else if(c == "C") {
                s.pop();
            }
            else {
                // It's a number (could be negative)
                s.push(stoi(c));
            }
        }
        
        while(!s.empty()) {
            ans += s.top();
            s.pop();
        }
        return ans;
    }
};