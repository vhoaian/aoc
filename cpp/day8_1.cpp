#include <iostream>
#include <sstream>
#include <map>
#include "utils.h"

using namespace std;

enum Direction {
    LEFT,
    RIGHT
};

struct Navigation {
    string left;
    string right;
};

class Map {
public:
    vector<Direction> directions;
    map<string, Navigation> moves;
    explicit Map(const string& direction) {
        for (auto c : direction) {
            switch (c) {
                case 'L':
                    directions.push_back(Direction::LEFT);
                    break;
                case 'R':
                    directions.push_back(Direction::RIGHT);
                    break;
                default:
                    break;
            }
        }
    }

    void addMove(const string& label, const string& left, const string& right) {
        moves[label] = Navigation { left, right };
    }

    int countStep() {
        string currentLabel = "AAA";
        int count = 0;
        size_t currentDirIdx = 0;
        while (currentLabel != "ZZZ") {
            count++;
            auto dir = this->directions.at(currentDirIdx);
            currentDirIdx = (currentDirIdx + 1) % this->directions.size();
            auto currentMove = this->moves[currentLabel];
            switch (dir) {
                case Direction::LEFT:
                    currentLabel = currentMove.left;
                    break;
                case Direction::RIGHT:
                    currentLabel = currentMove.right;
                    break;
                default:
                    break;
            }
        }
        return count;
    }

    string to_string() {
        ostringstream ss;
        ss << "Directions = ";
        for (auto d : this->directions) {
            ss << d << " ";
        }
        ss << "Moves = " << endl;
        for (const auto& move : this->moves) {
            ss << move.first << " (" << move.second.left << ", " << move.second.right << ")" << endl;
        }

        return ss.str();
    }
};

int main() {
    auto inp = getInput("inputs/day8_1_2.inp");
    Map final_map(inp[0]);
    inp.erase(inp.begin(), inp.begin() + 2);
    for (const auto& line : inp) {
        auto par = line.find('(');
        auto comma = line.find(',');
        final_map.addMove(line.substr(0, 3), line.substr(par + 1, 3), line.substr(comma + 2, 3));
    }

    cout << final_map.countStep();

    return 0;
}
