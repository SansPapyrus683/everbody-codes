#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const vector<pair<int, int>> SEGS{{0, 0}, {0, 1}, {0, 2}};

int min_power(const pair<int, int>& start, const pair<int, int>& m, int alt) {
    if (alt > m.second) {
        return -1;
    }
    int time = m.second - alt;
    int dx = m.first - time - start.first;
    int dy = m.second - time - start.second;

    if (dx != time) {
        return -1;
    }

    auto ending_dy = [&] (int pow) {
        if (time <= pow) {
            return time;
        } else if (time <= 2 * pow) {
            return pow;
        }
        return pow - (time - 2 * pow);
    };
    for (int p : vector<int>{dx, dy, (dx + dy) / 3}) {
        if (ending_dy(p) == dy) {
            return p;
        }
    }
    return -1;
}

int main() {
    vector<pair<int, int>> meteors;
    int x, y;
    while (cin >> x >> y) {
        meteors.push_back({x, y});
    }

    long long total_ranking = 0;
    for (pair<int, int> m : meteors) {
        if (m.first % 2 == 1) {
            m.first--;
            m.second--;
        }

        vector<pair<int, int>> to_use;
        for (int i = 0; i < SEGS.size(); i++) {
            for (int alt = m.second; alt >= 0; alt--) {
                int mp = min_power(SEGS[i], m, alt);
                if (mp != -1) {
                    to_use.push_back({-alt, mp * (i + 1)});
                    break;
                }
            }
        }

        sort(to_use.begin(), to_use.end());
        total_ranking += to_use.front().second;
    }

    cout << total_ranking << endl;
}
