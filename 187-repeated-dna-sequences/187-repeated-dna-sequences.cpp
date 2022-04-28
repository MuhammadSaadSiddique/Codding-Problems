
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> map;
        vector<string> res;
        
        if(s.size() < 10)    return res;
        
        for(int i=0; i<s.size() - 9; i++){
            map[s.substr(i,10)]++;
        }
        
        for(auto el:map){
            //cout<< el.first<< " "<< el.second<< endl;
            if(el.second > 1)
                res.push_back(el.first);
        }
        
        return res;
    }
};