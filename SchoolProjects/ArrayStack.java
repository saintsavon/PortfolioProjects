package SchoolProjects;

public class ArrayStack {

    int[] stack; // Array containing the data in the stack
    int top; // Index representing the top of the stack

    // Constructor
    ArrayStack() {
    stack = new int[10];
    top = 0;
    }

        void makeNewArray() {
        int[] newStack = new int[stack.length * 2];
        for (int i = 0; i < stack.length; i++) {
            newStack[i] = stack[i];
            }
        stack = newStack;
        }

        //push operation
        void push(int e) {
        if (top == stack.length) {
            makeNewArray();
            }
        stack[top] = e;
        top++;
        }

        //pop operation
        int pop() {
        top--;
        return stack[top];
        }

        //peek operation
        int peek() {
        return stack[top - 1];
        }

        //isEmpty operation
        boolean isEmpty() {
        return top == 0;
        }

        //size operation
        int size() {
        return top;

    }

}