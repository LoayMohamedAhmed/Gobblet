// Gobblet AI Player.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <stack>
#include <utility>
#include <vector>
#include <random>

using namespace std;

struct GobbletNode {
    int len;
    char color;
};

struct PLAYER {
    vector<  pair< stack<GobbletNode>, bool> > player;
    char color;
    PLAYER() : player(3) {
        // Additional initialization if needed
    }
};



// Define the dimensions of the 2D vector
const int rows = 4;
const int cols = 4;


void initialize_game(vector< pair< stack<GobbletNode>, bool>>& player_1, vector<  pair< stack<GobbletNode>, bool>  >& player_2);

void available_click(char c, vector<pair< stack<GobbletNode>, bool>>& player_1,
    vector<pair< stack<GobbletNode>, bool>>& player_2,
    vector<vector<pair< stack<GobbletNode>, bool>>>& board);

void handle_clicks(char c, vector<pair< stack<GobbletNode>, bool>>& player);

bool suggest_cells_case_1(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board);

bool suggest_cells_case_20(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board);


bool suggest_cells_case_21(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board, vector<bool> warning_list);


void off_outer_clicks(vector<pair< stack<GobbletNode>, bool>>& player);

int getRandomNumber();

void show_board_players(PLAYER & player_1, PLAYER& player_2, vector<vector<pair< stack<GobbletNode>, bool>>>& board);

void show_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board);


void show_check_board_players(PLAYER & player_1, PLAYER & player_2, vector<vector<pair< stack<GobbletNode>, bool>>>& board);

void show_check_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board);

bool get_click_from(int &outt, int &index_i, int &index_j);
void get_click_to(int& to_i, int& to_j);

bool check_winning(char c, vector<vector<pair< stack<GobbletNode>, bool>>>& board);
bool check_warning(char c, vector<bool> &warning_list, vector<vector<pair< stack<GobbletNode>, bool>>>& board);


int count_threats(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char c);
int count_blocks(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char c);
float count_pieces(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char player);
float evaluate_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char player);
float minimax(vector<vector<pair< stack<GobbletNode>, bool>>>& board, int depth, bool isMaximizing, bool firstTime, PLAYER & a_i);


vector<int> get_available_AI_move_stack(vector<pair< stack<GobbletNode>, bool>> player);
vector<pair<int, int>> get_available_AI_move_board(char player, vector<vector<pair< stack<GobbletNode>, bool>>>& board);

// initailize board and players
//vector<  pair< stack<GobbletNode>, bool>  > player_1(3);
//vector<  pair< stack<GobbletNode>, bool>  > player_2(3);

PLAYER  player_1;
PLAYER  player_2;
vector<vector<pair< stack<GobbletNode>, bool>>> board(4, vector<pair< stack<GobbletNode>, bool>>(4));  // Create a 2D vector of stacks




