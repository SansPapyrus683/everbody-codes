#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

constexpr int P3_THRESH = 6;

/** sauce: https://usaco.guide/gold/dsu?lang=cpp#implementation */
class DisjointSets {
   private:
    vector<int> parents;
    vector<int> sizes;
    vector<int> costs;

   public:
    DisjointSets(int size) : parents(size), sizes(size, 1), costs(size) {
        for (int i = 0; i < size; i++) {
            parents[i] = i;
        }
    }

    int find(int x) { return parents[x] == x ? x : (parents[x] = find(parents[x])); }

    bool unite(int x, int y, int cost) {
        int x_root = find(x);
        int y_root = find(y);
        if (x_root == y_root) {
            return false;
        }

        if (sizes[x_root] < sizes[y_root]) {
            swap(x_root, y_root);
        }
        sizes[x_root] += sizes[y_root];
        costs[x_root] += costs[y_root] + cost;
        parents[y_root] = x_root;
        return true;
    }

    int get_size(int x) { return sizes[find(x)]; }

    int get_cost(int x) { return costs[find(x)]; }
};

int l1_dist(const pair<int, int>& p1, const pair<int, int>& p2) {
    return abs(p1.first - p2.first) + abs(p1.second - p2.second);
}

int main() {
    vector<pair<int, int>> points;
    string row;
    for (int r = 0; cin >> row; r++) {
        for (int c = 0; c < row.size(); c++) {
            if (row[c] == '*') {
                points.push_back({r, c});
            }
        }
    }

    vector<pair<int, pair<int, int>>> links;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            const int dist = l1_dist(points[i], points[j]);
            links.push_back({dist, {i, j}});
        }
    }
    sort(links.begin(), links.end());

    DisjointSets dsu(points.size());
    int min_cost = 0;
    for (const auto& [dist, edge] : links) {
        min_cost += dist * dsu.unite(edge.first, edge.second, dist);
    }

    const int size = min_cost + points.size();
    printf("size of the total constellation (p1 & p2): %i\n", size);

    dsu = DisjointSets(points.size());
    for (const auto& [dist, edge] : links) {
        if (dist >= P3_THRESH) {
            break;
        }
        dsu.unite(edge.first, edge.second, dist);
    }

    map<int, int> constellations;
    for (int i = 0; i < points.size(); i++) {
        constellations[dsu.find(i)] = dsu.get_cost(i) + dsu.get_size(i);
    }
    if (constellations.size() < 3) {
        return 9;
    }

    vector<int> all_sizes;
    for (const pair<int, int> c : constellations) {
        all_sizes.push_back(c.second);
    }
    sort(all_sizes.begin(), all_sizes.end(), greater<int>());

    long long prod = 1;
    for (int i = 0; i < 3; i++) {
        prod *= all_sizes[i];
    }
    printf("product of 3 largest constellations (p3): %lld\n", prod);
}
