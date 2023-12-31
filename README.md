# Markov_Artist



My markov artist generates a unique piece of artwork by placing colored dots on a randomly selected background image. The dots' movement direction and size are influenced by specified transition matrices, working in the form of a markov chain: given the current direction or size, the matrices determine the probabilities of the next direction or size. The artwork starts with a random position on the canvas, and for 20,000 iterations, it calculates a new position and size for the next dot based on probabilities, colors it with a random color, and places it on the canvas. 
# Why was this meaningful?

This system is personally meaningful to me because of the two forms of art it combines. The background of each painting
is one of a set of images from a book that I read a lot as a child called The World We Live In. I remember loving the
pictures of the dinosaurs in the book, and being amazed by how detailed each of the drawings were. Overlayed is a more
abstract style of art painted by my Markov artist. As a kid my grandpa would take me to the art museum a lot and I never
liked the abstract art. I think I thought it was too simplistic and a little bit weird. My goal with this project was to
combine the two styles one I loved and one I did not like at all to create a unique combination.

# What made this project challenging?

This project was an important project for me as a programmer because I learned how to directly impliment a simple markov chain to create a piece of art.
One element of this project that challenged me as a computer scientist was figuring out how to place the dots on the
painting. I needed to format a system that could consider where the program wanted to place the next dot and compare
that to the size of the canvas to determine if the next placement was viable. This check was necessary because without
it the algorithm which determines where it wants to place the next dot would continue to place dots off of the canvas.
This was challenging because I needed to take a new direction from the transition matrix, and analyze the result of
using it in the painting. For example, if the last placed dot was in the upper left corner of the canvas, and the new
direction was to place a dot to the left of that it would be off the canvas and thus unviable. I pushed myself outside my comfort zone by using a python drawing package called Cairo that I had never worked with before. I was tempted at
first to go the rout of something more simple and familiar like the Turtle draw package from 1101, but the decision to
challenge myself was well worth it in the added functionality I got from Cairo. Going forward if I were to expand on
this project it would be cool to do more analysis on the background painting to influence where the dots should be
placed and what color they should be. 

# Why is this project creative?

I believe my project is creative because of the combination of the two art styles.
I have seen a fair bit of art in my life but nothing too similar to what my markov artist creates. That said I think it could be made more creative by having some greater level of crossover between the two elements of the painting. For example the placement and color of the dots could take into account the underlying image.

# Sources

All images are from LIFE magazine, as well as LIFE's The World We Live In by Lincoln Barnett