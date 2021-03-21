### CMPSC 100: G. Wiz and the Mega Move

![It'd be fun they said...](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-mega-move.png)

Of course, now that you and G. Wiz are friends, it's high time that they ask you for a favor. In this case, it's a hand in packing boxes for their upcoming move. Arriving at their place, you're quickly put to work packing up part of their study, which includes all kinds of strange and wonderous wizardy stuff. (Be careful with the hats -- they trust you!)

Your job is to put the following ten (10) items into a `box` and unpack that `box` at G. Wiz's new, spacious wizard pad:

1. Purple wizard hat
2. Magic dust
3. Box of magic wands
4. Blue wizard hat
5. Stack of Clawparazzis
6. Glass beaker
7. Green wizard hat
8. Lizard Wizard action figure
9. G. Wiz self portrait
10. Insect collection case

Fast forward some short time later, you arrive at G. Wiz's new place and are put in charge of unpacking the box you put together earlier. 

Recall that the _last item_ you put in should be the _first item_ to come out, and so forth.

### Sample output

```
Label for the box: {YOUR LABEL HERE}

Item to add: purple wizard hat
Magic dust added to the box.

Add another item to the box? [Y]es/[N]o: Y
...

Packed box:
purple wizard hat
magic dust
box of magic wands
blue wizard hat
stack of Clawparazzis
glass beaker
green wizard hat
Lizard Wizard action figure
G. Wiz self portrait
insect collection case

Items removed from the {YOUR LABEL HERE} box:

insect collection case removed from the box
G. Wiz self portrait removed from the box
Lizard Wizard action figure removed from the box
green wizard hat removed from the box
glass beaker removed from the box
stack of Clawparazzis removed from the box
blue wizard hat removed from the box
box of magic wands removed from the box
magic dust removed from the box
purple wizard hat removed from the box

The box is now empty!
```

## General guidelines for laboratory sessions

---

* Follow steps carefully. Laboratory sessions often get a bit more complicated than their preceeding course sessions. Especially for early sessions which expose you to platforms with which you may not be familiar, take notes on commands you run and their corresponding effects/outputs. If you find yourself stuck on a step, let a TL or the professor know! Laboratory sessions do not mean that we won't guide you in the same way we do during other sessions.
* Regularly ask and answer questions. Some of you may have more experience with the topics we're discussing than others. We can use this knowledge to our advantage. Let students try things for a while before offering help (always offer first). To ask questions, use your group's Slack channel or TL channels.
* Store and transfer files using GitHub. Various forms of file storage are more or less volatile. You are responsible for backing up and storing files. If you're unsure of files which have been changed, you can always type git status in the terminal for your working folder to determine what you need to back up.
* Keep all of your files. See above, but also remember that you're responsible for the files you create.
* Back up your files regularly. See above (and above-above).
* Review the Honor Code regularly when working. If you're taking a solution from another student or the Internet at-large (especially Stack Overflow), bear in mind that using these solutions can constitute a form of plagiarism that violates the Allegheny Honor Code. While it may seem easy and convenient to use these sources, it is equally easy and convenient to rely on them and create bad habits which include not attributing credit or relying exclusively on others to solve issues. Neither are productive uses of your intellect. Really.

## Requirements

---

### The `*.py` file

Your program should:

#### Packing up

* Create a varible called `box` to store the items
* Take `input` at a prompt to add items to the box
* `append` the items to the `box`
* Add a label to the box using a `string` called `label`
* `print` the final box contents

#### Unpacking

* `print` the box label
* Take items out of the `box` one by one
  * This includes using the `del` function
* `print` the items as they come out of the box to inventory them
* When the box is empty, print `The box is empty!`

### `reflection.md`

* At least 300 words
* Responds to all questions
* Contains `0` `TODO` markers