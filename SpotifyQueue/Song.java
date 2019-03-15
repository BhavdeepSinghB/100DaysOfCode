public class Song {
    private String name;
    private String artist;
    private String album;
    private double duration;

    public Song(String name, String artist, String album, double duration) {
        this.name = name;
        this.artist = artist;
        this.album = album;
        this.duration = duration;
    }

    public Song(String name, String artist, double duration) {
        this.name = name;
        this.artist = artist;
        this.album = name;
        this.duration = duration;
    }

    public String getName() {
        return this.name;
    }

    public String getArtist() {
        return this.artist;
    }

    public String getAlbum() {
        return this.album;
    }

    public double getDuration() {
        return this.duration;
    }

    public String toString() {
        return this.getName() + " by " + this.getArtist() + " from " + this.getAlbum() + "\n";
    }
}