int main()
{
    cout << "Hello World!\n";

    // initailize board and players

    player_1.color = 'b';
    player_2.color = 'w';

    initialize_game(player_1.player, player_2.player);



    // Push some values onto each stack in the 2D vector
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            board[i][j].second = 0; // intial can't click
        }
    }

    // makes vector with len(10) 4(rows), 4(cols), 2(diagonal) to flag the warining 
    bool warning_flag = false;
    vector<bool> warning_list(10, false);

    char c = 'b';
    show_board_players(player_1, player_2, board);

    while (1) 
    {
        // to handle AI
        if (c == 'b') 
        {
            float score = minimax(board, 2, true, true, player_1);
            c = 'w';
            show_board_players(player_1, player_2, board);
            continue;
        }
        
        available_click(c, player_1.player, player_2.player, board);

        show_check_board_players(player_1, player_2, board);

        //  TWO CASES (to know which case , use flag to know --> if (true) choose from board
        //                                                       else      out
        // case 1. player select gobblet from board
        // case 2.  player select gobblet from out

        int out = 0;    int from_i = 0;   int from_j = 0;
        bool out_in = get_click_from(out, from_i, from_j);

        if (out_in == true) // player choose from board
        {
            int choosen_len = board[from_i][from_j].first.top().len;
            bool not_lose = suggest_cells_case_1(choosen_len, board);
            if (not_lose == false)
            {
                cout << "GAME OVER";
                return 1;
            }
            
        }
        else  // player choose from out
        {
            // in this case , two scenario
            // first (no warning) --> the player only have empty cell
            // second (with warning) --> player have empty cell  and warning cells to gobble up
            int choosen_len;
            if (c == 'b')
            {
                choosen_len = player_1.player[out].first.top().len;
            }
            else choosen_len = player_2.player[out].first.top().len;
            if (warning_flag == false) 
            {
                bool not_lose = suggest_cells_case_20(choosen_len, board);
                if (not_lose == false)
                {
                    cout << "GAME OVER";
                    return 1;
                }
            }
            else
            {
                bool not_lose = suggest_cells_case_21(choosen_len, board, warning_list);
                if (not_lose == false)
                {
                    cout << "GAME OVER";
                    return 1;
                }
            }

        }

        show_check_board(board);
        int to_i = 0;
        int to_j = 0;

        get_click_to(to_i, to_j);

        GobbletNode temp_gobblet;
        if (out_in == 1) // player choose from board
        {
            temp_gobblet = board[from_i][from_j].first.top();
            board[from_i][from_j].first.pop();
        }
        else 
        {
            if (c == 'b') 
            {
                temp_gobblet = player_1.player[out].first.top();
                player_1.player[out].first.pop();
            }
            else 
            {
                temp_gobblet = player_2.player[out].first.top();
                player_2.player[out].first.pop();
            }
            
        }

        board[to_i][to_j].first.push(temp_gobblet);

        show_board_players(player_1, player_2, board);

        // check if any player win or not
        bool player1_win = check_winning('b', board);
        bool player2_win = check_winning('w', board);


        // if two players win --> we consider the player who play prevois step is the winner ,not current player
        if(c == 'b')
        {
            if (player2_win)
            {
                cout << "player 2  is the winner";
                break;
            }
            else if(player1_win)
            {
                cout << "player 1  is the winner";
                break;
            }
        }
        else 
        {
            if (player1_win)
            {
                cout << "player 1  is the winner";
                break;
            }
            else if (player2_win)
            {
                cout << "player 2  is the winner";
                break;
            }
        }
        

        // check the next player has warning or not                               
        //  so we check if current player is player1 --> check warning in player 2
         
        if (c == 'b') // check warning in player with color w
        {
            warning_flag = check_warning('w', warning_list, board);
        }
        else
        {
            warning_flag = check_warning('b', warning_list, board);
        }


        if (c == 'b')c = 'w';
        else c = 'b';

    }
    
    // Print the visual representation of the 2D matrix of stacks
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << "+---";
        }
        cout << "+" << std::endl;

        for (int j = 0; j < cols; ++j) {
            cout << "| " << board[i][j].second << " ";
            //board[i][j].first.pop();
        }
        cout << "|" << std::endl;
    }

    // Print the bottom border of the 2D matrix
    for (int j = 0; j < cols; ++j) {
        cout << "+---";
    }
    cout << "+" << std::endl;

    cout << "Hello World!\n";
    

}



void initialize_game(vector<pair< stack<GobbletNode>, bool>> &player_1, vector<pair<stack<GobbletNode>,bool>>&player_2)
{
    vector<char> charVector = { 'b', 'w' };


    stack<int> myStack;
    //vector< stack< GobbletNode > > vectorOfStacks(3);
    
    bool check = true;
    
    for (int j = 0; j < 2; j++) 
    {
        stack< GobbletNode >  tempstack;
        for (int i = 1; i <= 4; i++)
        {
            //cout << i;
            //  size   color 
            GobbletNode myNode = { i, charVector[j] };
            tempstack.push(myNode);
        }
        pair< stack<GobbletNode>, bool> tempPair = { tempstack , false };
        if(check) // to insert in player_1
        {
            for (int k = 0; k < 3; k++)
            {
                player_1[k] = tempPair;
            }
            check = !check;
        }
        else
        {
            for (int k = 0; k < 3; k++)
            {
                player_2[k] = tempPair;
            }
        }

    }
    

}

