package com.example.spotifybackend.Music;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "api/music")
public class MusicController {
    private final MusicService musicService;

    @Autowired
    public MusicController(MusicService musicService){
        this.musicService = musicService;
    }

    @GetMapping
    public List<Music> getinfo(){
        return musicService.getMusic();
    }

    @PostMapping
    public void saveinfo(@RequestBody Music music){
        musicService.addNewMusic(music);
    }

}
