package com.example.spotifybackend.Music;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MusicRepository  extends JpaRepository<Music,Long> {
}