void available_click(char c, vector<pair< stack<GobbletNode>, bool>>& player_1,
                        vector<pair< stack<GobbletNode>, bool>>& player_2,
                        vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    // access the available click in board
    for (int i = 0; i < 4; i++) 
    {
        for (int j = 0; j < 4; j++) 
        {

            // check on each cell if the cell is empty or have same color c
            if(board[i][j].first.size() != 0 && board[i][j].first.top().color == c)
            {
                board[i][j].second = 1; // make it clickable
            }
            else 
            {
                board[i][j].second = 0;
            }
        }
    }
    // change a button_click in two players
    handle_clicks(c, player_1);
    handle_clicks(c, player_2);

}

void handle_clicks(char c, vector<pair< stack<GobbletNode>, bool>>& player) 
{
    for (int i = 0; i < 3; i++)
    {
        if (player[i].first.size() != 0 && player[i].first.top().color == c)
        {
            player[i].second = 1;
        }
        else
        {
            player[i].second = 0;
        }
    }
}


// in board
bool suggest_cells_case_1(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board) 
{
    bool check = false;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            // check on each cell if the cell is empty or have same color c
            //cout << board[i][j].first.size();
            if (board[i][j].first.size() == 0 || board[i][j].first.top().len < choosen_size)
            {
                board[i][j].second = 1; //  suggest it
                check = true;
            }
            else
            {
                board[i][j].second = 0;
            }
        }
    }

    off_outer_clicks(player_1.player);
    off_outer_clicks(player_2.player);

    return check; // if check still equal false then player have no play (player loose ---> game over)
}


// out board without warning
bool suggest_cells_case_20(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    bool check = false;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            // check on each cell if the cell is empty 
            if (board[i][j].first.size() == 0)
            {
                board[i][j].second = 1; //  suggest it
                check = true;
            }
            else
            {
                board[i][j].second = 0;
            }
        }
    }

    off_outer_clicks(player_1.player);
    off_outer_clicks(player_2.player);

    return check; // if check still equal false then player have no play (player loose ---> game over)
}


// out board with warning
bool suggest_cells_case_21(int choosen_size, vector<vector<pair< stack<GobbletNode>, bool>>>& board, vector<bool> warning_list)
{
    int itr = 0;
    bool check = false;
    // handle horizontally
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            board[i][j].second = 0; // to zero all 2d board check  first
            if (warning_list[itr] == false) continue;

            if (board[i][j].first.size() == 0 || board[i][j].first.top().len < choosen_size)
            {
                board[i][j].second = 1;
                check = true;
            }
        }
        itr ++;
    }

    //handle vertically
    for (int i = 0; i < 4; i++)
    {
        if (warning_list[itr] == false) continue;
        for (int j = 0; j < 4; j++)
        {
            if (board[j][i].first.size() == 0 || board[j][i].first.top().len < choosen_size)
            {
                board[j][i].second = 1;
                check = true;
            }
        }
        itr++;

    }

    //handle top left diagonal
    if (warning_list[itr++] == true) 
    {
        for (int i = 0; i < 4; i++)
        {
            if (board[i][i].first.size() == 0 || board[i][i].first.top().len < choosen_size)
            {
                board[i][i].second = 1;
                check = true;
            }
        }
    }

    //handle top right diagonal
    if (warning_list[itr] == true)
    {
        for (int i = 0; i < 4; i++)
        {
            int j = 3 - i;
            if (board[i][j].first.size() == 0 || board[i][j].first.top().len < choosen_size)
            {
                board[i][j].second = 1;
                check = true;
            }
        }
    }

    off_outer_clicks(player_1.player);
    off_outer_clicks(player_2.player);

    return check; // if check still equal false then player have no play (player loose ---> game over)
}

void off_outer_clicks(vector<pair< stack<GobbletNode>, bool>>& player)
{
    for (int i = 0; i < 3; i++)
    {
        player[i].second = 0;  
    }
}


