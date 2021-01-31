def on_on_overlap(sprite, otherSprite):
    global count, level
    count += 1
    info.change_score_by(1)
    otherSprite.destroy()
    otherSprite.start_effect(effects.smiles, 200)
    if count > 10 + level:
        level += 1
        music.jump_up.play()
        startLevel()
    else:
        music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def startLevel():
    global count, food
    scene.set_background_color(randint(3, 7))
    count = 0
    index = 0
    while index <= 10 + level:
        food = sprites.create(sprites.food.small_cherries, SpriteKind.food)
        food.set_position(randint(20, 140), randint(20, 100))
        index += 1
    player2.say("Level " + str(level), 1000)
    info.start_countdown(10)
food: Sprite = None
count = 0
player2: Sprite = None
level = 0
game.splash("Ready to get UFinanced?", "Click \"A\" to continue")
music.pew_pew.play_until_done()
game.splash("Learn about personal", "finance by answering")
music.pew_pew.play_until_done()
game.splash("...a series of questions!")
music.pew_pew.play_until_done()
game.splash("Afterwards, play a fun", "mini game as your reward!")
music.pew_pew.play_until_done()
game.splash("A = True", "B = False")
music.pew_pew.play_until_done()
game.splash("Ready to get UFinanced?", "Let's GO!")
music.ba_ding.play_until_done()
scene.set_background_color(13)
if game.ask("Video games are needs.", "(A) True or (B) False?"):
    scene.set_background_color(2)
    game.splash("Incorrect. Food, shelter,", "and safety are needs.")
else:
    scene.set_background_color(7)
    game.splash("Good job!", "Food, shelter, & safety are needs.")
scene.set_background_color(13)
music.pew_pew.play_until_done()
if game.ask("Saving money is good.", "(A) True or (B) False?"):
    scene.set_background_color(7)
    game.splash("Great job!", "Saving money is good.")
else:
    scene.set_background_color(2)
    game.splash("It's okay to spend,", "but make sure to save money too.")
scene.set_background_color(13)
music.pew_pew.play_until_done()
if game.ask("Always borrow money.", "(A) True or (B) False?"):
    scene.set_background_color(2)
    game.splash("Only borrow if you know", "you can pay it back on time.")
else:
    scene.set_background_color(7)
    game.splash("Good job!", "Borrow money only when needed.")
scene.set_background_color(13)
music.pew_pew.play_until_done()
if game.ask("All money is the same.", "(A) True or (B) False?"):
    scene.set_background_color(2)
    game.splash("Better luck next time.",
        "Countries can have different currencies.")
else:
    scene.set_background_color(7)
    game.splash("Amazing! The United States",
        "uses dollars, but not all countries do.")
scene.set_background_color(13)
music.pew_pew.play_until_done()
if game.ask("Taxes are paid to police.", "(A) True or (B) False?"):
    scene.set_background_color(2)
    game.splash("Not quite.",
        "Taxes are paid to the government for schools and roads.")
else:
    scene.set_background_color(7)
    game.splash("Amazing! Taxes are paid to the",
        "government for schools and roads.")
music.jump_up.play_until_done()
scene.set_background_color(5)
game.splash("Wow, you finished all", "those questions!")
game.splash("Let's end with a FUN", "mini game.")
game.splash("Use the arrows on your",
    "keyboard or on your screen to play.")
game.splash("Hurry!", "Eat the cherries!")
level = 1
player2 = sprites.create(sprites.builtin.forest_snake4, SpriteKind.player)
controller.move_sprite(player2, 70, 70)
startLevel()
