#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

#include "debugging.hpp"

using namespace std;

vector<pair<int, int>> neighbors4(const pair<int, int>& pt, int r_max, int c_max) {
    vector<pair<int, int>> todo{{pt.first + 1, pt.second},
                                {pt.first - 1, pt.second},
                                {pt.first, pt.second + 1},
                                {pt.first, pt.second - 1}};
    vector<pair<int, int>> ret;
    for (const auto& [r, c] : todo) {
        if (0 <= r && r < r_max && 0 <= c && c < c_max) {
            ret.push_back({r, c});
        }
    }
    return ret;
}

int main() {
    string row;
    vector<string> grid;
    while (cin >> row) {
        grid.push_back(row);
    }

    const int row_num = grid.size();
    const int col_num = grid[0].size();
    pair<int, int> start{-1, -1};
    vector<pair<int, int>> poi;
    map<char, vector<pair<int, int>>> herbs;
    for (int r = 0; r < row_num; r++) {
        for (int c = 0; c < col_num; c++) {
            if (grid[r][c] == '.' && r == 0 && start.first == -1) {
                start = {r, c};
                poi.push_back({r, c});
            }
            if ('A' <= grid[r][c] && grid[r][c] <= 'Z') {
                herbs[grid[r][c]].push_back({r, c});
                poi.push_back({r, c});
            }
        }
    }

    assert(start != make_pair(-1, -1));

    map<pair<int, int>, map<pair<int, int>, int>> min_dists;
    for (const pair<int, int>& pt : poi) {
        map<pair<int, int>, int>& this_best = min_dists[pt];
        this_best[pt] = 0;
        std::queue<pair<int, int>> frontier;
        frontier.push(pt);
        while (!frontier.empty()) {
            pair<int, int> curr = frontier.front();
            frontier.pop();
            const int n_dist = this_best[curr] + 1;
            for (const auto& [nr, nc] : neighbors4(curr, row_num, col_num)) {
                const char cell = grid[nr][nc];
                if (cell != '#' && cell != '~' && !this_best.count({nr, nc})) {
                    this_best[{nr, nc}] = n_dist;
                    frontier.push({nr, nc});
                }
            }
        }
    }

    vector<char> ind_to_herb;
    for (const auto& h : herbs) {
        ind_to_herb.push_back(h.first);
    }

    vector<vector<vector<int>>> dp(1 << (int)herbs.size(),
                                   vector<vector<int>>(herbs.size()));
    for (int i = 0; i < dp.size(); i++) {
        for (int j = 0; j < herbs.size(); j++) {
            dp[i][j] = vector<int>(herbs[ind_to_herb[j]].size(), INT32_MAX);
        }
    }

    int i = 0;
    for (const auto& [h, pts] : herbs) {
        for (int j = 0; j < pts.size(); j++) {
            dp[1 << i][i][j] = min_dists[start][pts[j]];
        }
        i++;
    }

    for (int ss = 0; ss < dp.size(); ss++) {
        if ((ss & (ss - 1)) == 0) {
            continue;
        }

        for (int i = 0; i < herbs.size(); i++) {
            if ((ss & (1 << i)) == 0) {
                continue;
            }
            int prev_ss = ss & ~(1 << i);
            for (int prev_i = 0; prev_i < herbs.size(); prev_i++) {
                if ((prev_ss & (1 << prev_i)) == 0) {
                    continue;
                }

                for (int j = 0; j < herbs[ind_to_herb[i]].size(); j++) {
                    const pair<int, int>& pt = herbs[ind_to_herb[i]][j];
                    for (int prev_j = 0; prev_j < herbs[ind_to_herb[prev_i]].size();
                         prev_j++) {
                        const pair<int, int>& prev_pt =
                            herbs[ind_to_herb[prev_i]][prev_j];
                        dp[ss][i][j] =
                            min(dp[ss][i][j],
                                dp[prev_ss][prev_i][prev_j] + min_dists[prev_pt][pt]);
                    }
                }
            }
        }
    }

    int best = INT32_MAX;
    for (int i = 0; i < herbs.size(); i++) {
        for (int j = 0; j < herbs[ind_to_herb[i]].size(); j++) {
            const pair<int, int>& end = herbs[ind_to_herb[i]][j];
            best = min(best, dp.back()[i][j] + min_dists[end][start]);
        }
    }

    cout << best << endl;
}