void show_board_players(PLAYER& player_1, PLAYER& player_2, vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{

    vector<pair< stack<GobbletNode>, bool>> player = player_1.player;

    cout << "player_1 " << player_1.color <<"     ";
    for (int i = 0; i < 3; ++i) {
        if(player[i].first.size() == 0 ) cout<< 0 << "  ";
        else cout << player[i].first.top().len << "  ";
    }
    cout << endl;


    player = player_2.player;
    cout << "player_2 " << player_2.color << "     ";
    for (int i = 0; i < 3; ++i) {
        if (player[i].first.size() == 0) cout << 0 << "  ";
        else cout << player[i].first.top().len << "  ";
    }
    cout << endl;

    show_board(board);

}


void show_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    // Print the visual representation of the 2D matrix of stacks
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << "+---+---";
        }
        cout << "+" << std::endl;

        for (int j = 0; j < cols; ++j) {
            if (board[i][j].first.size() != 0)
                cout << "| " << board[i][j].first.top().len << ", " << board[i][j].first.top().color;
            else cout << "| " << 0 << ", " << 0;
        }
        cout << "|" << std::endl;
    }

    // Print the bottom border of the 2D matrix
    for (int j = 0; j < cols; ++j) {
        cout << "+---+---";
    }
    cout << "+" << std::endl;
}


void show_check_board_players(PLAYER & player_1, PLAYER & player_2, vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    vector<pair< stack<GobbletNode>, bool>> player = player_1.player;

    cout << "player_1 " << player_1.color << "     ";
    for (int i = 0; i < 3; ++i) {

        cout << player[i].second << "  ";
    }
    cout << endl;


    player = player_2.player;
    cout << "player_2 " << player_2.color << "     ";
    for (int i = 0; i < 3; ++i) {

        cout << player[i].second << "  ";
    }
    cout << endl;

    show_check_board(board);

}


void show_check_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    // Print the visual representation of the 2D matrix of stacks
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << "+---";
        }
        cout << "+" << std::endl;

        for (int j = 0; j < cols; ++j) {
                cout << "| " << board[i][j].second;
        }
        cout << "|" << std::endl;
    }

    // Print the bottom border of the 2D matrix
    for (int j = 0; j < cols; ++j) {
        cout << "+---";
    }
    cout << "+" << std::endl;
}


bool get_click_from(int &outt, int &index_i, int &index_j)
{
    int out_in;
    int out =0;
    int i =0;
    int j=0;
    cout << "if u want to choose gobblet frm out press 0 , other press 1 ";
    cin >> out_in;
    if (out_in == 0) 
    {
        cout << "choose which index";
        cin >> out;
    }
    else 
    {
        cout << "choose which index i";
        cin >> i;
        cout << "choose which index j";
        cin >> j;
    }
    outt = out;
    index_i = i;
    index_j = j;

    return out_in;
}

void get_click_to(int &to_i, int &to_j) 
{
    int index_i;
    int index_j;

    cout << "choose which index i";
    cin >> index_i;
    cout << "choose which index j";
    cin >> index_j;

    to_i = index_i;
    to_j = index_j;

}




bool check_winning(char c, vector<vector<pair< stack<GobbletNode>, bool>>>& board) 
{
    // make three for loop to check vertically, horizontally , diagonally

    //check horizontally
    bool check = true;
    for (int i = 0; i < 4; i++) 
    {
        check = true;
        for (int j = 0; j < 4; j++) 
        {
            if (board[i][j].first.size() == 0 || board[i][j].first.top().color != c) 
            {
                check = false;
            }
        }
        if (check) return check;
    }

    //check vertically
    check = true;
    for (int i = 0; i < 4; i++)
    {
        check = true;
        for (int j = 0; j < 4; j++)
        {
            if (board[j][i].first.size() == 0 || board[j][i].first.top().color != c)
            {
                check = false;
            }
        }
        if (check) return check;
    }

    //check top left diagonal
    check = true;
    for (int i = 0; i < 4; i++)
    {
        if (board[i][i].first.size() == 0 || board[i][i].first.top().color != c)
        {
            check = false;
        }
    }
    if(check) return check;


    //check top right diagonal
    check = true;
    for (int i = 0; i < 4; i++)
    {
        // i --> 0  1   2   3
        // j --> 3  2   1    0
        
        int j = 3 - i;
        if (board[i][j].first.size() == 0 || board[i][j].first.top().color != c)
        {
            check = false;
        }
    }
    //if (check) return check;

    return check;
}

