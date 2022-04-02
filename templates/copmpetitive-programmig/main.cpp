#include <bits/stdc++.h>

#define int long long
#define x first
#define y second
#define getbit(x, i) (((x) >> (i)) & 1)
using namespace std;
typedef pair<int, int> pii;
#define hashset unordered_set
#define hashmap unordered_map
#define unify(arr) arr.resize(unique(arr.begin(), arr.end()) - arr.begin())
#define getbit(x, i) (((x) >> (i)) & 1)

/** Interface */

inline int readInt();

inline int readUInt();

inline void readWord(char *s);

inline int fast_readchar();  // you may use readchar() instead of it

inline void writeInt(int x);

inline void fast_writechar(int x);  // you may use putchar() instead of it
inline void writeWord(const char *s);

inline void fast_flush();

struct hash_pair {
    template<class T1, class T2>
    size_t operator()(const pair<T1, T2> &p) const {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};

template<typename T>
vector<T> readvector(size_t sz) {
    vector<T> res(sz);
    for (size_t i = 0; i < sz; ++i) { cin >> res[i]; }
    return res;
}

template<typename T, typename U>
std::ostream &operator<<(std::ostream &out, const std::pair<T, U> &p) {
    out << p.first << " " << p.second;
    return out;
}

template<typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v) {
    std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, " "));
    return out;
}

inline int binPow(int x, int deg, int mod) {
    int ans = 1;
    for (int i = sizeof(deg) * CHAR_BIT - 1; i >= 0; i--) {
        ans *= ans;
        ans %= mod;
        if (getbit(deg, i)) ans *= x;
        ans %= mod;
    }
    return ans;
}

int n;

int gcd(int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

/** Interface */

// ====================== END ======================
const int MAXN = 4e5 + 10;
const int MOD = 1e9 + 7;
const int INF = 1e18;

typedef pair<int, int> vec;

int operator*(vec A, vec B) { return A.x * B.x + A.y * B.y; }

int operator%(vec A, vec B) { return A.x * B.y - A.y * B.x; }

vec operator*(vec A, int c) { return {A.x * c, A.y * c}; }

vec operator-(vec A, vec B) { return {A.x - B.x, A.y - B.y}; }

vec operator+(vec A, vec B) { return {A.x + B.x, A.y + B.y}; }

vector<vec> D = {{-1, 0},
                 {1,  0},
                 {0,  -1},
                 {0,  1}};

long long fact[MAXN], inv_fact[MAXN];

void precalc() {
    fact[0] = 1;
    for (int i = 1; i < MAXN; i++) { fact[i] = (fact[i - 1] * i) % MOD; }
    inv_fact[MAXN - 1] = binPow(fact[MAXN - 1], MOD - 2, MOD);
    for (int i = MAXN - 1; i > 0; i--) { inv_fact[i - 1] = (inv_fact[i] * i) % MOD; }
}

long long c(int n, int k) {
    if (k < 0 || k > n || n < 0) return 0;
    return ((fact[n] * inv_fact[k]) % MOD * inv_fact[n - k]) % MOD;
}

vector<int> graph[MAXN];

int total = 0;

int generate(int left, int right, string_view &s, std::vector<int> &arr, std::vector<int> &b) {

    if (right - left <= 1) {
        return 0;
    }
    int m = (left + right) / 2;
    int prefix = generate(left, m, s, arr, b);
    if (prefix == -1) {
        return -1;
    }

    prefix = generate(m, right, s, arr, b);
    if (prefix == -1) {
        return -1;
    }

    int i = left, j = m, k = left;
    int cnt = 0;
    while (i < m && j < right) {
        if (s.empty()) return -1;
        if (s[0] == '0') {
            graph[arr[i]].push_back(arr[j]);
            b[k++] = arr[i++];
        } else {
            graph[arr[j]].push_back(arr[i]);
            b[k++] = arr[j++];
        }
        s = s.substr(1);
        ++cnt;
    }
    while (i < m) {
        b[k++] = arr[i++];
    }
    while (j < right) {
        b[k++] = arr[j++];
    }
    copy(b.begin() + left, b.begin() + right, arr.begin() + left);
    total += cnt;
    return cnt;
}


inline void solve() {
    int n;
    cin >> n;
    auto a = readvector<int>(n);
    bool inc = true;
    for (int i = 1; i < n; i++) {
        inc &= (a[i] > a[i - 1]);
    }
    if (inc && n % 2 == 1) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
    }
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
//        cout << "Case #" << i << ": ";
        solve();
    }
    fast_flush();
    return 0;
}

/** Read */

static const int buf_size = 4096;

inline int fast_readchar() {
    static char buf[buf_size];
    static int len = 0, pos = 0;
    if (pos == len) pos = 0, len = fread(buf, 1, buf_size, stdin);
    if (pos == len) return -1;
    return buf[pos++];
}

inline int readUInt() {
    int c = fast_readchar(), x = 0;
    while (c <= 32) c = fast_readchar();
    while ('0' <= c && c <= '9') x = x * 10 + c - '0', c = fast_readchar();
    return x;
}

inline int readInt() {
    int s = 1, c = fast_readchar();
    int x = 0;
    while (c <= 32) c = fast_readchar();
    if (c == '-') s = -1, c = fast_readchar();
    while ('0' <= c && c <= '9') x = x * 10 + c - '0', c = fast_readchar();
    return x * s;
}

inline void readWord(char *s) {
    int c = fast_readchar();
    while (c <= 32) c = fast_readchar();
    while (c > 32) *s++ = c, c = fast_readchar();
    *s = 0;
}

/** Write */

static int write_pos = 0;
static char write_buf[buf_size];

inline void fast_writechar(int x) {
    if (write_pos == buf_size) fwrite(write_buf, 1, buf_size, stdout), write_pos = 0;
    write_buf[write_pos++] = x;
}

inline void fast_flush() {
    if (write_pos) fwrite(write_buf, 1, write_pos, stdout), write_pos = 0;
}

inline void writeInt(int x) {
    if (x < 0) fast_writechar('-'), x = -x;

    char s[24];
    int n = 0;
    while (x || !n) s[n++] = '0' + x % 10, x /= 10;
    while (n--) fast_writechar(s[n]);
}

inline void writeWord(const char *s) {
    while (*s) fast_writechar(*s++);
}
