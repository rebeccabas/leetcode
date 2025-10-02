class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        int empty = numBottles;
        while (empty >= numExchange) {
            empty = empty - numExchange + 1;
            numExchange++;
            ans++;
        }
        return ans;
    }
};