bool check_warning(char c, vector<bool>& warning_list, vector<vector<pair< stack<GobbletNode>, bool>>>& board) 
{
    int itr = 0;
    bool check = false;
    //check horizontally
    int count ;
    for (int i = 0; i < 4; i++)
    {
        count = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j].first.size() == 0);
            else if(board[i][j].first.top().color != c)
            {
                count++;
            }
            else
            {
                count--; 
            }
        }
        if (count == 3) 
        { 
            warning_list[itr++] = true;
            check = true;
        }
        else warning_list[itr++] = false;
    }

    //check vertically
    for (int i = 0; i < 4; i++)
    {
        count = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[j][i].first.size() == 0);
            else if (board[j][i].first.top().color != c)
            {
                count++;
            }
            else
            {
                count--;
            }
        }
        if (count == 3)
        {
            warning_list[itr++] = true;
            check = true;
        }
        else warning_list[itr++] = false;
    }

    //check top left diagonal
    count = 0;
    for (int i = 0; i < 4; i++)
    {
        if (board[i][i].first.size() == 0);
        else if (board[i][i].first.top().color != c) count++;
        else count--;
    }
    if (count == 3)
    {
        warning_list[itr++] = true;
        check = true;
    }
    else warning_list[itr++] = false;


    //check top right diagonal
    count = 0;
    for (int i = 0; i < 4; i++)
    {
        int j = 3 - i;
        if (board[i][j].first.size() == 0);
        else if (board[i][j].first.top().color != c) count++;
        else count--;
    }
    if (count == 3)
    {
        warning_list[itr++] = true;
        check = true;
    }
    else warning_list[itr++] = false;

    return check;
}



