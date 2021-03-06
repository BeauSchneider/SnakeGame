# SnakeGame
 snake game in python with OOP and turtle libraries.
Author(s): Beau Schneider

❗️indicates action items; you should remove these emoji as you complete/update the items which they accompany. (This means that your final README should have no ❗️in it!)

References: Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.

https://www.edureka.co/community/51415/how-do-i-make-one-turtle-follow-another-turtle-in-python: i used this source to help me create the turtle that follows the player around (cube3.setheading(cube3.towards(self)))
https://opensource.com/article/19/7/get-modular-python-classes: I used this source to just help me understand more about classes and programming.
http://cs.berea.edu/courses/csc226book/events.html: i used chapter 10 in the textbook to help me with keybindings, and learned how to use the (goto) and (wn.listen()).
http://cs.berea.edu/courses/csc226book/hello_little_turtles.html: I referenced this chapter to help me brush up on turtles and their commands and functions.
Milestone 1: Setup, Planning, Design
️Title: This > The Snake game?

Purpose: In a single sentence, describe what your project will do. - This program will let the user control a snake and collect (candy).

️Sources: Which assignments or code will you base your project on? - This assignment won't be based off of a previously made assignment

️Kanban Board: What is the link to the Kanban board on Trello? - https://trello.com/b/aRY9ZaNq/final-project

️CRC Card:

Please write a CRC card for a class that your project will implement.
See this link for a sample CRC card, and a template to use for your own cards (you will have to make a copy to edit): https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing
Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - and replace it with your own.
alt text alt text alt text alt text
Milestone 2: Code
No README action items. Keep your Kanban board up to date, and focus on your code. 🙃

Milestone 3: Virtual Check-in
Indicates what percentage of the project you have left to complete, and how confident you are feeling.

️Completion Percentage: 80%

️Confidence: Describe how confident you feel about completing this project, and why. Then, describe some strategies you can employ to increase the likelihood taht you'll be successful in completing this project before the deadline. - I feel fairly confident in my ability to complete this assignment, but i know that if i get stuck I can look in the textbook or go to the lab for assistance.
Milestone 4: Final Code, Presentation, Demo
User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button.

once the user has hit the start button the window to play will pop up. Click on the window and use the left and right arrow keys to make the turtle turn left or right by 90 degrees. The player will also be able to use the down arrow key to turn 180 degrees. On death of the player you will use the 'q' key to quit the program and click the run button to try again. the goal of the game is to avoid everything that's red and collect the yellow "candies" that spawn around the playable area (each candy give the player 10 score). while doing this you will have to stay on the move to avoid the enemy that is constantly following the player around the playable area. The enemy also isnt as fast as the player but its also not restricted my 90 degree movement, so the player has to be smart/tactical to evade it. If the enemy catches you die, and the score is reset to 0! Survive as long as you can and try to get a high score!
Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.

Red enemies can sometimes spawn in front or on top of player after collecting a candy.
snake growing with every candy eaten had to be scrapped due to time, and the complexity of the code that would have to be written to make it work. Instead, an enemy that chases the player was created to make the game much harder.
program starts automatically, so the user has to click on the window quickly and immediately start playing.
there is no grind in the game like a classic snake game. This is because the enemy player doesn't move in 90 degree turns, and I didn't want the screen to feel cluttered.
Program doesn't automatically reset after each player death, instead it makes the player press 'q' to quit and makes the player press the run button again.
whenever the player presses a key to move in a direction the enemy freeze momentarily until the player starts moving again.
Reflection
In three to four well-written paragraphs, address the following (at a minimum):

Why did you select the project that you did?

How closely did your final project reflect your initial design?

What did you learn from this process?

What was the hardest part of the final project?

What would you do differently next time, knowing what you know now?

I was very interested in this project when it was assigned and have had a lot of fun working on it. To choose this project I knew I wanted to make a game that was challenging but also try to not do too much and overload myself. At first, I wanted to make a version of rock paper scissors that would use keys to tell what the users input was but that felt a little too easy, and I wanted it to be more interactive. Then I decided on making a snake game, at first everything was working fine until i realized i didn't know how to make the snake grow after eating each candy and if the snake never grew the game would have no challenge. To combat this I decided to make an enemy that follows the player constantly and if he catches the player you die. I also used some random red squares as additional enemies for the player to have to navigate around.

So my inital design had to be changed slightly to make new enemies and this caused the game to become very different from what I intended it to be from the start. But im glad for these changes I made to the original snake game. It added I feel a much-needed layer of authenticity and made the project unique to me. I knew there had been examples/people that had made a snake game in python before so as a part of this assignment I made sure that id make changes to the game to make it my own, and in the end it almost became a whole new game.

When i first started this project i had very little experience using classes and didnt fully understand how to use them when writing my code (I still don't completely). But once I got started and read over the chapters in the textbook on classes and turtles it helped be get a better idea for where to start (CRC cards helped a lot too). I made a base template with classes and some methods in them with no actual code just yet. I would say from there it was actually not extremely difficult. The most difficult part for me was deciding what to put in the parameters for the classes and objects and using them appropriately in the code. But a very close second to that would definitely be the score system. I had to go to the Lab to get help and once they gave me a few hints the solution became clear, I was just thinking about how to go about it in the wrong way and got stuck.

If i could start over i would make a few changes. I would definetly make a lot more classes, i found that when i made the CRC cards I thought I wouldn't use nearly as many classes as I ended up needing in the end. Also i would make significantly more methods for each object in the classes to make it a lot easier to make more specific things happen when referencing certain objects in the game. I've learned a lot from this project particular when it comes to classes and how to use them in making bigger files of code. Also using the users keyboard/mouse interaction was a lot of fun, and I learned and got a lot more experience using those commands while working on this project.

Ive had a great time working on this assignment as it helped me learn new things and was overall a very interesting and engaging project. I will most definitely make more games in my free time to continue to practice coding and learn even more on how to make other functions/classes work together to make more games in better detail.
