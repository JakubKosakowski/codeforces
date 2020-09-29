#include <bits/stdc++.h>

using namespace std;

bool myfunction(string i, string j) {
    return i < j;
}

int main()
{
    int n;
    vector<string> v;

    cin >> n;

    n += 1;

    while (n--) {
        string s;

        getline(cin, s);
        v.push_back(s);
    }
    sort(v.begin(), v.end(), myfunction);
    int ans = 0;
    string a = v[0];

    for (int i = 1; i < v.size(); ++i) {
        if (a != v[i]) {
            a = v[i];
            ++ans;
        }
        else {
            continue;
        }
    }

    cout << ans << endl;
    return 0;
}