float minimax(vector<vector<pair< stack<GobbletNode>, bool>>>& board, int depth, bool isMaximizing, bool firstTime, PLAYER & a_i) 
{

    //char opponent_player = a_i.color == 'b' ? 'w' : 'b';
    PLAYER opponent_Player = a_i.color == 'b' ? player_2 : player_1;


    // base case:
    // check winning and depth
    // check the opponent_player win first , then check the player
    if (check_winning(opponent_Player.color, board)) // player lose
    {
        return -20000;
    }
    if (check_winning(a_i.color, board))// player win
    {
        return 20000;
    }
    if(depth == 0)
    {
        return evaluate_board(board, a_i.color);
    }


    float finalScore;
    // make a fun to return (index pair<i ,j>) number a available gobblet in board and out
    vector<pair<int, int>> available_gobblets_frm_board = get_available_AI_move_board(a_i.color, board);

    vector<int> available_gobblets_frm_stack = get_available_AI_move_stack(a_i.player);

    // make minimax algorithm
   
    if (isMaximizing)
    {
        finalScore = -20000; //////////////////////////////////////////////////
        int final_to_I, final_to_J, final_frm_I;
        int final_frm_J=5;

        // make two for loop, first to iterate on move_board, second move_stack
        for (int x = 0; x < available_gobblets_frm_board.size(); x++)
        {

            pair<int, int> temp_pair(available_gobblets_frm_board[x].first, available_gobblets_frm_board[x].second);

            int length = board[temp_pair.first][temp_pair.second].first.top().len;
            
            // if  suggest_cells_case_1 return false , no moves can pay, then return game over
            if (suggest_cells_case_1(length, board) == false) 
            {
                return -20000; //////////////////////////////////////////////////////////
            }
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (board[i][j].second == 1)
                    {
                        GobbletNode temp_gobbelt = board[temp_pair.first][temp_pair.second].first.top();
                        board[temp_pair.first][temp_pair.second].first.pop();
                        board[i][j].first.push(temp_gobbelt);

                        float score = minimax(board, depth - 1, false, false, opponent_Player);//////////////////////////////////////////////////////
                        board[i][j].first.pop();
                        board[temp_pair.first][temp_pair.second].first.push(temp_gobbelt);

                        if (score > finalScore) {////////////////////////////////////////////////
                            finalScore = score;
                            final_frm_I = temp_pair.first;
                            final_frm_J = temp_pair.second;
                            final_to_I = i;
                            final_to_J = j;
                        }
                        if (firstTime) {
                            cout << "score from  board," << final_frm_I << "," << final_frm_J << ": " << score << "\n";
                            cout << " to board," << final_to_I << "," << final_to_J << endl;
                               // << ": " << score << "\n";
                            cout << endl;
                        }
                    }
                }
            }


        }

        vector<bool> warning_list(10, false);
        bool warning = check_warning(a_i.color, warning_list, board);///////////////////////////////////////////////
        //cout << "--------------------available_gobblets_frm_stack.size()" << available_gobblets_frm_stack.size();
        for (int x = 0; x < available_gobblets_frm_stack.size(); x++)
        {
            int length = a_i.player[available_gobblets_frm_stack[x]].first.top().len;

            if (warning) 
            {
                if (suggest_cells_case_21(length, board, warning_list) == false)
                {
                    return -20000;/////////////////////////////////
                }
            }
            else
            {
                if (suggest_cells_case_20(length, board) == false)
                {
                    return -20000;//////////////////////////////////////
                }
            }

            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (board[i][j].second == 1)
                    {

                        GobbletNode temp_gobbelt = a_i.player[available_gobblets_frm_stack[x]].first.top();
                        //cout << "i--> " << i << ",j-->" << j << endl;
                        a_i.player[available_gobblets_frm_stack[x]].first.pop();
                        board[i][j].first.push(temp_gobbelt);
                        //cout << "i--> " << i << ",j-->" << j << endl;
                        float score = minimax(board, depth - 1, false, false, opponent_Player);////////////////////////////////////////////////
                        //cout << "score from outtter  where x = " << x << "is -->" << score << "          " << endl;
                        
                        board[i][j].first.pop();
                        a_i.player[available_gobblets_frm_stack[x]].first.push(temp_gobbelt);

                        if (score > finalScore) {/////////////////////////////////////////////////
                            finalScore = score;
                            final_frm_I = available_gobblets_frm_stack[x];
                            final_frm_J = 6; // use it as a flag to know if it get from out ir board
                            final_to_I = i;
                            final_to_J = j;
                        }

                        if (firstTime  ) {
                            cout << "score from  out," << final_frm_I << "," << ": " << score << "\n";
                            cout << " to board," << i << "," << j <<  "\n";
                            cout << endl;
                        }
                        
                    }
                }
            }
        }
    
        //cout << endl << endl << endl;
        cout << " final score is " << finalScore<<"     ";
        if(final_frm_J == 6)
        {
            cout << "from outter";
            GobbletNode temp_gobbelt = a_i.player[final_frm_I].first.top();
            a_i.player[final_frm_I].first.pop();
            board[final_to_I][final_to_J].first.push(temp_gobbelt);
        }
        else 
        {
            cout << "from inner";
            GobbletNode temp_gobbelt = board[final_frm_I][final_frm_J].first.top();
            board[final_frm_I][final_frm_J].first.pop();
            board[final_to_I][final_to_J].first.push(temp_gobbelt);
        }
        cout << endl << endl << endl;
    }
    else // isMinimizing
    {
        
        finalScore = 20000;
        int final_to_I, final_to_J, final_frm_I;
        int final_frm_J = 5;
        
        for (int x = 0; x < available_gobblets_frm_board.size(); x++)
        {
            //if (!isMaximizing)cout << "????????????  available_gobblets_frm_board" << available_gobblets_frm_board.size() <<endl;
            pair<int, int> temp_pair(available_gobblets_frm_board[x].first, available_gobblets_frm_board[x].second);

            int length = board[temp_pair.first][temp_pair.second].first.top().len;

            // if suggest_cells_case_1 returns false, no moves can be played, then return game over
            if (suggest_cells_case_1(length, board) == false)
            {
                return 20000;
            }

            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (board[i][j].second == 1)
                    {
                        GobbletNode temp_gobbelt = board[temp_pair.first][temp_pair.second].first.top();
                        board[temp_pair.first][temp_pair.second].first.pop();
                        board[i][j].first.push(temp_gobbelt);

                        float score = minimax(board, depth - 1, true, false, opponent_Player);

                        board[i][j].first.pop();
                        board[temp_pair.first][temp_pair.second].first.push(temp_gobbelt);

                        if (score < finalScore)
                        {
                            finalScore = score;
                            final_frm_I = temp_pair.first;
                            final_frm_J = temp_pair.second;
                            final_to_I = i;
                            final_to_J = j;
                        }

                        if (firstTime) {
                           // cout << "score from  board," << final_frm_I << "," << final_frm_J << ": " << score << "\n";
                           // cout << " to board," << final_to_I << "," << final_to_J << ": " << score << "\n";
                           // cout << endl;
                        }
                    }
                }
            }

        }

        
        vector<bool> warning_list(10, false);
        bool warning = check_warning(a_i.color, warning_list, board);

        //if (!isMaximizing)cout << available_gobblets_frm_stack.size() << endl;

        for (int x = 0; x < available_gobblets_frm_stack.size(); x++)
        {
            //if (!isMaximizing)cout << available_gobblets_frm_stack[0] << endl;
            int length = a_i.player[available_gobblets_frm_stack[x]].first.top().len;
            
            if (warning)
            {
                if (suggest_cells_case_21(length, board, warning_list) == false)
                {
                    return 20000;
                }
            }
            else
            {
                if (suggest_cells_case_20(length, board) == false)
                {
                    return 20000;
                }
            }
           // if (!isMaximizing)cout << "--------------" << endl;
            //show_check_board(board);
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (board[i][j].second == 1)
                    {
                        //if (!isMaximizing)cout << "????????????" << endl;
                        //if (!isMaximizing)cout << a_i.player[available_gobblets_frm_stack[x]].first.top().len << endl;
                        //if (!isMaximizing)cout << "i --->" << i << ", j --->" << j << endl;
                        GobbletNode temp_gobbelt = a_i.player[available_gobblets_frm_stack[x]].first.top();
                        a_i.player[available_gobblets_frm_stack[x]].first.pop();
                        board[i][j].first.push(temp_gobbelt);
                        //if (!isMaximizing)cout << "************" << endl;
                        float score = minimax(board, depth - 1, true, false, opponent_Player);
                        //cout << score << score << score << score << score;
                        board[i][j].first.pop();
                        a_i.player[available_gobblets_frm_stack[x]].first.push(temp_gobbelt);
                        //cout << "____________________________" << endl;
                        if (score < finalScore)
                        {
                           // cout << "::::::::::::::::::::::"<<endl;
                            finalScore = score;
                            final_frm_I = available_gobblets_frm_stack[x];
                            final_frm_J = 6; // use it as a flag to know if it get from out ir board
                            final_to_I = i;
                            final_to_J = j;
                            //cout << "$$$$$$$$$$$$$$$$$$$$$";
                        }

                        if (firstTime)
                        {
                           // cout << "score from  out," << final_frm_I << "," << ": " << score << "\n";
                            //cout << " to board," << final_to_I << "," << final_to_J << ": " << score << "\n";
                            //cout << endl;
                        }
                    }
                }
            }
        }
    }

    return finalScore;
}




