#include <bits/stdc++.h>

using namespace std;

bool myfunction(int i, int j) {
    return (i < j);
}

int main()
{
    int n;
    set<int> s;

    cin >> n;

    while (n--) {
        string in;

        cin >> in;
        int l = in.length(), d = 0;
        for (int i = 0; i < l; ++i) {
            d = d | (1 << (in[i] - 'a'));
        }
        s.insert(d);
    }

    cout << s.size();

    return 0;
}
