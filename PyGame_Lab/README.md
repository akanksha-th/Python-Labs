# PyGameLab

Once upon a boring spring, with a week’s holiday and an empty hostel…  
I decided to pick up a new hobby — that’s when I tried my hands on **Pygame**.  
It was fun if nothing else, and I’ll be catching on soon! INDEED!!  

---

## 🕹️ What’s Inside?  
A bunch of mini-games I built while learning Pygame.  
Some are cool, some are broken — all are part of the journey!  

- **DotDash** → Moving shapes & basic controls 
- **BrickBreaker** → Collision detection & paddle logic 
- **BouncingBall** → Multi-directional controls (needs fixing!)  
- **RunToTheEdge** → Sprite sheets & restart mechanics  
- **FlappyBall** → Gravity, jump physics & win conditions  

---

## Folder Structure

    PyGame_Labs
    │   1.DotDash.py
    │   2.BrickBreaker.py
    │   3.BouncingBall.py
    │   4.Run_to_the_edge.py
    │   5.FlappyBall.py
    │   README.md
    │   
    └───demo_images
            BouncingBall_demo.png
            BrickBreaker_demo.png
            DotDash_demo.png
            FlappyBall_demo.png
            RunToTheEdge_demo.png

--------------------------------------------------------

## Here's what I learned

### 1. DotDash
**Description:**

A simple game where a circle moves across the screen using the WASD keys. The game introduces basic movement mechanics.

**What I Learned:**
- How to draw objects (like circles) on the screen using Pygame.
- How to display text on the screen.

### 2. BrickBreaker
**Description:**

A classic brick-breaking game where a player-controlled paddle bounces a ball to break bricks.

**What I Learned:**
- The difference between shape objects (pygame.draw.rect()) and placeholders- for positioning & collision detection (pygame.Rect()).
- How to implement collision detection and control object movement using logic.

### 3. BouncingBall
**Description:**

 The left and right paddles are controlled using W/S and Up/Down keys, while the top and bottom paddles are controlled using A/D and Left/Right keys. The game stops when the ball escapes the screen.

**What I Learned:**A visualization game with four paddles and a bouncing ball.
- Attempted to extend knowledge from the BrickBreaker game.
- The complexity of multi-directional controls made the game difficult to manage.
- This game needs fixing to improve playability.
- Learned how to detect win condition and how to implement a game restart feature.


### 4. RunToTheEdge
**Description:**

A game where a sprite character moves left and right using arrow keys to reach the other end of the screen.

**What I Learned:**
- How to use sprite sheets in Pygame.
- How to create text that changes size dynamically, simulating a GIF effect.
- Implemented a game restart feature.

### 5. Flappy Ball
**Description:**

A simple physics-based game where a ball falls due to gravity and jumps when the spacebar is pressed. The goal is to reach the top of the screen to win. If successful, the game displays a "You Win!" message and restarts after 10 seconds.

**What I Learned:**
- How to apply gravity and jump mechanics in Pygame.
- How to display a win message dynamically.

---

## 🖼️ Game Previews  

| DotDash | BrickBreaker | BouncingBall | RunToTheEdge | FlappyBall |
|---------|--------------|--------------|--------------|------------|
| A simple game where a circle moves with WASD keys. <br><br> ![](demo_images/DotDash_demo.png) | Classic paddle-ball brick breaker. <br><br> ![](demo_images/BrickBreaker_demo.png) | A ball bounces with four paddles (W/S, A/D, arrows). <br><br> ![](demo_images/BouncingBall_demo.png) | Sprite character runs to the screen edge. <br><br> ![](demo_images/RunToTheEdge_demo.png) | Gravity-based ball that jumps with spacebar. <br><br> ![](demo_images/FlappyBall_demo.png) |


## 🎯 What I Built & Learned

### 1. DotDash
| | |
|-|-|
| **Preview** | ![](demo_images/DotDash_demo.png) |
| **Description** | A simple game where a circle moves with WASD keys. |
| **Key Learnings** | - Drawing objects (circles)<br>- Displaying text in Pygame |

---

### 2. BrickBreaker
| | |
|-|-|
| **Preview** | ![](demo_images/BrickBreaker_demo.png) |
| **Description** | Classic paddle-ball brick breaker. |
| **Key Learnings** | - Difference: `pygame.draw.rect()` vs `pygame.Rect()`<br>- Collision detection & movement logic |

---

### 3. BouncingBall
| | |
|-|-|
| **Preview** | ![](demo_images/BouncingBall_demo.png) |
| **Description** | A ball bounces with four paddles (W/S, A/D, arrows). |
| **Key Learnings** | - Extended logic from BrickBreaker<br>- Learned win/restart conditions<br>- Multi-direction controls (too messy, needs fixing!) |

---

### 4. RunToTheEdge
| | |
|-|-|
| **Preview** | ![](demo_images/RunToTheEdge_demo.png) |
| **Description** | Sprite character runs to the screen edge. |
| **Key Learnings** | - Using sprite sheets<br>- Dynamic text effects (like GIF)<br>- Restart feature |

---

### 5. FlappyBall
| | |
|-|-|
| **Preview** | ![](demo_images/FlappyBall_demo.png) |
| **Description** | Gravity-based ball that jumps with spacebar. |
| **Key Learnings** | - Gravity & jump mechanics<br>- Dynamic win message display |
