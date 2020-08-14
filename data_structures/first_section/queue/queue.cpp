#include <iostream>
#include <ostream>

using namespace std;

class Node{
  public:
    int data; //interchangeable with different types of data
    Node *next;
};

class Queue{
  private:
    Node *first;
    Node *last;
  public:
    Queue(){
      first = NULL; //Set the first node to NULL by default
      last = NULL;
    }
    void Add(int new_data){
      Node *add = new Node();
      add -> data = new_data;
      if(first == NULL){
        first = add;
	last = add;
      }
      else{
        Node *node_var = first;
        while (node_var -> next != NULL){
            node_var = node_var -> next;
        }
        node_var -> next = add;
        last = node_var;
      }
    }
    Node * Remove(){
      Node *node_first = first;
      if (first != NULL){
        first = first -> next;
      }
      else{
        cout << "Understack\n" << endl;
      }
      return node_first;
    }
    int Top(){
      return first -> data ;
    }
    int Peek(){
      return last -> data;
    }
    bool Is_Empty(){
      if(first == NULL){
        return true;
      }
      return false;
    }
};

int main() {
  return 0;
}