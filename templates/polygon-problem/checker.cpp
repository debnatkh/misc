/**
 * Author: Deb Natkh Maxim (debnatkh@gmail.com)
 * Date: 02.03.2019
 */

#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

int n;
vector<int> message_counts;

inline int readAndCheckAnswer(InStream& in) {
    int result = in.readInt(-1, n * 100);
    if(result == -1)
        return result;

    vector<int> messages_can_send = message_counts;
    vector<bool> got_message(n, false);
    got_message[0] = true;

    for (int i = 0; i < result; i++) {
        int from = in.readInt(1, n) - 1;
        int to = in.readInt(1, n) - 1;
        
        if (messages_can_send[from] <= 0)
            in.quitf(_wa, "Student %d can not send more than %d messages", from + 1, message_counts[from]);
        if (!got_message[from])
            in.quitf(_wa, "Student %d send message but does not already know the news", from + 1);
        if (from == to)
            in.quitf(_wa, "Student %d can not send messages to himself", from + 1);
        
        got_message[to] = true;
        messages_can_send[from]--;
    }

    for (int i = 0; i < n; i++)
        if (!got_message[i])
            in.quitf(_wa, "Not all students got the message");

    return result;
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    n = inf.readInt();
    message_counts.resize(n);
    for(int i = 0; i < n; i++)
        message_counts[i] = inf.readInt();

    int ja = readAndCheckAnswer(ans);
    int pa = readAndCheckAnswer(ouf);

    if(ja != -1 && pa == -1)
        quitf(_wa, "Jury has the answer but participant has not");
    if(ja == -1 && pa != -1)
        quitf(_fail, "Participant has the answer but jury has not");

    quitf(_ok, "n=%d", n);
}