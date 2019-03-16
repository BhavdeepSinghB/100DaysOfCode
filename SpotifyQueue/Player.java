public class Player {
	private Playlist exp;

	public Player(Playlist p) {
		exp = new Playlist();
		p.shallowCopy(exp);
	} 

	public Song nowPlaying() {
		return exp.head.getSong();
	}

	public void playNext() {
		if(exp.head.getNext() != null) {
			exp.head = exp.head.getNext();	
			return;
		}
		System.out.println("This is the last song");
		
	}

	public void playPrev() {
		if(exp.head.getPrev() != null) {
			exp.head = exp.head.getPrev();
			return;	
		}
		System.out.println("This is the first song");
		
	}

	public static void main(String args[]) {
		Playlist list = new Playlist();

		Song s = new Song("Sunday Rain", "Foo Fighters", 3.4);
		list.append(s);
		s = new Song("Sky is a Neightbourhood", "Foo fighters", "Concrete and Gold", 3.2);
		list.append(s);
		s = new Song("Everlong", "Foo fighters", "The size and the shape", 2.5);
		list.append(s);
		s = new Song("Congregation", "Foo fighters", "Sonic Highways", 3.8);
		list.append(s);


		Player pl = new Player(list);
		System.out.println(pl.nowPlaying());
		pl.playNext();
		System.out.println(pl.nowPlaying());
		pl.playPrev();
		System.out.println(pl.nowPlaying());
		pl.playPrev();
		//System.out.println(pl.nowPlaying());

	}
}