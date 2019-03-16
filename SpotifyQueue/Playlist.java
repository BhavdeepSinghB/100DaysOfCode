public class Playlist {
    public  Node head;
    public Node tail;

    public Playlist() {
        head = null;
        tail = null;
    }

    public Node getHead() {
        return this.head;
    }

    public void append(Song s) {
        if(head == null) {
            head = new Node(s, null);
            tail = head;
            head.setPrev(null);
            return;
        }
        tail.setNext(new Node(s, null, tail));
        tail = tail.getNext();
    }

    public void print() {
        Node temp = head;
        while(temp != null) {
            System.out.print(temp.getSong().toString());
            temp = temp.getNext();

        }
    }

    public void shallowCopy(Playlist other) {
        Node temp = head; 
        while (temp != null) {
            other.append(temp.getSong());
            temp = temp.getNext();
        }
    }
}
