title: Teaching Programming with Human Functions
date: 2014-02-08
category: Programming
tags: Tech, STEM, Ruby
summary: Functions are a pretty big concept for a new programmer to grasp. Here's a technique I found useful for teaching kids about Ruby functions.


Today, in my [RubyStory]({filename}/Teaching_Kids_Programming_With_RubyStory.md) class, I attempted to introduce the kids to Ruby functions. I won't go so far as to say it was a disaster, but it didn't go particularly well. They just didn't get it.

OK. Functions are a pretty big concept for a new programmer to grasp.

I also made a major mistake: too much talking, not enough coding. The kids are much happier and seem to understand better when actually writing code, making things happen and experimenting on their own.

I did experiment with a different kind of example, however, and it seemed to bring some fun and understanding: "human functions."

Basically, the kids became functions and we interactively ran the program by talking to each other. Here's how it worked.

First, I took one of the students, Sophie, aside and gave her some secret instructions: 

> Take the word you're given and use it in a sentence.

Then, one of the other students would "call" her with a word: "Sophie: donuts." Sophie would respond "I love to eat donuts."

We had some fun with it, as 10 year old kids will, and changed up the examples a bit. As I explained, this pretty much equates to the following code.

```ruby
def sophie(word)
    puts "I love to eat " + word
end

sophie("donuts")
```

This seemed to help the kids understand a lot better. I think next class we'll start out with more exercises like this before moving to the code. We could get multiple human functions involved to demonstrate how functions generalize tasks within a program.

For example, here's a simplified version of our storytelling program.

```ruby
def prompt(choice1, choice2)
    print "Which do you choose (%s or %s): " % [choice_1, choice_2]
    answer = gets.chomp
    return answer
end

def story
    puts "A zombie appears. Do you run or fight?"
    action = prompt("run", "fight")

    if action == "run"
        puts "Chicken! Bawk bawk bawk!"
    elsif action == "fight"
        winorlose
    end
end

def winorlose
    puts "Rolling the dice..."
    diceroll = 1 + rand(6)

    if diceroll > 3
        puts "Yay! You win!"
    else
        puts "Sorry, you lose."
    end
end
```

My human functions can run this program.

1. Kendall starts the story, and passes the the prompt to Arden.
2. Arden asks Teddy the question and returns his answer to Kendall.
3. Kendall either ends the story ("run") or calls Sophie ("fight").
4. Sophie rolls a die and, depending on the roll, tells Teddy whether he won or lost.

We'll have to see how it works. Looks like I've got a bit of writing and scheming to do before the next lesson.