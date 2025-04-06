package com.example.spotifybackend.Music;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MusicService {

    private final MusicRepository musicRepository;
    @Autowired
    public MusicService(MusicRepository musicRepository){
        this.musicRepository = musicRepository;
    }

    public List<Music> getMusic(){
        return musicRepository.findAll();
    }

    public void addNewMusic(Music music){
        musicRepository.save(music);
    }
}