vector<pair<int,int>> get_available_AI_move_board(char player, vector<vector<pair< stack<GobbletNode>, bool>>>& board)
{
    vector<pair<int, int>> available_gobblets;
    pair<int, int> temp_pair;

    // get  available gobblet from board
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            // check on each cell if the cell is empty or have same color c
            if (board[i][j].first.size() != 0 && board[i][j].first.top().color == player)
            {
                temp_pair.first = i;
                temp_pair.second = j;
                available_gobblets.push_back(temp_pair);
            }
            
        }
    }

    return available_gobblets;
}

vector<int> get_available_AI_move_stack(vector<pair< stack<GobbletNode>, bool>> player)
{

    vector<int> available_gobblets;
 
    // make a bool list with size => 4 to check if the size if choosen before or not 
    vector<bool> taken_bfore(4, false);
    for (int i = 0; i < 3; i++) 
    {
        if (player[i].first.size() != 0) 
        {
            //cout << i << "     " ;
            if (taken_bfore[player[i].first.top().len - 1] == false) 
            {
                // first element refer to index of playerStack, second element refer to flag(if index from)
                available_gobblets.push_back(i);
                taken_bfore[player[i].first.top().len - 1] = true;
            }
        }
    }

    return available_gobblets;
}


float evaluate_board(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char player)
{
    char opponent_player = player == 'b' ? 'w' : 'b';

    if (check_winning(player, board)) 
    {
        return 20000;
    }
    if (check_winning(opponent_player, board)) 
    {
        return -20000;
    }


    float piece_count_weight = 1;
    float threat_weight = 2;
    float blocking_weight = 2;


    float player_score = 0;
    float opponent_score = 0;
    int num_of_empty_cell = 0;


    // Piece count
    player_score += piece_count_weight * count_pieces(board, player);
    opponent_score += piece_count_weight * count_pieces(board, opponent_player);

    // Threats 
    player_score += threat_weight * count_threats(board, opponent_player);
    opponent_score += threat_weight * count_threats(board,player);

    //  blocking
    player_score += blocking_weight * count_blocks(board, player);
    opponent_score += blocking_weight * count_blocks(board, opponent_player);

    return player_score - opponent_score;

}


