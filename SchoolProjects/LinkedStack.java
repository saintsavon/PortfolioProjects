package SchoolProjects;

class LinkedNode {

    protected int x;
    protected LinkedNode next;

    public LinkedNode(int n) {
    this.x = n;

    }

}
    
    public class LinkedStack {
    
    LinkedNode front; // Reference to the first LinkedNode in the list
    int count; 
    
    // Constructor
    LinkedStack() {
    front = null;
    count = 0;
    }
    
        //push operation
        void push(int x) {
        LinkedNode newNode = new LinkedNode(x);
        newNode.next = front;
        front = newNode;
        count++;
        }
    
        //pop operation
        int pop() {
        int x = front.x;
        front = front.next;
        count--;
        return x;
        }
    
        //peek operation
        int peek() {
        return front.x;
        }
    
        // isEmpty operation
        boolean isEmpty() {
        return front == null;
        }
    
        //size operation
        int size() {
        return count;
        }
    
        public String toString() {
        String str = "";
        LinkedNode cur = front;

        while (cur != null) {
            str += cur.x + " ";
            cur = cur.next;
        }
        return str;
    
    }
    
}