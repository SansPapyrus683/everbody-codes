#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>

using namespace std;

const vector<int> DOTS{1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101};
constexpr int MAX_DIFF = 100;

int main() {
    vector<int> balls;
    int x;
    int up_to = 0;
    while (cin >> x) {
        balls.push_back(x);
        up_to = max(up_to, x);
    }

    vector<int> min_dots(up_to + 1, INT32_MAX);
    min_dots[0] = 0;
    for (int d : DOTS) {
        for (int i = d; i <= up_to; i++) {
            if (min_dots[i - d] == INT32_MAX) {
                continue;
            }
            min_dots[i] = min(min_dots[i], min_dots[i - d] + 1);
        }
    }

    long long min_used = 0;
    for (int b : balls) {
        int half = b / 2;
        int this_best = INT32_MAX;
        for (int h1 = half - MAX_DIFF; h1 <= half + MAX_DIFF; h1++) {
            int h2 = b - h1;
            if (abs(h1 - h2) > MAX_DIFF) {
                continue;
            }
            this_best = min(this_best, min_dots[h1] + min_dots[h2]);
        }
        min_used += this_best;
    }

    cout << min_used << endl;
}
