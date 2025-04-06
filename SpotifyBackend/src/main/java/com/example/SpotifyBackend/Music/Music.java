package com.example.spotifybackend.Music;

import jakarta.persistence.*;

@Entity
@Table
public class Music {
    @Column(
            nullable = false
    )
    private String song_name;
    @Column(
            nullable = false
    )
    private String playlist_name;
    @Id
    @SequenceGenerator(
            name = "music_seq",
            sequenceName = "music_seq",
            allocationSize = 1

    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "music_seq"
    )
    private long id;

    public Music(String song_name, String playlist_name, long id) {
        this.song_name = song_name;
        this.playlist_name = playlist_name;
        this.id = id;
    }

    public Music(String song_name, String playlist_name) {
        this.song_name = song_name;
        this.playlist_name = playlist_name;
    }

    public Music() {
    }

    @Override
    public String toString() {
        return "Music{" +
                "song_name='" + song_name + '\'' +
                ", playlist_name='" + playlist_name + '\'' +
                ", id=" + id +
                '}';
    }

    public String getPlaylist_name() {

        return playlist_name;
    }

    public void setPlaylist_name(String playlist_name) {
        this.playlist_name = playlist_name;
    }

    public String getSong_name() {
        return song_name;
    }

    public void setSong_name(String song_name) {
        this.song_name = song_name;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }
}