// to give a score to the pieces on the board based on (number, size, postion)
float count_pieces(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char player)
{
    float result = 0;

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j].first.size() == 0) continue;

            if (board[i][j].first.top().color == player) 
            {
                if ((i == 0 || i == 3) && (j == 0 || j == 3)) 
                {
                    // handel corner
                    result += 2 * ( 0.25 * board[i][j].first.top().len);
                }
                else if ((i == 0 || i == 3) || (j == 0 || j == 3)) 
                {
                    // handel boundary
                    result += (0.25 * board[i][j].first.top().len);
                }
                else 
                {
                    // handle center
                    result += 2 * (0.25 * board[i][j].first.top().len);
                }
            }

        }
    }
    return result;

}


int count_threats( vector<vector<pair< stack<GobbletNode>, bool>>>& board, char c)
{
    int result = 0;

    //check horizontally
    int count;
    for (int i = 0; i < 4; i++)
    {
        count = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j].first.size() == 0);
            else if (board[i][j].first.top().color != c)
            {
                count++;
            }
            else
            {
                count--;
            }
        }
        if (count == 3)
        {
            result++;
        }
    }

    //check vertically
    for (int i = 0; i < 4; i++)
    {
        count = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[j][i].first.size() == 0);
            else if (board[j][i].first.top().color != c)
            {
                count++;
            }
            else
            {
                count--;
            }
        }
        if (count == 3)
        {
            result++;
        }

    }
    
    //check top left diagonal
    count = 0;
    for (int i = 0; i < 4; i++)
    {
        if (board[i][i].first.size() == 0);
        else if (board[i][i].first.top().color != c) count++;
        else count--;
    }
    if (count == 3)
    {
        result++;
    }

    //check top right diagonal
    count = 0;
    for (int i = 0; i < 4; i++)
    {
        int j = 3 - i;
        if (board[i][j].first.size() == 0);
        else if (board[i][j].first.top().color != c) count++;
        else count--;
    }
    if (count == 3)
    {
        result++;
    }

    return result;
}

int count_blocks(vector<vector<pair< stack<GobbletNode>, bool>>>& board, char c)
{
    int result = 0;

    //check horizontally
    int count_p;
    int count_o;
    for (int i = 0; i < 4; i++)
    {
        count_p = 0;
        count_o =0;
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j].first.size() == 0) break;
            else if (board[i][j].first.top().color != c)
            {
                count_o++;
            }
            else
            {
                count_p++;
            }
        }
        if (count_o == 3 && count_p == 1)
        {
            result++;
        }
    }

    //check vertically
    for (int i = 0; i < 4; i++)
    {
        count_p = 0;
        count_o = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[j][i].first.size() == 0)break;
            else if (board[j][i].first.top().color != c)
            {
                count_p++;
            }
            else
            {
                count_o++;
            }
        }
        if (count_o == 3 && count_p == 1)
        {
            result++;
        }

    }

    //check top left diagonal
    count_p = 0;
    count_o = 0;
    for (int i = 0; i < 4; i++)
    {
        if (board[i][i].first.size() == 0)break;
        else if (board[i][i].first.top().color != c) count_p++;
        else count_o++;
    }
    if (count_o == 3 && count_p == 1)
    {
        result++;
    }

    //check top right diagonal
    count_p = 0;
    count_o = 0;
    for (int i = 0; i < 4; i++)
    {
        int j = 3 - i;
        if (board[i][j].first.size() == 0)break;
        else if (board[i][j].first.top().color != c) count_p++;
        else count_o++;
    }
    if (count_o == 3 && count_p == 1)
    {
        result++;
    }

    return result;
}


int getRandomNumber() {
    // Seed the random number generator with the current time
    std::random_device rd;
    std::mt19937 generator(rd());

    // Define the distribution for integers between 1 and 4
    std::uniform_int_distribution<int> distribution(1, 4);

    // Generate a random number
    int randomNumber = distribution(generator);

    return randomNumber;
}
