#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>

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

vector<vector<int>> dists(const vector<string>& grid,
                          const vector<pair<int, int>>& starts) {
    const int row_num = grid.size();
    const int col_num = grid[0].size();
    vector<vector<int>> min_dist(row_num, vector<int>(col_num, -1));
    queue<pair<int, int>> frontier;
    for (const auto& [r, c] : starts) {
        min_dist[r][c] = 0;
        frontier.push({r, c});
    }
    while (!frontier.empty()) {
        pair<int, int> curr = frontier.front();
        frontier.pop();
        for (const auto& [nr, nc] : neighbors4(curr, row_num, col_num)) {
            if (grid[nr][nc] != '#' && min_dist[nr][nc] == -1) {
                min_dist[nr][nc] = min_dist[curr.first][curr.second] + 1;
                frontier.push({nr, nc});
            }
        }
    }
    return min_dist;
}

int main() {
    vector<string> grid;
    string row;
    while (cin >> row) {
        grid.push_back(row);
    }
    const int row_num = grid.size();
    const int col_num = grid[0].size();

    vector<pair<int, int>> starts;
    for (int r = 0; r < row_num; r++) {
        if (r == 0 || r == row_num - 1) {
            for (int c = 0; c < col_num; c++) {
                if (grid[r][c] == '.') {
                    starts.push_back({r, c});
                }
            }
        } else {
            for (int c : vector<int>{0, col_num - 1}) {
                if (grid[r][c] == '.') {
                    starts.push_back({r, c});
                }
            }
        }
    }

    if (!starts.empty()) {
        vector<vector<int>> min_dist(dists(grid, starts));
        int max_dist = 0;
        for (int r = 0; r < row_num; r++) {
            for (int c = 0; c < col_num; c++) {
                if (grid[r][c] == 'P') {
                    max_dist = max(max_dist, min_dist[r][c]);
                }
            }
        }
        printf("min dist to fill all Ps: %i\n", max_dist);
    }

    vector<vector<vector<int>>> p_dists;
    for (int r = 0; r < row_num; r++) {
        for (int c = 0; c < col_num; c++) {
            if (grid[r][c] == 'P') {
                p_dists.push_back(dists(grid, {{r, c}}));
            }
        }
    }

    int best_time = INT32_MAX;
    for (int r = 0; r < row_num; r++) {
        for (int c = 0; c < col_num; c++) {
            if (grid[r][c] == '.') {
                int time_sum = 0;
                for (const vector<vector<int>>& d : p_dists) {
                    time_sum += d[r][c];
                }
                best_time = min(best_time, time_sum);
            }
        }
    }
    printf("sum of times for best digging pt: %i\n", best_time);
}
