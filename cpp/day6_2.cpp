#include <iostream>
#include <sstream>
#include "utils.h"

using namespace std;

class Race {
public:
    long long time;
    long long distance;
    Race(long long time, long long distance) : time(time), distance(distance) {}

    string to_string() {
        ostringstream ss;
        ss << "Time = " << time << ", Distance = " << distance;
        return ss.str();
    }

    int countNumOfWaysYouCanWin() {
        long long count = 0;
        for (long long i = 1; i < time; i++) {
            long long distance = (time - i) * i;
            if (distance > this->distance) {
                count++;
            }
        }
        return count;
    }
};

long long parseToNumber(string thing) {
    auto found = thing.find(":");
    auto numbers = thing.substr(found + 1);
    istringstream ss(numbers);
    vector<long long> result;

    ostringstream number;
    string temp;
    while (ss >> temp) {
        number << temp;
    }
    return stoll(number.str());
}

int main() {
    auto inp = getInput("inputs/day6_1_2.inp");
    auto time = parseToNumber(inp[0]);
    auto distance = parseToNumber(inp[1]);
    auto race = Race(time, distance);

    cout << race.countNumOfWaysYouCanWin();
    return 0;
}
