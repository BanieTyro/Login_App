import tkinter as tk
from tkinter import messagebox
import os
import pygame
import turtle
import time
import sys


def save_user(username, password):
    with open("user_data.txt", 'a') as f:
        f.write(f"{username},{password}\n")

def check_user(username, password):
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", 'r') as f:
            for line in f:
                user, pwd = line.strip().split(',')
                if user == username and pwd == password:
                    return True
    return False

def login_page():
    
    tk.Label(root, text="Login").pack()
    tk.Label(root, text="Username:").pack()
    global username_entry_login
    username_entry_login = tk.Entry(root)
    username_entry_login.pack()
    
    tk.Label(root, text="Password:").pack()
    global password_entry_login
    password_entry_login = tk.Entry(root, show="*")
    password_entry_login.pack()

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Signup", command=signup_page).pack()

def signup_page():

    tk.Label(root, text="Signup").pack()
    tk.Label(root, text="Username:").pack()
    global username_entry_signup
    username_entry_signup = tk.Entry(root)
    username_entry_signup.pack()
    
    tk.Label(root, text="Password:").pack()
    global password_entry_signup
    password_entry_signup = tk.Entry(root, show="*")
    password_entry_signup.pack()

    tk.Button(root, text="Signup", command=signup).pack()
    tk.Button(root, text="Back to Login", command=login_page).pack()

def signup():
    username = username_entry_signup.get()
    password = password_entry_signup.get()
    
    if username and password:
        save_user(username, password)
        messagebox.showinfo("Success", "User signed up successfully!")
        login_page()
    else:
        messagebox.showerror("Error", "Username and password cannot be empty.")

def login():
    username = username_entry_login.get()
    password = password_entry_login.get()

    if check_user(username, password):
        messagebox.showinfo("Success", "Logged in successfully!")
        start_game()
    else:
        messagebox.showerror("Error", "Invalid credentials.")

def start_game():
    root.withdraw()
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Flying Bird Game')

    background_color = (135, 206, 235)

    bird_image = pygame.image.load('bird.png')
    bird_image = pygame.transform.scale(bird_image, (200, 200))
    bird_x = 300
    bird_y = 200
    bird_direction = 1

    start_time = time.time()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bird_y += bird_direction * 1
        if bird_y > 400 or bird_y < 100:
            bird_direction *= -1  

        screen.fill(background_color)
        screen.blit(bird_image, (bird_x, bird_y))
        pygame.display.flip()

        if time.time() - start_time > 10:
            running = False

    pygame.quit()
    show_turtle_design()

def show_turtle_design():
    turtle.setup(800, 600)
    turtle.bgcolor("black")
    turtle.speed(2)
    
    for i in range(5):
        turtle.color("yellow")
        turtle.forward(100)
        turtle.right(144)

    turtle.hideturtle()
    
    turtle.penup()
    turtle.goto(0, -100)
    turtle.color("white")
    turtle.write("Thank You!", align="center", font=("Arial", 24, "bold"))
    
    turtle.done()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login System")
    login_page()
    root.mainloop()
