# USAGE

- import 2 module

```
    from app.graphic import draw_pane, play_game
```

- draw_pane

```
    pac_man_id, ghost_ids, food_ids, score_table_id = draw_pane(map, map_size, pacman_pos, zoom=0.7)
```

- play_game

```
    play_game(
            map_size,
            pac_man_id,
            ghost_ids,
            food_ids,
            score_table_id,
            path,
            ghost_paths,
            score,
            time_frame=0.3,
            zoom=0.7
        )
```
