#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

constexpr int COL_NUM = 4;

int main() {
    vector<vector<int>> cols(COL_NUM);
    int x;
    int at = 0;
    while (cin >> x) {
        cols[at++ % COL_NUM].push_back(x);
    }

    set<int> vals;
    map<long long, int> seen;
    int i = 0;
    while (vals.empty() || *vals.rbegin() < 2024) {
        vector<int>& curr_col = cols[i % COL_NUM];
        int clapper = curr_col.front();
        curr_col.erase(curr_col.begin());

        vector<int>& next_col = cols[(i + 1) % COL_NUM];
        int end_pos = (clapper - 1) % (2 * next_col.size());
        if (end_pos >= next_col.size()) {
            end_pos = next_col.size() - (end_pos - next_col.size());
        }
        next_col.insert(next_col.begin() + end_pos, clapper);

        string shout;
        for (const vector<int>& col : cols) {
            shout += to_string(col.front());
        }
        long long shout_val = stoll(shout);

        if (seen.count(shout_val)) {
            vals.erase(seen[shout_val]);
        }
        seen[shout_val]++;
        vals.insert(seen[shout_val]);

        i++;
    }

    for (const auto& [k, v] : seen) {
        if (v == 2024) {
            cout << k * i << endl;
            break;
        }
    }
}
