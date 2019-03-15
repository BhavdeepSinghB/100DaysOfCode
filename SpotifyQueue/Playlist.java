public class Playlist {
    private Node head;
    private Node tail;

    public Playlist() {
        head = null;
        tail = null;
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

    public static void main(String args[]) {
        Playlist p = new Playlist();

        Song s1 = new Song("Island in the Sun", "Weezer", "Green Album", 4.5);
        Song s2 = new Song("Nothing Else Matters", "Metallica", "The Black Album", 2.5);
        Song s3 = new Song("Dirty Water", "Foo Fighters", "Concrete and Gold", 3.2);
        Song s4 = new Song("Everlong", "Foo Fighters", "The Size and the Shape", 3.5);

        p.append(s1);
        p.append(s2);
        p.append(s3);
        p.append(s4);

        p.print();
    }
}
