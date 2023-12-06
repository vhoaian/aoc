#include <iostream>
#include <sstream>
#include "utils.h"

using namespace std;

class Race {
public:
    int time;
    int distance;
    Race(int time, int distance) : time(time), distance(distance) {}

    string to_string() {
        ostringstream ss;
        ss << "Time = " << time << ", Distance = " << distance;
        return ss.str();
    }

    int countNumOfWaysYouCanWin() {
        int count = 0;
        for (int i = 1; i < time; i++) {
            int distance = (time - i) * i;
            if (distance > this->distance) {
                count++;
            }
        }
        return count;
    }
};

vector<int> parseToInts(string thing) {
    auto found = thing.find(":");
    auto numbers = thing.substr(found + 1);
    istringstream ss(numbers);
    vector<int> result;

    int number;
    while (ss >> number) {
        result.push_back(number);
    }
    return result;
}

int main() {
    auto inp = getInput("inputs/day6_1_2.inp");
    vector<Race> races;
    auto times = parseToInts(inp[0]);
    auto distances = parseToInts(inp[1]);

    for (int i = 0; i < times.size(); i++) {
        auto race = Race(times.at(i), distances.at(i));
        races.push_back(race);
    }

    int product = 1;
    for (auto i : races) {
        product *= i.countNumOfWaysYouCanWin();
    }

    cout << product << endl;
    return 0;
}
