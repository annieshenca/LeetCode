class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string> empty_str;
        
        for (auto word: words) {
            string code;
            for (auto w: word) {
                code += morse[w - 'a'];
            }
            empty_str.insert(code);
        }
        return empty_str.size();
    }
};
