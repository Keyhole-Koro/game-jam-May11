# Declare characters used by this game. Each character has a unique identifier.
# The color argument is optional and can be used to colorize the name display.

define old_woman = Character("Old Woman")
define old_man = Character("Old Man")
define momotaro = Character("Momotaro")
define villager_a = Character("Villager A")
define villager_b = Character("Villager B")
define dog = Character("Dog")
define monkey = Character("Monkey")
define pheasant = Character("Pheasant")
define rabbit = Character("Rabbit")
define raccoon_dog = Character("Raccoon Dog")
define turtle = Character("Turtle")
define demon_leader = Character("Demon Leader")

# The game starts here.
label start:

    # Scene 1: The discovery of the peach at the river.
    scene bg river with fade
    old_woman "My goodness! What a huge peach!"
    old_woman "A peach this splendid—Grandpa will be so happy if I bring it home."
    old_woman "Let’s have this peach for dinner. Hehe, today’s going to be a good day."

    # Scene 2: The miraculous birth of Momotaro from the peach.
    scene bg house with fade
    old_man "Wow! That’s one enormous peach! Where did you find it?"
    old_woman "I found it in the river. It was so magnificent, I thought we’d have it for dinner."
    "Thud! The peach suddenly trembled and then split cleanly in half."
    momotaro "Hello, Grandpa and Grandma! I’m Momotaro, born from a peach!"
    old_woman "What a miracle… But I’m so happy. From today, we’re a family of three."

    # Scene 3: Momotaro decides to fight the demons after hearing about their atrocities.
    scene bg village_square with fade
    villager_a "The demons came again and stole our rice..."
    villager_b "I heard a village beyond the mountains was burned down..."
    momotaro "Grandpa, Grandma. I’m going to Oni Island to defeat the demons."
    old_woman "Please don’t… The demons are terrifying..."
    momotaro "But if I don’t go, the villagers will continue to suffer. I want to protect them."
    old_woman "All right. Then let me make you some millet dumplings to give you strength."

    # Scene 4: Departure. The grandparents bid farewell to Momotaro.
    scene bg house with fade
    old_woman "Here, Momotaro. Take these with you. I made them with all my heart — they’ll give you strength."
    old_man "You can do this. Keep your heart true and go forward with courage."
    momotaro "I will! I’m off!"

    # Scene 5: Meeting potential animal companions on the journey.
    # Each animal interaction is handled by calling the `meet_animal` function.
    call meet_animal("Dog", "wagging tail", "Sure! Let’s go beat those demons!", "No thanks, but good luck!")
    call meet_animal("Monkey", "grinning", "Alright, I’ll join!", "Hmm… I’ll pass this time.")
    call meet_animal("Pheasant", "spreading wings", "Gladly! I’ll support you from the skies.", "I’ll cheer for you from here.")
    call meet_animal("Rabbit", "ears twitching", "Sure, I’ll come along!", "I’ll stay here, but I’ll be cheering you on!")
    call meet_animal("Raccoon Dog", "smiling", "Of course I will!", "I’ll stay back. Safe travels!")
    call meet_animal("Turtle", "slowly", "I’ll join you.", "I’ll stay here and watch over you from afar.")

    # Scene 6: Arrival at Oni Island and preparation for the battle.
    scene bg oni_island with fade
    momotaro "So this is… Oni Island."
    dog "Hey, Momotaro. Look over there!"
    "We saw a group of demons gathered around a bonfire, laughing and shouting."
    momotaro "Everyone, are you ready? Now’s the time for us to fight together."

    # Scene 7: Confrontation and battle with the demons.
    label battle:
        momotaro "Hey, demons! Why do you steal from the village?!"
        demon_leader "There's no reason. We do it just because we're strong and it's fun. That's all."
        momotaro "You’re crazy! The villagers are suffering because they’ve lost everything!"
        menu:
            "Fight the demons":
                jump fight
            "Run away":
                momotaro "I won’t give up, but I need to regroup."
                return

    # Battle sequence against the demons. Placeholder for gameplay mechanics.
    label fight:
        "A fierce battle ensued..."
        menu:
            "Win":
                momotaro "Never steal from the village again."
                demon_leader "We understand… we won’t do it again. Please forgive us."
                return
            "Lose":
                momotaro "I must try again!"
                jump battle

    return

# Function for meeting animal companions during the journey.
# Parameters:
# - animal_name: The name of the animal.
# - action: A description of the animal's behavior.
# - join_response: The response if the animal joins Momotaro.
# - decline_response: The response if the animal declines to join.
label meet_animal(animal_name, action, join_response, decline_response):
    # Introduce the animal
    "[animal_name] ([action]) \"Where are you going?\"" 
    momotaro "To Oni Island. I’m going to defeat the demons."
    
    # Add a player choice to decide if the animal joins
    menu:
        "Invite the [animal_name] to join":
            momotaro "I have some millet dumplings. Will you come with me?"
            "[animal_name] ([action]) \"[join_response]\""
            # Add the animal to the party or any tracking variable here if necessary.
        "Continue without [animal_name]":
            "[animal_name] ([action]) \"[decline_response]\""

    return