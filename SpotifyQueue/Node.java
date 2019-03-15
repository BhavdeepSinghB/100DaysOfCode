public class Node {
    private Song s;
    private Node next;
    private Node prev;

    public Node(Song s, Node next, Node prev) {
        this.s = s;
        this.next = next;
        this.prev = prev;
    }

    public Node(Song s, Node next) {
        this.s = s;
        this.next = next;
        this.prev = null;
    }

    public Song getSong() {
        return this.s;
    }

    public Node getNext() {
        return this.next;
    }

    public Node getPrev() {
        return this.prev;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public void setSong(Song s) {
        this.s = s;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }
}
