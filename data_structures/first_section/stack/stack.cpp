
#include <iostream>
#include<ostream>
using namespace std;
class Node
{
public:
	int data; //interchangeable with different types of data
	Node *next;

};
class Stack
{
private:
	Node *top;
public:
	Stack()
	{
		top = NULL; //Set the initial node as NULL
	}
	void Push(int number)//Adds and item into the stack
	{
		Node *temp; //Create a new node
		temp = new Node();
		temp->data = number;// And we stablish the number given as input of the method
		if (top == NULL)
		{
			temp->next = NULL; // If the current node is null we create the future one
		}
		else
		{
			temp->next=top;//Otherwise the last node will become
			//The one pointed by the new one
		}
		top = temp; //Set the new node as the current one
	}
	int Pop()//Remove the last item that was added from the stack and returns it
	{
		if (top==NULL)
		{
			cout<<"Underflow"<<endl; //Occurs if the stack if empty
			return 0;
		}
		else
		{
			Node * temp =top; //Set the a temporal node as the current one
			top = top->next; //Set the current one as the one below it
			int aux = temp->data; //save the value popped()
			delete(temp); // 
			return aux;
		}
	}
	int Peek()//Returns the last item added to the stack
	{
		return top->data;
	}
	bool isEmpty()//Returns true if the stack is empty, false if it has at least one element
	{
		if (top==NULL)
		{
			return true;
		}
		return false;
	}
	
};
int main() {
    return 0;
}