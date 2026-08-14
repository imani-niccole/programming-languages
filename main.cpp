//
//  main.cpp
//  are you smarter than a fifth grader
//
//  Created by Jael Mackell on 10/27/24.
//
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include <atomic>

using namespace std;
void  introdcution()
{
    cout << "***Welcome to ARE YOU SMARTER THAN A FIFTH GRADER!****"<<endl;
    cout << "The rules are simple:)"<<endl;
    cout << "Answer the given question within 15 minutes"<<endl;
}

void getInput(string& answer, atomic<bool>& inputReceived)
{
    getline(cin, answer);
    inputReceived = true; // Mark that input has been received
}

int main()
{
    vector<string> questions =
    {
        "Question one: Crawfish are fish? | True or False: ",
        "Question two: Density describes the mass of an object divided by what? ",
        "Question three: Costa Rica borders two countries. Nicaragua is one of the countries. What is the other? ",
        "Question four: Which of the following is NOT an official language of Switzerland: German, Italian, or Spanish? ",
        "Question five: What is the process of a caterpillar turning into a butterfly called? ",
        "Question six: What is the capital of Australia? ",
        "Question seven: In classical music, what instruments usually comprise a string quartet? ",
        "Question eight: The Tropic of Capricorn lies in which hemisphere? ",
        "Question nine: What are the large rocks that orbit the sun between Mars and Jupiter called? ",
        "Question ten: What is the prefix in the word unnecessary? "
    };

    vector<string> answers(questions.size());

    for (size_t i = 0; i < questions.size(); ++i) {
        cout << questions[i];
        cout << "You have 15 seconds to enter your response: ";

        string answer;
        atomic<bool> inputReceived(false);

        // Start a thread for getting user input
        thread inputThread(getInput, ref(answer), ref(inputReceived));

        // Wait for 30 seconds or until input is received
        auto start = chrono::high_resolution_clock::now();
        while (chrono::duration_cast<chrono::seconds>(chrono::high_resolution_clock::now() - start).count() < 15)
        {
            if (inputReceived)
            {
                break; // Exit if input is received
            }
        }

        // Stop the input thread if time is up
        if (!inputReceived)
        {
            cout << "Time's up! No answer recorded." << endl;
            answers[i] = "No answer"; // Set default response
        }
        else
        {
            cout << "Response received: " << answer << endl;
            answers[i] = answer; // Store the answer
        }

        // Join the thread if it's still running
        if (inputThread.joinable())
        {
            inputThread.join();
        }
    }

    cout << "\nYour answers:\n";
    for (size_t i = 0; i < answers.size(); ++i)
    {
        cout << questions[i] << answers[i] << endl;
    }

    return 0;
}
