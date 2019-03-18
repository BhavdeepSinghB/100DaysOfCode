public class Node {
    private Song s;
    private Node next;
    private Node prev;
    private boolean qStatus;

    public Node(Song s, Node next, Node prev, boolean qStatus) {
        this.s = s;
        this.next = next;
        this.prev = prev;
        this.qStatus = qStatus;
    }

    public Node(Song s, Node next, Node prev) {
        this.s = s;
        this.next = next;
        this.prev = prev;
        this.qStatus = false;
    }

    public Node(Song s, Node next) {
        this.s = s;
        this.next = next;
        this.prev = null;
        this.qStatus = false;
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

    public boolean getqStatus() {
        return this.qStatus;
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

    public void setqStatus(boolean qStatus) {
        this.qStatus = qStatus;
    }
}
