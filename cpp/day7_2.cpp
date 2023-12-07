#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <unordered_map>
#include "utils.h"

using namespace std;

enum CardsType {
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIR,
    THREE_OF_A_KIND,
    FULL_HOUSE,
    FOUR_OF_A_KIND,
    FIVE_OF_A_KIND
};

enum Card {
    CARD_J,
    CARD_2,
    CARD_3,
    CARD_4,
    CARD_5,
    CARD_6,
    CARD_7,
    CARD_8,
    CARD_9,
    CARD_T,
    CARD_Q,
    CARD_K,
    CARD_A
};

char findMostFrequentChar(const string& str) {
    unordered_map<char, int> charCount;
    for (char c : str) {
        charCount[c]++;
    }
    char mostFrequentChar = '\0';
    int maxCount = 0;
    for (const auto& pair : charCount) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mostFrequentChar = pair.first;
        }
    }

    return mostFrequentChar;
}

class Hand {
public:
    vector<Card> cards;
    CardsType type;
    long long amount;
    Hand(string cardsInStr, long long amount) {
        for (auto c : cardsInStr) {
            Card card = Card::CARD_A;
            switch (c) {
                case '2':
                    card = Card::CARD_2;
                    break;
                case '3':
                    card = Card::CARD_3;
                    break;
                case '4':
                    card = Card::CARD_4;
                    break;
                case '5':
                    card = Card::CARD_5;
                    break;
                case '6':
                    card = Card::CARD_6;
                    break;
                case '7':
                    card = Card::CARD_7;
                    break;
                case '8':
                    card = Card::CARD_8;
                    break;
                case '9':
                    card = Card::CARD_9;
                    break;
                case 'T':
                    card = Card::CARD_T;
                    break;
                case 'J':
                    card = Card::CARD_J;
                    break;
                case 'Q':
                    card = Card::CARD_Q;
                    break;
                case 'K':
                    card = Card::CARD_K;
                    break;
                default:
                    break;
            }
            cards.push_back(card);
        }

        this->amount = amount;
        this->type = CardsType::FIVE_OF_A_KIND;

        int countJ = count(cardsInStr.begin(), cardsInStr.end(), 'J');

        string anotherStr(cardsInStr);
        cardsInStr.erase(remove(cardsInStr.begin(), cardsInStr.end(), 'J'), cardsInStr.end());

        auto mostFreq = findMostFrequentChar(cardsInStr);

        if (mostFreq != '\0' && countJ > 0) {
            replace(anotherStr.begin(), anotherStr.end(), 'J', mostFreq);
        }

        cardsInStr = anotherStr;

        sort(cardsInStr.begin(), cardsInStr.end());

        vector<int> pos;
        pos.push_back(0);
        for (int i = 1; i < cardsInStr.length(); i++) {
            if (cardsInStr[i] != cardsInStr[i-1]) {
                pos.push_back(i);
            }
        }

        switch (pos.size()) {
            case 5:
                this->type = CardsType::HIGH_CARD;
                break;
            case 4:
                this->type = CardsType::ONE_PAIR;
                break;
            case 3:
                for (int i = 0; i < cardsInStr.length() - 2; i++) {
                    if ((cardsInStr[i] == cardsInStr[i+1]) and (cardsInStr[i] == cardsInStr[i+2])) {
                        this->type = CardsType::THREE_OF_A_KIND;
                        break;
                    }
                }
                if (this->type != CardsType::THREE_OF_A_KIND) {
                    this->type = CardsType::TWO_PAIR;
                }
                break;
            case 2:
                for (int i = 0; i < cardsInStr.length() - 3; i++) {
                    if ((cardsInStr[i] == cardsInStr[i+1])
                        and (cardsInStr[i] == cardsInStr[i+2])
                        and (cardsInStr[i] == cardsInStr[i+3])) {
                        this->type = CardsType::FOUR_OF_A_KIND;
                        break;
                    }
                }
                if (this->type != CardsType::FOUR_OF_A_KIND) {
                    this->type = CardsType::FULL_HOUSE;
                }
                break;
            default:
                this->type = CardsType::FIVE_OF_A_KIND;
                break;
        }
    }

    string to_string() {
        ostringstream ss;
        ss << "Cards = ";
        for (auto c : cards) {
            ss << c << " ";
        }
        ss << "Type = " << type << " Amount = " << amount;

        return ss.str();
    }

    bool operator==(const Hand& other) {
        if (this->type == other.type) {
            for (int i = 0; i < this->cards.size(); i++) {
                if (this->cards[i] != other.cards[i]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    bool operator>(Hand other) {
        if (this->type > other.type) {
            return true;
        } else if (this->type == other.type) {
            for (int i = 0; i < this->cards.size(); i++) {
                if (this->cards[i] > other.cards[i]) {
                    return true;
                } else if (this->cards[i] < other.cards[i]) {
                    return false;
                }
            }
            return false;
        }
        return false;
    }

    bool operator<(const Hand& other) {
        return (*this != other) and !(*this > other);
    }

    bool operator!=(const Hand& other) {
        return !(*this == other);
    }

    bool operator<=(const Hand& other) {
        return (*this == other) or !(*this < other);
    }

    bool operator>=(const Hand& other) {
        return (*this == other) or !(*this > other);
    }
};

Hand parseToHand(string thing) {
    istringstream ss(thing);

    string cards;
    int amount;
    ss >> cards >> amount;

    return Hand(cards, amount);
}

int main() {
    auto inp = getInput("inputs/day7_1_2.inp");
    vector<Hand> hands;
    for (auto line : inp) {
        auto hand = parseToHand(line);
        hands.push_back(hand);
    }

    sort(hands.begin(), hands.end());

    long long sum = 0;
    for (int i = 0; i < hands.size(); i++) {
//        cout << hands[i].to_string() << endl;
        sum += (i + 1) * hands.at(i).amount;
    }

    cout << sum;

    return 0;
}
