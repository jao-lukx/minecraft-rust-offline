fn mining(
    game: &mut crate::game::Game<'_>,
    pos: [i32; 3],
) -> core::ops::ControlFlow<crate::game::Result<()>> {
    let previous_break_pos = game.lan_break_pos;
    game.lan_break_pos = Some(pos);
    let result = game.with_player_actor(|game| game.veinminer_break_block(pos));
    game.lan_break_pos = previous_break_pos;
    core::ops::ControlFlow::Break(result)
}
